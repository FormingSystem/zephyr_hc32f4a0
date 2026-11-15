---
id: learning.zephyr-docs.kconfig-reference.page-402
title: "`subsys/net`配置项参考（12/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第402章\_`subsys/net`配置项参考（12/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_LLDP_CHASSIS_ID_MAC4"></a>

## 402.1 `CONFIG_NET_LLDP_CHASSIS_ID_MAC4`

**提示（Prompt）**：机箱标识符（Chassis ID）MAC 地址的字节 4

**说明（Help）**

MAC 地址的字节 4。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE = 4 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0x53
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:111`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L111)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_CHASSIS_ID_MAC5"></a>

## 402.2 `CONFIG_NET_LLDP_CHASSIS_ID_MAC5`

**提示（Prompt）**：机箱标识符（Chassis ID）MAC 地址的字节 5

**说明（Help）**

MAC 地址的字节 5。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE = 4 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0x8d
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE"></a>

## 402.3 `CONFIG_NET_LLDP_CHASSIS_ID_SUBTYPE`

**提示（Prompt）**：机箱标识符（Chassis ID）TLV 子类型（Subtype）

**说明（Help）**

机箱标识符（Chassis ID）的子类型如下，详见 IEEE 802.1AB 第 8.5.2.2 节。

| 子类型（Subtype） | 含义 |
| --- | --- |
| 1 | 机箱组件（Chassis component） |
| 2 | 接口别名（Interface alias） |
| 3 | 端口组件（Port component） |
| 4 | MAC 地址（MAC address） |
| 5 | 网络地址（Network address） |
| 6 | 接口名称（Interface name） |
| 7 | 本地分配（Locally assigned） |

选择子类型 4，即 MAC 地址时，必须定义 `NET_LLDP_CHASSIS_ID_MAC0` 至 `NET_LLDP_CHASSIS_ID_MAC5`；否则必须改用 `NET_LLDP_CHASSIS_ID`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 7]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:64`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L64)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_END_LLDPDU_TLV_ENABLED"></a>

## 402.4 `CONFIG_NET_LLDP_END_LLDPDU_TLV_ENABLED`

**提示（Prompt）**：LLDPDU 结束 TLV（End of LLDPDU TLV）

**说明（Help）**

指定是否在 LLDP 协议数据单元（LLDPDU）数据包末尾包含结束标记（End marker）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:55`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L55)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_LOG_LEVEL_CHOICE"></a>

## 402.5 `CONFIG_NET_LLDP_LOG_LEVEL_CHOICE`

**提示（Prompt）**：链路层发现协议（LLDP）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_LLDP_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_LLDP_LOG_LEVEL_OFF
CONFIG_NET_LLDP_LOG_LEVEL_ERR
CONFIG_NET_LLDP_LOG_LEVEL_WRN
CONFIG_NET_LLDP_LOG_LEVEL_INF
CONFIG_NET_LLDP_LOG_LEVEL_DBG
CONFIG_NET_LLDP_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_LLDP_LOG_LEVEL_DEFAULT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_LLDP_LOG_LEVEL_OFF`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_LOG_LEVEL_OFF)、[`CONFIG_NET_LLDP_LOG_LEVEL_ERR`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_LOG_LEVEL_ERR)、[`CONFIG_NET_LLDP_LOG_LEVEL_WRN`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_LOG_LEVEL_WRN)、[`CONFIG_NET_LLDP_LOG_LEVEL_INF`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_LOG_LEVEL_INF)、[`CONFIG_NET_LLDP_LOG_LEVEL_DBG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_LLDP_LOG_LEVEL_DBG"></a>

## 402.6 `CONFIG_NET_LLDP_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_LLDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP） → 链路层发现协议（LLDP）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_LLDP_LOG_LEVEL_DEFAULT"></a>

## 402.7 `CONFIG_NET_LLDP_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_LLDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP） → 链路层发现协议（LLDP）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_LLDP_LOG_LEVEL_ERR"></a>

## 402.8 `CONFIG_NET_LLDP_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_LLDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP） → 链路层发现协议（LLDP）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_LLDP_LOG_LEVEL_INF"></a>

## 402.9 `CONFIG_NET_LLDP_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_LLDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP） → 链路层发现协议（LLDP）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_LLDP_LOG_LEVEL_OFF"></a>

## 402.10 `CONFIG_NET_LLDP_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_LLDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP） → 链路层发现协议（LLDP）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_LLDP_LOG_LEVEL_WRN"></a>

## 402.11 `CONFIG_NET_LLDP_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_LLDP_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP） → 链路层发现协议（LLDP）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_LLDP_PORT_ID"></a>

## 402.12 `CONFIG_NET_LLDP_PORT_ID`

**提示（Prompt）**：端口标识符（Port ID）的值

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_PORT_ID_SUBTYPE != 3 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"PORT_ID_PLACEHOLDER"
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:196`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L196)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_PORT_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_PORT_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_PORT_ID_MAC0"></a>

## 402.13 `CONFIG_NET_LLDP_PORT_ID_MAC0`

**提示（Prompt）**：机箱标识符（Chassis ID）MAC 地址的字节 0

**说明（Help）**

MAC 地址的字节 0。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_PORT_ID_SUBTYPE = 3 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0x00
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:153`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L153)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_PORT_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_PORT_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_PORT_ID_MAC1"></a>

## 402.14 `CONFIG_NET_LLDP_PORT_ID_MAC1`

**提示（Prompt）**：机箱标识符（Chassis ID）MAC 地址的字节 1

**说明（Help）**

MAC 地址的字节 1。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_PORT_ID_SUBTYPE = 3 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0x00
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:160`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L160)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_PORT_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_PORT_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_PORT_ID_MAC2"></a>

## 402.15 `CONFIG_NET_LLDP_PORT_ID_MAC2`

**提示（Prompt）**：机箱标识符（Chassis ID）MAC 地址的字节 2

**说明（Help）**

MAC 地址的字节 2。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_PORT_ID_SUBTYPE = 3 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0x5e
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_PORT_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_PORT_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_PORT_ID_MAC3"></a>

## 402.16 `CONFIG_NET_LLDP_PORT_ID_MAC3`

**提示（Prompt）**：机箱标识符（Chassis ID）MAC 地址的字节 3

**说明（Help）**

MAC 地址的字节 3。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_PORT_ID_SUBTYPE = 3 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0x00
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:174`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L174)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_PORT_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_PORT_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_PORT_ID_MAC4"></a>

## 402.17 `CONFIG_NET_LLDP_PORT_ID_MAC4`

**提示（Prompt）**：机箱标识符（Chassis ID）MAC 地址的字节 4

**说明（Help）**

MAC 地址的字节 4。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_PORT_ID_SUBTYPE = 3 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0x53
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_PORT_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_PORT_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_PORT_ID_MAC5"></a>

## 402.18 `CONFIG_NET_LLDP_PORT_ID_MAC5`

**提示（Prompt）**：机箱标识符（Chassis ID）MAC 地址的字节 5

**说明（Help）**

MAC 地址的字节 5。

**类型（Type）**：十六进制整数（Hexadecimal），`hex`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP_PORT_ID_SUBTYPE = 3 && CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0x8d
```

**取值范围（Ranges）**

```text
[0, 0xff]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:188`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L188)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP_PORT_ID_SUBTYPE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LLDP_PORT_ID_SUBTYPE)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_PORT_ID_SUBTYPE"></a>

## 402.19 `CONFIG_NET_LLDP_PORT_ID_SUBTYPE`

**提示（Prompt）**：端口标识符（Port ID）TLV 子类型（Subtype）

**说明（Help）**

端口标识符（Port ID）的子类型如下，详见 IEEE 802.1AB 第 8.5.3.2 节。

| 子类型（Subtype） | 含义 |
| --- | --- |
| 1 | 接口别名（Interface alias） |
| 2 | 端口组件（Port component） |
| 3 | MAC 地址（MAC address） |
| 4 | 网络地址（Network address） |
| 5 | 接口名称（Interface name） |
| 6 | 代理电路标识符（Agent circuit ID） |
| 7 | 本地分配（Locally assigned） |

选择子类型 3，即 MAC 地址时，必须定义 `NET_LLDP_PORT_ID_MAC0` 至 `NET_LLDP_PORT_ID_MAC5`；否则必须改用 `NET_LLDP_PORT_ID`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5
```

**取值范围（Ranges）**

```text
[1, 7]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:134`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L134)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_TX_HOLD"></a>

## 402.20 `CONFIG_NET_LLDP_TX_HOLD`

**提示（Prompt）**：以发送间隔乘数计算生存时间（Time to Live）

**说明（Help）**

此值 `msgTxHold` 乘以 `CONFIG_NET_LLDP_TX_INTERVAL`，得到 LLDP 帧中的生存时间（Time to Live，TTL）。更多信息参见 LLDP 规范第 9.2.5.6 节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[1, 100]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:42`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L42)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LLDP_TX_INTERVAL"></a>

## 402.21 `CONFIG_NET_LLDP_TX_INTERVAL`

**提示（Prompt）**：发送间隔（msgTxInterval，秒）

**说明（Help）**

正常发送期间，即非快速模式（Non-fast mode）下，两次发送 LLDP 协议数据单元（LLDPDU）的间隔。更多信息参见 LLDP 规范第 9.2.5.7 节。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LLDP && CONFIG_NET_L2_ETHERNET && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
30
```

**取值范围（Ranges）**

```text
[1, 3600]
```

**定义位置（Location）**：[`subsys/net/l2/ethernet/lldp/Kconfig:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/l2/ethernet/lldp/Kconfig#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 链路层选项（Link layer options） → 以太网支持（Ethernet support） → 链路层发现协议（Link Layer Discovery Protocol，LLDP）

**配置项引用（Symbol References）**：[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_LOG"></a>

## 402.22 `CONFIG_NET_LOG`

**提示（Prompt）**：网络协议栈日志与调试（Logging and debugging）

**说明（Help）**

在网络协议栈的各部分启用日志（Logging），同时开放 IPv6、IPv4 等其他子菜单中的具体调试选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_LOG
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.debug:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.debug#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)。

<a id="CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE"></a>

## 402.23 `CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE`

**提示（Prompt）**：网络环回驱动（Network loopback driver）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_LOG && CONFIG_NET_LOOPBACK && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
CONFIG_NET_LOOPBACK_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_LOOPBACK_LOG_LEVEL_OFF
CONFIG_NET_LOOPBACK_LOG_LEVEL_ERR
CONFIG_NET_LOOPBACK_LOG_LEVEL_WRN
CONFIG_NET_LOOPBACK_LOG_LEVEL_INF
CONFIG_NET_LOOPBACK_LOG_LEVEL_DBG
CONFIG_NET_LOOPBACK_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 网络回环（Loopback）驱动

**配置项引用（Symbol References）**：[`CONFIG_LOG`](P367_subsys_logging_配置项参考_16.md#CONFIG_LOG)、[`CONFIG_NET_LOOPBACK`](P131_drivers_net_配置项参考.md#CONFIG_NET_LOOPBACK)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)、[`CONFIG_NET_LOOPBACK_LOG_LEVEL_DEFAULT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOOPBACK_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_LOOPBACK_LOG_LEVEL_OFF`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOOPBACK_LOG_LEVEL_OFF)、[`CONFIG_NET_LOOPBACK_LOG_LEVEL_ERR`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOOPBACK_LOG_LEVEL_ERR)、[`CONFIG_NET_LOOPBACK_LOG_LEVEL_WRN`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOOPBACK_LOG_LEVEL_WRN)、[`CONFIG_NET_LOOPBACK_LOG_LEVEL_INF`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOOPBACK_LOG_LEVEL_INF)、[`CONFIG_NET_LOOPBACK_LOG_LEVEL_DBG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOOPBACK_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_LOOPBACK_LOG_LEVEL_DBG"></a>

## 402.24 `CONFIG_NET_LOOPBACK_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 网络回环（Loopback）驱动 → 网络环回驱动（Network loopback driver）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_LOOPBACK_LOG_LEVEL_DEFAULT"></a>

## 402.25 `CONFIG_NET_LOOPBACK_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 网络回环（Loopback）驱动 → 网络环回驱动（Network loopback driver）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_LOOPBACK_LOG_LEVEL_ERR"></a>

## 402.26 `CONFIG_NET_LOOPBACK_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 网络回环（Loopback）驱动 → 网络环回驱动（Network loopback driver）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_LOOPBACK_LOG_LEVEL_INF"></a>

## 402.27 `CONFIG_NET_LOOPBACK_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 网络回环（Loopback）驱动 → 网络环回驱动（Network loopback driver）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_LOOPBACK_LOG_LEVEL_OFF"></a>

## 402.28 `CONFIG_NET_LOOPBACK_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 网络回环（Loopback）驱动 → 网络环回驱动（Network loopback driver）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_LOOPBACK_LOG_LEVEL_WRN"></a>

## 402.29 `CONFIG_NET_LOOPBACK_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 网络回环（Loopback）驱动 → 网络环回驱动（Network loopback driver）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOOPBACK_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_MAX_6LO_CONTEXTS"></a>

## 402.30 `CONFIG_NET_MAX_6LO_CONTEXTS`

**提示（Prompt）**：支持的 6LoWPAN 上下文选项（Context Option，6CO）数量

**说明（Help）**

6LoWPAN 上下文选项（Context option）表的大小。根据网络需求和内存消耗设置；更多 6CO 选项会占用更多内存。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_6LO_CONTEXT && CONFIG_NET_NATIVE_IPV6 && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 16]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:604`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L604)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 低功耗无线个域网 IPv6 压缩库（6LoWPAN） → 基于上下文的 6LoWPAN 压缩（context based compression）

**配置项引用（Symbol References）**：[`CONFIG_NET_6LO_CONTEXT`](P395_subsys_net_配置项参考_5.md#CONFIG_NET_6LO_CONTEXT)、[`CONFIG_NET_NATIVE_IPV6`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IPV6)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IPV6`。

<a id="CONFIG_NET_MAX_CONN"></a>

## 402.31 `CONFIG_NET_MAX_CONN`

**提示（Prompt）**：支持的网络连接（Network connection）数量

**说明（Help）**

该值取决于网络需求，应同时计入 UDP 和 TCP 连接。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_UDP || CONFIG_NET_TCP || CONFIG_NET_SOCKETS_PACKET || CONFIG_NET_SOCKETS_CAN) && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8 if CONFIG_NET_IPV6 && CONFIG_NET_IPV4
4
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:544`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L544)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_UDP)、[`CONFIG_NET_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TCP)、[`CONFIG_NET_SOCKETS_PACKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_PACKET)、[`CONFIG_NET_SOCKETS_CAN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_CAN)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)。

<a id="CONFIG_NET_MAX_CONTEXTS"></a>

## 402.32 `CONFIG_NET_MAX_CONTEXTS`

**提示（Prompt）**：要分配的网络上下文（Network context）数量

**说明（Help）**

每个网络上下文（Network context）描述监听或发送网络流量时使用的网络五元组（Network 5-tuple），与其他系统中通常称为网络套接字（Network socket）的对象非常相似。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
6
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:559`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L559)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_MAX_MCAST_ROUTES"></a>

## 402.33 `CONFIG_NET_MAX_MCAST_ROUTES`

**提示（Prompt）**：可存储的多播路由表项（Multicast routing entry）最大数量［已弃用，Deprecated］

**说明（Help）**

决定多播路由表（Multicast routing table）能够存储多少个表项。此符号已弃用，请改用 `NET_IPV6_MAX_MCAST_ROUTES`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ROUTE_MCAST && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:57`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L57)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 多播路由与转发（Multicast Routing / Forwarding）［已弃用，Deprecated］

**配置项引用（Symbol References）**：[`CONFIG_NET_ROUTE_MCAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE_MCAST)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_MAX_NEXTHOPS"></a>

## 402.34 `CONFIG_NET_MAX_NEXTHOPS`

**提示（Prompt）**：可存储的下一跳表项（Next hop entry）最大数量［已弃用，Deprecated］

**说明（Help）**

决定下一跳表（Nexthop table）能够存储多少个表项。此符号已弃用，请改用 `NET_IPV6_MAX_NEXTHOPS`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ROUTE && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_MAX_ROUTES
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_ROUTE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MAX_ROUTES`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MAX_ROUTES)。

<a id="CONFIG_NET_MAX_ROUTERS"></a>

## 402.35 `CONFIG_NET_MAX_ROUTERS`

**提示（Prompt）**：支持的路由器（Router）数量

**说明（Help）**

该值取决于网络需求。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
!CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2 if CONFIG_NET_IPV4 && CONFIG_NET_IPV6
1 if CONFIG_NET_IPV4 && !CONFIG_NET_IPV6
1 if !CONFIG_NET_IPV4 && CONFIG_NET_IPV6
```

**取值范围（Ranges）**

```text
[1, 254]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:443`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L443)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)。

<a id="CONFIG_NET_MAX_ROUTES"></a>

## 402.36 `CONFIG_NET_MAX_ROUTES`

**提示（Prompt）**：可存储的路由表项（Routing entry）最大数量［已弃用，Deprecated］

**说明（Help）**

决定路由表（Routing table）能够存储多少个表项。此符号已弃用，请改用 `NET_IPV6_MAX_ROUTES`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ROUTE && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_IPV6_MAX_NEIGHBORS
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版）

**配置项引用（Symbol References）**：[`CONFIG_NET_ROUTE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV6_MAX_NEIGHBORS`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_MAX_NEIGHBORS)。

<a id="CONFIG_NET_MCAST_ROUTE_MAX_IFACES"></a>

## 402.37 `CONFIG_NET_MCAST_ROUTE_MAX_IFACES`

**提示（Prompt）**：每个多播路由表项可关联的网络接口最大数量［已弃用，Deprecated］

**说明（Help）**

决定单个多播路由表项（Multicast route entry）可以分配多少个网络接口。此符号已弃用，请改用 `NET_IPV6_MCAST_ROUTE_MAX_IFACES`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ROUTE_MCAST && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**取值范围（Ranges）**

```text
[1, 8]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 多播路由与转发（Multicast Routing / Forwarding）［已弃用，Deprecated］

**配置项引用（Symbol References）**：[`CONFIG_NET_ROUTE_MCAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE_MCAST)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_MCAST_ROUTE_MLD_REPORTS"></a>

## 402.38 `CONFIG_NET_MCAST_ROUTE_MLD_REPORTS`

**提示（Prompt）**：在 MLDv2 报告中报告多播路由（Multicast route）［已弃用，Deprecated］

**说明（Help）**

决定是否在 MLDv2 报告中通告多播路由表项（Multicast route entry）。此符号已弃用，请改用 `NET_IPV6_MCAST_ROUTE_MLD_REPORTS`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_ROUTE_MCAST && CONFIG_NET_IPV6_MLD && CONFIG_NET_IPV6 && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_DEPRECATED
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.ipv6:76`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.ipv6#L76)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → IPv6（互联网协议第 6 版） → 多播路由与转发（Multicast Routing / Forwarding）［已弃用，Deprecated］

**配置项引用（Symbol References）**：[`CONFIG_NET_ROUTE_MCAST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ROUTE_MCAST)、[`CONFIG_NET_IPV6_MLD`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_MLD)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_RAW_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_DEPRECATED`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_DEPRECATED)。

<a id="CONFIG_NET_MGMT"></a>

## 402.39 `CONFIG_NET_MGMT`

**提示（Prompt）**：网络管理 API（Network Management API）

**说明（Help）**

添加网络管理（Network Management，NM）API 支持，用于管理网络协议栈的各个方面，并接收网络事件通知，例如 IP 地址改变、接口启用并运行等。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_L2_VIRTUAL_MGMT
CONFIG_NET_L2_ETHERNET_MGMT
CONFIG_NET_LLDP
CONFIG_NET_L2_PPP
CONFIG_NET_L2_PPP_MGMT
CONFIG_NET_L2_IEEE802154_MGMT
CONFIG_NET_L2_WIFI_MGMT
CONFIG_NET_PMTU
CONFIG_NET_IPV6_PE
CONFIG_NET_IPV4_AUTO
CONFIG_NET_PROMISCUOUS_MODE
CONFIG_NET_STATISTICS_USER_API
CONFIG_MDNS_RESPONDER_PROBE
CONFIG_MCP_HTTP_LOG_ADDRESS
CONFIG_NET_CONFIG_SETTINGS
CONFIG_NET_CAPTURE
CONFIG_NET_DHCPV4
CONFIG_NET_DHCPV6
CONFIG_NET_DHCPV6_SERVER
CONFIG_WIREGUARD
CONFIG_NET_CONNECTION_MANAGER
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_VIRTUAL_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_MGMT)、[`CONFIG_NET_L2_ETHERNET_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_ETHERNET_MGMT)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NET_L2_PPP_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_MGMT)、[`CONFIG_NET_L2_IEEE802154_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_MGMT)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NET_PMTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PMTU)、[`CONFIG_NET_IPV6_PE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE)、[`CONFIG_NET_IPV4_AUTO`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO)、[`CONFIG_NET_PROMISCUOUS_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PROMISCUOUS_MODE)、[`CONFIG_NET_STATISTICS_USER_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_STATISTICS_USER_API)、[`CONFIG_MDNS_RESPONDER_PROBE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_PROBE)、[`CONFIG_MCP_HTTP_LOG_ADDRESS`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_HTTP_LOG_ADDRESS)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NET_DHCPV6`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6)、[`CONFIG_NET_DHCPV6_SERVER`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER)、[`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)、[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_L2_IEEE802154_MGMT`、`CONFIG_NET_PMTU`。

<a id="CONFIG_NET_MGMT_EVENT"></a>

## 402.40 `CONFIG_NET_MGMT_EVENT`

**提示（Prompt）**：添加运行时网络事件通知支持（event notifications）

**说明（Help）**

允许网络协议栈向相关监听者（Listener）通知事件。当应用或其他组件需要在特定网络事件发生时，例如 IP 地址改变时，得到通知并触发相关工作，就可能需要此功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_L2_VIRTUAL_MGMT
CONFIG_NET_L2_ETHERNET_MGMT
CONFIG_NET_LLDP
CONFIG_NET_L2_PPP
CONFIG_NET_L2_PPP_MGMT
CONFIG_NET_L2_IEEE802154_MGMT
CONFIG_NET_L2_WIFI_MGMT
CONFIG_NET_PMTU
CONFIG_NET_IPV6_PE
CONFIG_NET_IPV4_AUTO
CONFIG_NET_PROMISCUOUS_MODE
CONFIG_MDNS_RESPONDER_PROBE
CONFIG_MCP_HTTP_LOG_ADDRESS
CONFIG_NET_CONFIG_SETTINGS
CONFIG_NET_CAPTURE
CONFIG_NET_DHCPV4
CONFIG_NET_DHCPV6
CONFIG_NET_DHCPV6_SERVER
CONFIG_WIREGUARD
CONFIG_NET_CONNECTION_MANAGER
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_VIRTUAL_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_VIRTUAL_MGMT)、[`CONFIG_NET_L2_ETHERNET_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_ETHERNET_MGMT)、[`CONFIG_NET_LLDP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LLDP)、[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NET_L2_PPP_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP_MGMT)、[`CONFIG_NET_L2_IEEE802154_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_IEEE802154_MGMT)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NET_PMTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PMTU)、[`CONFIG_NET_IPV6_PE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE)、[`CONFIG_NET_IPV4_AUTO`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO)、[`CONFIG_NET_PROMISCUOUS_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PROMISCUOUS_MODE)、[`CONFIG_MDNS_RESPONDER_PROBE`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER_PROBE)、[`CONFIG_MCP_HTTP_LOG_ADDRESS`](P394_subsys_net_配置项参考_4.md#CONFIG_MCP_HTTP_LOG_ADDRESS)、[`CONFIG_NET_CONFIG_SETTINGS`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONFIG_SETTINGS)、[`CONFIG_NET_CAPTURE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CAPTURE)、[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NET_DHCPV6`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6)、[`CONFIG_NET_DHCPV6_SERVER`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_SERVER)、[`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)、[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_L2_IEEE802154_MGMT`、`CONFIG_NET_PMTU`。

<a id="CONFIG_NET_MGMT_EVENT_DIRECT"></a>

## 402.41 `CONFIG_NET_MGMT_EVENT_DIRECT`

**提示（Prompt）**：发出事件时触发回调（Callback）

**说明（Help）**

发出事件时直接调用网络事件处理程序（Network event handler）。启用 `NET_MGMT_EVENT_INFO` 时，向回调处理程序传递数据指针，不复制信息数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MGMT_EVENT_WORKER>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications） → 网络事件调度（Network event scheduling）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_WORKER`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_WORKER)。

<a id="CONFIG_NET_MGMT_EVENT_INFO"></a>

## 402.42 `CONFIG_NET_MGMT_EVENT_INFO`

**提示（Prompt）**：随事件传递信息（Event information）

**说明（Help）**

事件通知者（Event notifier）可随事件提供信息，监听者（Listener）随后可获取这些信息。具体信息取决于事件类型。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_L2_WIFI_MGMT
CONFIG_NET_PMTU
CONFIG_NET_IPV6_PE
CONFIG_NET_IPV4_AUTO
CONFIG_NET_SOCKETS_NET_MGMT
CONFIG_NET_DHCPV4
CONFIG_NET_DHCPV6_DECLINE_ON_DAD_FAILURE
CONFIG_WIREGUARD
CONFIG_NET_CONNECTION_MANAGER
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:91`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L91)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NET_PMTU`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_PMTU)、[`CONFIG_NET_IPV6_PE`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PE)、[`CONFIG_NET_IPV4_AUTO`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_AUTO)、[`CONFIG_NET_SOCKETS_NET_MGMT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_NET_MGMT)、[`CONFIG_NET_DHCPV4`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4)、[`CONFIG_NET_DHCPV6_DECLINE_ON_DAD_FAILURE`](P398_subsys_net_配置项参考_8.md#CONFIG_NET_DHCPV6_DECLINE_ON_DAD_FAILURE)、[`CONFIG_WIREGUARD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD)、[`CONFIG_NET_CONNECTION_MANAGER`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_CONNECTION_MANAGER)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_PMTU`。

<a id="CONFIG_NET_MGMT_EVENT_INFO_DEFAULT_DATA_SIZE"></a>

## 402.43 `CONFIG_NET_MGMT_EVENT_INFO_DEFAULT_DATA_SIZE`

**提示（Prompt）**：事件信息数据（Event information data）的默认大小

**说明（Help）**

可以随事件传递的数据的默认大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT_EVENT_INFO && CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
32
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:100`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L100)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications） → 随事件传递信息（Event information）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_INFO`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_INFO)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE"></a>

## 402.44 `CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE`

**提示（Prompt）**：网络管理事件核心（Network management event core）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_MGMT_EVENT_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_MGMT_EVENT_LOG_LEVEL_OFF
CONFIG_NET_MGMT_EVENT_LOG_LEVEL_ERR
CONFIG_NET_MGMT_EVENT_LOG_LEVEL_WRN
CONFIG_NET_MGMT_EVENT_LOG_LEVEL_INF
CONFIG_NET_MGMT_EVENT_LOG_LEVEL_DBG
CONFIG_NET_MGMT_EVENT_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT_EVENT_LOG_LEVEL_DEFAULT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_MGMT_EVENT_LOG_LEVEL_OFF`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_LOG_LEVEL_OFF)、[`CONFIG_NET_MGMT_EVENT_LOG_LEVEL_ERR`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_LOG_LEVEL_ERR)、[`CONFIG_NET_MGMT_EVENT_LOG_LEVEL_WRN`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_LOG_LEVEL_WRN)、[`CONFIG_NET_MGMT_EVENT_LOG_LEVEL_INF`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_LOG_LEVEL_INF)、[`CONFIG_NET_MGMT_EVENT_LOG_LEVEL_DBG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_MGMT_EVENT_LOG_LEVEL_DBG"></a>

## 402.45 `CONFIG_NET_MGMT_EVENT_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications） → 网络管理事件核心（Network management event core）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_MGMT_EVENT_LOG_LEVEL_DEFAULT"></a>

## 402.46 `CONFIG_NET_MGMT_EVENT_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications） → 网络管理事件核心（Network management event core）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_MGMT_EVENT_LOG_LEVEL_ERR"></a>

## 402.47 `CONFIG_NET_MGMT_EVENT_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications） → 网络管理事件核心（Network management event core）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_MGMT_EVENT_LOG_LEVEL_INF"></a>

## 402.48 `CONFIG_NET_MGMT_EVENT_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications） → 网络管理事件核心（Network management event core）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_MGMT_EVENT_LOG_LEVEL_OFF"></a>

## 402.49 `CONFIG_NET_MGMT_EVENT_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications） → 网络管理事件核心（Network management event core）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_MGMT_EVENT_LOG_LEVEL_WRN"></a>

## 402.50 `CONFIG_NET_MGMT_EVENT_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications） → 网络管理事件核心（Network management event core）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_MGMT_EVENT_MONITOR"></a>

## 402.51 `CONFIG_NET_MGMT_EVENT_MONITOR`

**提示（Prompt）**：通过网络命令行（net shell）监测网络事件

**说明（Help）**

允许用户在网络命令行（net shell）中使用 `net events [on|off]` 命令监测网络事件。监测默认关闭。为避免漏掉事件，通常应将 `NET_MGMT_EVENT_QUEUE_SIZE` 增大到默认值以上。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SHELL && CONFIG_NET_MGMT_EVENT_INFO && CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:106`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L106)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications） → 随事件传递信息（Event information）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SHELL)、[`CONFIG_NET_MGMT_EVENT_INFO`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_INFO)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_MGMT_EVENT_MONITOR_AUTO_START"></a>

## 402.52 `CONFIG_NET_MGMT_EVENT_MONITOR_AUTO_START`

**提示（Prompt）**：启动时自动运行事件监测器（Event monitor）

**说明（Help）**

允许系统启动时自动开始监测网络事件。自动启动默认禁用，使用默认基于 UART 的命令行（Shell）打印数据。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT_EVENT_MONITOR && CONFIG_SHELL_BACKEND_SERIAL && CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:125`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L125)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_MONITOR`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_MONITOR)、[`CONFIG_SHELL_BACKEND_SERIAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_SERIAL)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_MGMT_EVENT_MONITOR_STACK_SIZE"></a>

## 402.53 `CONFIG_NET_MGMT_EVENT_MONITOR_STACK_SIZE`

**提示（Prompt）**：为 `event_mon_stack` 线程分配的栈大小（Stack size）

**说明（Help）**

设置 `event_mon_stack_thread` 的栈大小（Stack size）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT_EVENT_MONITOR && CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1024
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:118`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L118)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_MONITOR`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_MONITOR)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_MGMT_EVENT_QUEUE"></a>

## 402.54 `CONFIG_NET_MGMT_EVENT_QUEUE`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，用于在采用异步回调（Asynchronous callback）时启用网络事件队列（Event queue）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_MGMT_EVENT_THREAD || CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE) && CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:50`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L50)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_THREAD`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_THREAD)、[`CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_MGMT_EVENT_QUEUE_SIZE"></a>

## 402.55 `CONFIG_NET_MGMT_EVENT_QUEUE_SIZE`

**提示（Prompt）**：事件队列（Event queue）的大小

**说明（Help）**

可同时排队的事件数量。原文特别说明：如果第三个事件到来，第一个事件将被移除，且不会生成任何通知。因此，需要根据系统负载和预期用途调整该队列大小。

译注：“第三个事件”是原文采用的表述；此项本身配置的是队列容量，不应据此将所有配置下的容量都理解为固定两个事件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT_EVENT_QUEUE && CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
16 if CONFIG_NET_MGMT_EVENT_MONITOR
5
```

**取值范围（Ranges）**

```text
[1, 1024]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:70`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L70)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_QUEUE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_QUEUE)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT_EVENT_MONITOR`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_MONITOR)。

<a id="CONFIG_NET_MGMT_EVENT_QUEUE_TIMEOUT"></a>

## 402.56 `CONFIG_NET_MGMT_EVENT_QUEUE_TIMEOUT`

**提示（Prompt）**：事件队列（Event queue）的超时

**说明（Help）**

事件队列（Event queue）的超时时间，单位为毫秒，用于等待队列可用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT_EVENT_QUEUE && CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10
```

**取值范围（Ranges）**

```text
[1, 10000]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_QUEUE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_QUEUE)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_MGMT_EVENT_STACK_SIZE"></a>

## 402.57 `CONFIG_NET_MGMT_EVENT_STACK_SIZE`

**提示（Prompt）**：处理事件回调的内部线程的栈大小（Stack size）

**说明（Help）**

设置网络管理（NM）用于在事件发生时执行已注册回调（Callback）的内部栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT_EVENT_THREAD && CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4200 if CONFIG_WIFI_NM_WPA_SUPPLICANT
2048 if CONFIG_COVERAGE_GCOV
840 if CONFIG_X86
800 if CONFIG_THREAD_LOCAL_STORAGE
768
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:58`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L58)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_THREAD`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_THREAD)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_COVERAGE_GCOV`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COVERAGE_GCOV)、[`CONFIG_X86`](P027_arch_Kconfig_配置项参考_2.md#CONFIG_X86)、[`CONFIG_THREAD_LOCAL_STORAGE`](P002_kernel_配置项参考_2.md#CONFIG_THREAD_LOCAL_STORAGE)。

<a id="CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE"></a>

## 402.58 `CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE`

**提示（Prompt）**：系统工作队列（System work queue）

**说明（Help）**

向系统工作队列（System work queue）提交工作，以调度网络事件回调处理程序。启用 `NET_MGMT_EVENT_INFO` 时，数据会复制到消息队列（Message queue）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MGMT_EVENT_WORKER>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:33`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L33)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications） → 网络事件调度（Network event scheduling）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_WORKER`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_WORKER)。

<a id="CONFIG_NET_MGMT_EVENT_THREAD"></a>

## 402.59 `CONFIG_NET_MGMT_EVENT_THREAD`

**提示（Prompt）**：独立网络事件线程（Separate network events thread）

**说明（Help）**

为网络事件回调处理程序创建专用线程（Dedicated thread）。启用 `NET_MGMT_EVENT_INFO` 时，数据会复制到消息队列（Message queue）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MGMT_EVENT_WORKER>
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications） → 网络事件调度（Network event scheduling）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT_WORKER`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_WORKER)。

<a id="CONFIG_NET_MGMT_EVENT_WORKER"></a>

## 402.60 `CONFIG_NET_MGMT_EVENT_WORKER`

**提示（Prompt）**：网络事件调度（Network event scheduling）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_MGMT_EVENT_THREAD
```

**可选项（Choices）**

```text
CONFIG_NET_MGMT_EVENT_THREAD
CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE
CONFIG_NET_MGMT_EVENT_DIRECT
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:22`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L22)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT_EVENT_THREAD`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_THREAD)、[`CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_SYSTEM_WORKQUEUE)、[`CONFIG_NET_MGMT_EVENT_DIRECT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_DIRECT)。

<a id="CONFIG_NET_MGMT_THREAD_PRIORITY"></a>

## 402.61 `CONFIG_NET_MGMT_THREAD_PRIORITY`

**提示（Prompt）**：`net_mgmt` 线程优先级（Thread priority）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT_THREAD_PRIO_CUSTOM && CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NUM_PREEMPT_PRIORITIES
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:151`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L151)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications） → 自定义网络管理（Network management）线程优先级。

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_THREAD_PRIO_CUSTOM`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_THREAD_PRIO_CUSTOM)、[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NUM_PREEMPT_PRIORITIES`](P001_kernel_配置项参考_1.md#CONFIG_NUM_PREEMPT_PRIORITIES)。

<a id="CONFIG_NET_MGMT_THREAD_PRIO_CUSTOM"></a>

## 402.62 `CONFIG_NET_MGMT_THREAD_PRIO_CUSTOM`

**提示（Prompt）**：自定义网络管理（Network management）线程优先级。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT_EVENT && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.mgmt:146`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.mgmt#L146)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络管理 API（Network Management API） → 添加运行时网络事件通知支持（event notifications）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE"></a>

## 402.63 `CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE`

**提示（Prompt）**：网络 MIDI 2.0（Network MIDI2）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NETMIDI2_HOST && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_MIDI2_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_MIDI2_LOG_LEVEL_OFF
CONFIG_NET_MIDI2_LOG_LEVEL_ERR
CONFIG_NET_MIDI2_LOG_LEVEL_WRN
CONFIG_NET_MIDI2_LOG_LEVEL_INF
CONFIG_NET_MIDI2_LOG_LEVEL_DBG
CONFIG_NET_MIDI2_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 网络 MIDI 2 主机，UDP（Network MIDI2 host）【实验性 EXPERIMENTAL】

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NETMIDI2_HOST`](P395_subsys_net_配置项参考_5.md#CONFIG_NETMIDI2_HOST)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MIDI2_LOG_LEVEL_DEFAULT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MIDI2_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_MIDI2_LOG_LEVEL_OFF`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MIDI2_LOG_LEVEL_OFF)、[`CONFIG_NET_MIDI2_LOG_LEVEL_ERR`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MIDI2_LOG_LEVEL_ERR)、[`CONFIG_NET_MIDI2_LOG_LEVEL_WRN`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MIDI2_LOG_LEVEL_WRN)、[`CONFIG_NET_MIDI2_LOG_LEVEL_INF`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MIDI2_LOG_LEVEL_INF)、[`CONFIG_NET_MIDI2_LOG_LEVEL_DBG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MIDI2_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_MIDI2_LOG_LEVEL_DBG"></a>

## 402.64 `CONFIG_NET_MIDI2_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 网络 MIDI 2 主机，UDP（Network MIDI2 host）【实验性 EXPERIMENTAL】 → 网络 MIDI 2.0（Network MIDI2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_MIDI2_LOG_LEVEL_DEFAULT"></a>

## 402.65 `CONFIG_NET_MIDI2_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 网络 MIDI 2 主机，UDP（Network MIDI2 host）【实验性 EXPERIMENTAL】 → 网络 MIDI 2.0（Network MIDI2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_MIDI2_LOG_LEVEL_ERR"></a>

## 402.66 `CONFIG_NET_MIDI2_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 网络 MIDI 2 主机，UDP（Network MIDI2 host）【实验性 EXPERIMENTAL】 → 网络 MIDI 2.0（Network MIDI2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_MIDI2_LOG_LEVEL_INF"></a>

## 402.67 `CONFIG_NET_MIDI2_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 网络 MIDI 2 主机，UDP（Network MIDI2 host）【实验性 EXPERIMENTAL】 → 网络 MIDI 2.0（Network MIDI2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_MIDI2_LOG_LEVEL_OFF"></a>

## 402.68 `CONFIG_NET_MIDI2_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 网络 MIDI 2 主机，UDP（Network MIDI2 host）【实验性 EXPERIMENTAL】 → 网络 MIDI 2.0（Network MIDI2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_MIDI2_LOG_LEVEL_WRN"></a>

## 402.69 `CONFIG_NET_MIDI2_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络协议（Network Protocols） → 网络 MIDI 2 主机，UDP（Network MIDI2 host）【实验性 EXPERIMENTAL】 → 网络 MIDI 2.0（Network MIDI2）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MIDI2_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_NAMESPACE_COMPAT_MODE"></a>

## 402.70 `CONFIG_NET_NAMESPACE_COMPAT_MODE`

**提示（Prompt）**：网络命名空间兼容模式（Network namespace compatibility mode）

**说明（Help）**

网络 API 和代码现在已使用命名空间，即相关 API 带有 `net_`、`NET_` 或 `ZSOCK_` 前缀。这可以避免与可能定义重复符号的 POSIX 子系统之间产生循环依赖（Circular dependency）。兼容模式未来将被弃用，最终移除。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(!CONFIG_NET_TEST || CONFIG_POSIX_API) && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:11`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L11)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TEST)、[`CONFIG_POSIX_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_API)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_NATIVE"></a>

## 402.71 `CONFIG_NET_NATIVE`

**提示（Prompt）**：原生网络协议栈（Native network stack）支持

**说明（Help）**

启用 Zephyr 原生网络协议栈（Native networking stack）。如果禁用此项而仍需要网络连接，则必须启用网络卸载（Offloading）支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_OFFLOAD"></a>

## 402.72 `CONFIG_NET_OFFLOAD`

**提示（Prompt）**：卸载 IP 协议栈（Offload IP stack）

**说明（Help）**

允许将 TCP/IP 协议栈卸载到协处理器（Co-processor）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_MODEM_HL7800
CONFIG_MODEM_HL78XX
CONFIG_MODEM_SIM7080
CONFIG_MODEM_ST87MXX
CONFIG_MODEM_UBLOX_SARA
CONFIG_MODEM_WNCM14A2A
CONFIG_WIFI_OFFLOAD
CONFIG_WIFI_ESWIFI
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:98`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L98)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MODEM_HL7800`](P125_drivers_modem_配置项参考_1.md#CONFIG_MODEM_HL7800)、[`CONFIG_MODEM_HL78XX`](P126_drivers_modem_配置项参考_2.md#CONFIG_MODEM_HL78XX)、[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM_ST87MXX`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_ST87MXX)、[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_MODEM_WNCM14A2A`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_WNCM14A2A)、[`CONFIG_WIFI_OFFLOAD`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_OFFLOAD)、[`CONFIG_WIFI_ESWIFI`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI)。

<a id="CONFIG_NET_OFFLOADING_SUPPORT"></a>

## 402.73 `CONFIG_NET_OFFLOADING_SUPPORT`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

隐藏选项，当 `NET_OFFLOAD` 或 `NET_SOCKETS_OFFLOAD` 中任意一个启用时设置，使代码只需检查一个选项而不必检查两个。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_NET_OFFLOAD || CONFIG_NET_SOCKETS_OFFLOAD
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_OFFLOAD`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD)、[`CONFIG_NET_SOCKETS_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD)。

<a id="CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE"></a>

## 402.74 `CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE`

**提示（Prompt）**：卸载层（Offload layer）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_OFFLOAD && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_OFFLOAD_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_OFFLOAD_LOG_LEVEL_OFF
CONFIG_NET_OFFLOAD_LOG_LEVEL_ERR
CONFIG_NET_OFFLOAD_LOG_LEVEL_WRN
CONFIG_NET_OFFLOAD_LOG_LEVEL_INF
CONFIG_NET_OFFLOAD_LOG_LEVEL_DBG
CONFIG_NET_OFFLOAD_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_OFFLOAD`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_OFFLOAD_LOG_LEVEL_DEFAULT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_OFFLOAD_LOG_LEVEL_OFF`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD_LOG_LEVEL_OFF)、[`CONFIG_NET_OFFLOAD_LOG_LEVEL_ERR`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD_LOG_LEVEL_ERR)、[`CONFIG_NET_OFFLOAD_LOG_LEVEL_WRN`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD_LOG_LEVEL_WRN)、[`CONFIG_NET_OFFLOAD_LOG_LEVEL_INF`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD_LOG_LEVEL_INF)、[`CONFIG_NET_OFFLOAD_LOG_LEVEL_DBG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_OFFLOAD_LOG_LEVEL_DBG"></a>

## 402.75 `CONFIG_NET_OFFLOAD_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 卸载层（Offload layer）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_OFFLOAD_LOG_LEVEL_DEFAULT"></a>

## 402.76 `CONFIG_NET_OFFLOAD_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 卸载层（Offload layer）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_OFFLOAD_LOG_LEVEL_ERR"></a>

## 402.77 `CONFIG_NET_OFFLOAD_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 卸载层（Offload layer）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_OFFLOAD_LOG_LEVEL_INF"></a>

## 402.78 `CONFIG_NET_OFFLOAD_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 卸载层（Offload layer）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_OFFLOAD_LOG_LEVEL_OFF"></a>

## 402.79 `CONFIG_NET_OFFLOAD_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 卸载层（Offload layer）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_OFFLOAD_LOG_LEVEL_WRN"></a>

## 402.80 `CONFIG_NET_OFFLOAD_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 卸载层（Offload layer）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_OFFLOAD_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_ALLOC_STATS"></a>

## 402.81 `CONFIG_NET_PKT_ALLOC_STATS`

**提示（Prompt）**：获取 `net_pkt` 分配统计信息（Allocation statistics）

**说明（Help）**

收集 `net_pkt` 分配统计信息（Allocation statistics），包括成功和失败分配各自的分配次数、平均分配大小，以及以微秒为单位的平均分配时间等。可在网络命令行（net-shell）中通过 `net mem` 命令查看这些额外统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:1023`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L1023)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_PKT_BUF_RX_DATA_POOL_SIZE"></a>

## 402.82 `CONFIG_NET_PKT_BUF_RX_DATA_POOL_SIZE`

**提示（Prompt）**：用于分配缓冲区的接收内存池（RX memory pool）大小

**说明（Help）**

指定接收内存池（RX memory pool）的大小，各接收网络缓冲区从该池分配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_BUF_VARIABLE_DATA_SIZE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4096 if CONFIG_NET_PKT_LARGE_DEFAULTS
2048
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:806`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L806)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_VARIABLE_DATA_SIZE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_BUF_VARIABLE_DATA_SIZE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_LARGE_DEFAULTS`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_LARGE_DEFAULTS)。

<a id="CONFIG_NET_PKT_BUF_TX_DATA_ALLOC_ALIGN_LEN"></a>

## 402.83 `CONFIG_NET_PKT_BUF_TX_DATA_ALLOC_ALIGN_LEN`

**提示（Prompt）**：发送 `net_buf` 分配的对齐量（Alignment）

**说明（Help）**

指定分配用于发送的 `net_buf` 数据时，缓冲区长度的对齐量（Alignment）。默认不要求特殊对齐。例如，Nordic Wi-Fi 芯片使用的 SPI 驱动要求发送数据的长度和起始地址均按 4 字节对齐，因此需要此设置。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_BUF_VARIABLE_DATA_SIZE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 8]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:831`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L831)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_VARIABLE_DATA_SIZE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_BUF_VARIABLE_DATA_SIZE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_PKT_BUF_TX_DATA_POOL_SIZE"></a>

## 402.84 `CONFIG_NET_PKT_BUF_TX_DATA_POOL_SIZE`

**提示（Prompt）**：用于分配缓冲区的发送内存池（TX memory pool）大小

**说明（Help）**

指定发送内存池（TX memory pool）的大小，各发送网络缓冲区从该池分配。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_BUF_VARIABLE_DATA_SIZE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4096 if CONFIG_NET_PKT_LARGE_DEFAULTS
2048
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:815`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L815)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_BUF_VARIABLE_DATA_SIZE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_BUF_VARIABLE_DATA_SIZE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_LARGE_DEFAULTS`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_LARGE_DEFAULTS)。

<a id="CONFIG_NET_PKT_BUF_USER_DATA_SIZE"></a>

## 402.85 `CONFIG_NET_PKT_BUF_USER_DATA_SIZE`

**提示（Prompt）**：收发网络缓冲区中可用的 `user_data` 大小

**说明（Help）**

接收（RX）和发送（TX）网络缓冲区使用的用户数据（User data）大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**取值范围（Ranges）**

```text
[4, 16]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:824`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L824)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_PKT_CONTROL_BLOCK"></a>

## 402.86 `CONFIG_NET_PKT_CONTROL_BLOCK`

**提示（Prompt）**：数据包控制块（Packet control block）

**说明（Help）**

启用可由任意层使用的控制块（Control block）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_DSA_NXP_IMX_NETC
CONFIG_IEEE802154
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:843`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L843)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_DSA_NXP_IMX_NETC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_DSA_NXP_IMX_NETC)、[`CONFIG_IEEE802154`](P109_drivers_ieee802154_配置项参考_1.md#CONFIG_IEEE802154)。

<a id="CONFIG_NET_PKT_CONTROL_BLOCK_SIZE"></a>

## 402.87 `CONFIG_NET_PKT_CONTROL_BLOCK_SIZE`

**提示（Prompt）**：数据包控制块（Packet control block）的大小（字节）

**说明（Help）**

未启用其他特定控制块（Control block）时的数据包控制块大小，单位为字节。如果已启用 `net_pkt_cb_ieee802154` 等特定控制块，则实际数据包控制块大小取它们的最大值。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PKT_CONTROL_BLOCK && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1 if CONFIG_DSA_TAG_PROTOCOL_NETC
1
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:848`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L848)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 数据包控制块（Packet control block）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_CONTROL_BLOCK`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_CONTROL_BLOCK)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_DSA_TAG_PROTOCOL_NETC`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_DSA_TAG_PROTOCOL_NETC)。

<a id="CONFIG_NET_PKT_DATA_ALLOC_TYPE"></a>

## 402.88 `CONFIG_NET_PKT_DATA_ALLOC_TYPE`

**提示（Prompt）**：网络数据包分配器类型（data allocator type）

**说明（Help）**

选择用于保存数据包数据的网络缓冲区的内存分配器（Memory allocator）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_BUF_FIXED_DATA_SIZE
```

**可选项（Choices）**

```text
CONFIG_NET_BUF_FIXED_DATA_SIZE
CONFIG_NET_BUF_VARIABLE_DATA_SIZE
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:778`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L778)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_BUF_FIXED_DATA_SIZE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_BUF_FIXED_DATA_SIZE)、[`CONFIG_NET_BUF_VARIABLE_DATA_SIZE`](P396_subsys_net_配置项参考_6.md#CONFIG_NET_BUF_VARIABLE_DATA_SIZE)。

<a id="CONFIG_NET_PKT_FILTER"></a>

## 402.89 `CONFIG_NET_PKT_FILTER`

**提示（Prompt）**：网络数据包过滤（Network packet filtering）

**说明（Help）**

网络数据包过滤（Network Packet Filtering）功能提供基础设施，用于构建自定义规则，接受或拒绝数据包的发送与接收。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR
CONFIG_NET_IPV4_NAT
```

**定义位置（Location）**：[`subsys/net/pkt_filter/Kconfig:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/pkt_filter/Kconfig#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络数据包过滤（Network Packet Filtering）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR)、[`CONFIG_NET_IPV4_NAT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_NAT)。

<a id="CONFIG_NET_PKT_FILTER_IPV4_HOOK"></a>

## 402.90 `CONFIG_NET_PKT_FILTER_IPV4_HOOK`

**提示（Prompt）**：IPv4 协议栈内的附加网络数据包过滤钩子（Filtering hook）

**说明（Help）**

此附加钩子（Hook）提供基础设施，用于构建针对 IP 数据包的自定义规则。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && CONFIG_NET_PKT_FILTER && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR
CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR
CONFIG_NET_IPV4_NAT
```

**定义位置（Location）**：[`subsys/net/pkt_filter/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/pkt_filter/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络数据包过滤（Network Packet Filtering） → 网络数据包过滤（Network packet filtering）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_PKT_FILTER`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR`](P248_modules_openthread_配置项参考_3.md#CONFIG_OPENTHREAD_ZEPHYR_BORDER_ROUTER_NAT64_TRANSLATOR)、[`CONFIG_NET_IPV4_NAT`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_NAT)。

<a id="CONFIG_NET_PKT_FILTER_IPV6_HOOK"></a>

## 402.91 `CONFIG_NET_PKT_FILTER_IPV6_HOOK`

**提示（Prompt）**：IPv6 协议栈内的附加网络数据包过滤钩子（Filtering hook）

**说明（Help）**

此附加钩子（Hook）提供基础设施，用于构建针对 IP 数据包的自定义规则。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && CONFIG_NET_PKT_FILTER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/pkt_filter/Kconfig:23`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/pkt_filter/Kconfig#L23)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络数据包过滤（Network Packet Filtering） → 网络数据包过滤（Network packet filtering）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_PKT_FILTER`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_PKT_FILTER_LOCAL_IN_HOOK"></a>

## 402.92 `CONFIG_NET_PKT_FILTER_LOCAL_IN_HOOK`

**提示（Prompt）**：连接输入的附加网络数据包过滤钩子（Filtering hook）

**说明（Help）**

此附加钩子（Hook）提供基础设施，用于构建针对 TCP、UDP 等数据包的自定义规则。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IP && CONFIG_NET_PKT_FILTER && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/pkt_filter/Kconfig:30`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/pkt_filter/Kconfig#L30)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络数据包过滤（Network Packet Filtering） → 网络数据包过滤（Network packet filtering）

**配置项引用（Symbol References）**：[`CONFIG_NET_IP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IP)、[`CONFIG_NET_PKT_FILTER`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_IP`。

<a id="CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE"></a>

## 402.93 `CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE`

**提示（Prompt）**：数据包过滤（Packet filtering）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_PKT_FILTER && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_PKT_FILTER_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_PKT_FILTER_LOG_LEVEL_OFF
CONFIG_NET_PKT_FILTER_LOG_LEVEL_ERR
CONFIG_NET_PKT_FILTER_LOG_LEVEL_WRN
CONFIG_NET_PKT_FILTER_LOG_LEVEL_INF
CONFIG_NET_PKT_FILTER_LOG_LEVEL_DBG
CONFIG_NET_PKT_FILTER_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络数据包过滤（Network Packet Filtering） → 网络数据包过滤（Network packet filtering）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_PKT_FILTER`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_FILTER_LOG_LEVEL_DEFAULT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_PKT_FILTER_LOG_LEVEL_OFF`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER_LOG_LEVEL_OFF)、[`CONFIG_NET_PKT_FILTER_LOG_LEVEL_ERR`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER_LOG_LEVEL_ERR)、[`CONFIG_NET_PKT_FILTER_LOG_LEVEL_WRN`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER_LOG_LEVEL_WRN)、[`CONFIG_NET_PKT_FILTER_LOG_LEVEL_INF`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER_LOG_LEVEL_INF)、[`CONFIG_NET_PKT_FILTER_LOG_LEVEL_DBG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_PKT_FILTER_LOG_LEVEL_DBG"></a>

## 402.94 `CONFIG_NET_PKT_FILTER_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络数据包过滤（Network Packet Filtering） → 网络数据包过滤（Network packet filtering） → 数据包过滤（Packet filtering）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_FILTER_LOG_LEVEL_DEFAULT"></a>

## 402.95 `CONFIG_NET_PKT_FILTER_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络数据包过滤（Network Packet Filtering） → 网络数据包过滤（Network packet filtering） → 数据包过滤（Packet filtering）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_FILTER_LOG_LEVEL_ERR"></a>

## 402.96 `CONFIG_NET_PKT_FILTER_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络数据包过滤（Network Packet Filtering） → 网络数据包过滤（Network packet filtering） → 数据包过滤（Packet filtering）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_FILTER_LOG_LEVEL_INF"></a>

## 402.97 `CONFIG_NET_PKT_FILTER_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络数据包过滤（Network Packet Filtering） → 网络数据包过滤（Network packet filtering） → 数据包过滤（Packet filtering）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_FILTER_LOG_LEVEL_OFF"></a>

## 402.98 `CONFIG_NET_PKT_FILTER_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络数据包过滤（Network Packet Filtering） → 网络数据包过滤（Network packet filtering） → 数据包过滤（Packet filtering）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_FILTER_LOG_LEVEL_WRN"></a>

## 402.99 `CONFIG_NET_PKT_FILTER_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络数据包过滤（Network Packet Filtering） → 网络数据包过滤（Network packet filtering） → 数据包过滤（Packet filtering）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_PKT_LARGE_DEFAULTS"></a>

## 402.100 `CONFIG_NET_PKT_LARGE_DEFAULTS`

**提示（Prompt）**：默认提供更多网络数据包（Network packet）资源

**说明（Help）**

为网络数据包池和缓冲区池使用较大的默认值。这些默认值适用于以线速（Line rate）传输完整以太网帧的接口。如果启用以太网第二层（Ethernet L2）仅用于少量流量的用途，例如只执行扫描的 Wi-Fi 驱动，可禁用此项以减少 RAM 占用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_ETH_DRIVER
y if CONFIG_NET_SLIP_TAP
y if CONFIG_WIFI && !CONFIG_WIFI_USAGE_MODE_SCAN_ONLY
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:732`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L732)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)、[`CONFIG_NET_SLIP_TAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SLIP_TAP)、[`CONFIG_WIFI`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI)、[`CONFIG_WIFI_USAGE_MODE_SCAN_ONLY`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_USAGE_MODE_SCAN_ONLY)。

<!-- kconfig-navigation -->

[上一章](P401_subsys_net_配置项参考_11.md) · [返回大纲](大纲.md) · [下一章](P403_subsys_net_配置项参考_13.md)
