---
id: learning.zephyr-docs.kconfig-reference.page-404
title: "`subsys/net`配置项参考（14/19）"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第404章\_`subsys/net`配置项参考（14/19）

本章翻译官方 Kconfig 数据库中 `subsys/net` 的 100 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式和配置标识符保持原样，默认值除有译注明示的构建机路径相对化外保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_SHELL_VLAN_SUPPORTED"></a>

## 404.1 `CONFIG_NET_SHELL_VLAN_SUPPORTED`

**提示（Prompt）**：虚拟局域网（VLAN）配置

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_NET_VLAN) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_NET_VLAN`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_VLAN)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_WEBSOCKET_SUPPORTED"></a>

## 404.2 `CONFIG_NET_SHELL_WEBSOCKET_SUPPORTED`

**提示（Prompt）**：WebSocket 客户端状态（Client status）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_WEBSOCKET_CLIENT) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:207`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L207)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_WEBSOCKET_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CLIENT)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SHELL_WIREGUARD_SUPPORTED"></a>

## 404.3 `CONFIG_NET_SHELL_WIREGUARD_SUPPORTED`

**提示（Prompt）**：WireGuard 虚拟专用网络（VPN）的配置与状态

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS || CONFIG_WIREGUARD_SHELL) && CONFIG_NET_SHELL && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/shell/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/shell/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → 网络命令行工具（Network shell utilities）

**配置项引用（Symbol References）**：[`CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL_SHOW_DISABLED_COMMANDS)、[`CONFIG_WIREGUARD_SHELL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIREGUARD_SHELL)、[`CONFIG_NET_SHELL`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_SHELL)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_WIREGUARD_SHELL`。

<a id="CONFIG_NET_SLIP_TAP"></a>

## 404.4 `CONFIG_NET_SLIP_TAP`

**提示（Prompt）**：TAP SLIP 驱动

**说明（Help）**

使用 QEMU 测试时需要 SLIP TAP 支持。宿主机必须运行支持 TAP 的 `tunslip6`，才能通过 SLIP 驱动通信。更多信息参见 [net-tools 项目](https://github.com/zephyrproject-rtos/net-tools)。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_QEMU_SLIP && CONFIG_NET_NATIVE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y if CONFIG_QEMU_TARGET && !CONFIG_NET_TEST
```

**主动选择（Selects）**

```text
CONFIG_SLIP
CONFIG_UART_PIPE
CONFIG_UART_INTERRUPT_DRIVEN
CONFIG_SLIP_TAP
CONFIG_NET_L2_ETHERNET
```

**弱选择（Implies）**

```text
CONFIG_ETH_DRIVER
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig:709`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig#L709)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_QEMU_SLIP`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_QEMU_SLIP)、[`CONFIG_NET_NATIVE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_NATIVE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QEMU_TARGET`](P041_boards_Kconfig_配置项参考.md#CONFIG_QEMU_TARGET)、[`CONFIG_NET_TEST`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TEST)、[`CONFIG_SLIP`](P131_drivers_net_配置项参考.md#CONFIG_SLIP)、[`CONFIG_UART_PIPE`](P168_drivers_serial_配置项参考_4.md#CONFIG_UART_PIPE)、[`CONFIG_UART_INTERRUPT_DRIVEN`](P167_drivers_serial_配置项参考_3.md#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_SLIP_TAP`](P131_drivers_net_配置项参考.md#CONFIG_SLIP_TAP)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_ETH_DRIVER`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER)。

<a id="CONFIG_NET_SOCKETPAIR"></a>

## 404.5 `CONFIG_NET_SOCKETPAIR`

**提示（Prompt）**：套接字对（socketpair）支持

**说明（Help）**

通过一对已连接、未命名的 UNIX 域套接字（UNIX domain socket）通信。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_POSIX_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:466`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L466)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_POSIX_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_NETWORKING)。

<a id="CONFIG_NET_SOCKETPAIR_ALLOCATION_STRATEGY"></a>

## 404.6 `CONFIG_NET_SOCKETPAIR_ALLOCATION_STRATEGY`

**提示（Prompt）**：套接字对（socketpair）的内存管理（Memory management）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETPAIR && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_SOCKETPAIR_HEAP if CONFIG_KERNEL_MEM_POOL
```

**可选项（Choices）**

```text
CONFIG_NET_SOCKETPAIR_STATIC
CONFIG_NET_SOCKETPAIR_HEAP
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:480`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L480)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 套接字对（socketpair）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETPAIR`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETPAIR)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETPAIR_HEAP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETPAIR_HEAP)、[`CONFIG_KERNEL_MEM_POOL`](P001_kernel_配置项参考_1.md#CONFIG_KERNEL_MEM_POOL)、[`CONFIG_NET_SOCKETPAIR_STATIC`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETPAIR_STATIC)。

<a id="CONFIG_NET_SOCKETPAIR_BUFFER_SIZE"></a>

## 404.7 `CONFIG_NET_SOCKETPAIR_BUFFER_SIZE`

**提示（Prompt）**：中间缓冲区（Intermediate buffer）大小（字节）

**说明（Help）**

`socketpair(2)` 的缓冲区大小（Buffer size）

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETPAIR && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
64
```

**取值范围（Ranges）**

```text
[1, 4096]
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:473`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L473)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 套接字对（socketpair）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETPAIR`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETPAIR)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETPAIR_HEAP"></a>

## 404.8 `CONFIG_NET_SOCKETPAIR_HEAP`

**提示（Prompt）**：使用堆（Heap）分配套接字对（Socket pair）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_SOCKETPAIR_ALLOCATION_STRATEGY>
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:487`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L487)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 套接字对（socketpair）支持 → 套接字对（socketpair）的内存管理（Memory management）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETPAIR_ALLOCATION_STRATEGY`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETPAIR_ALLOCATION_STRATEGY)。

<a id="CONFIG_NET_SOCKETPAIR_MAX"></a>

## 404.9 `CONFIG_NET_SOCKETPAIR_MAX`

**提示（Prompt）**：预分配套接字对（Socket pair）的数量

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETPAIR_STATIC && CONFIG_NET_SOCKETPAIR && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:494`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L494)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 套接字对（socketpair）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETPAIR_STATIC`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETPAIR_STATIC)、[`CONFIG_NET_SOCKETPAIR`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETPAIR)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETPAIR_STATIC"></a>

## 404.10 `CONFIG_NET_SOCKETPAIR_STATIC`

**提示（Prompt）**：静态预分配内存（Static memory pre-allocation）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_SOCKETPAIR_ALLOCATION_STRATEGY>
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:484`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L484)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 套接字对（socketpair）支持 → 套接字对（socketpair）的内存管理（Memory management）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETPAIR_ALLOCATION_STRATEGY`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETPAIR_ALLOCATION_STRATEGY)。

<a id="CONFIG_NET_SOCKETS"></a>

## 404.11 `CONFIG_NET_SOCKETS`

**提示（Prompt）**：BSD 套接字兼容 API（BSD Sockets compatible API）

**说明（Help）**

在 Zephyr 原生网络 API 之上提供类似 BSD 套接字（BSD Sockets）的 API。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_ZVFS
CONFIG_ZVFS_POLL
CONFIG_ZVFS_SELECT
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_SIWX91X_FIRMWARE_UPGRADE_SHELL
CONFIG_WIFI_BFLB
CONFIG_WIFI_ESWIFI
CONFIG_COAP_SERVER
CONFIG_DNS_RESOLVER
CONFIG_MDNS_RESPONDER
CONFIG_LLMNR_RESPONDER
CONFIG_NET_LATMON
CONFIG_MCP_TRANSPORT_HTTP
CONFIG_NETMIDI2_HOST
CONFIG_MQTT_LIB
CONFIG_MQTT_SN_TRANSPORT_UDP
CONFIG_PTP
CONFIG_RTP_TRANSPORT_SOCKET
CONFIG_TFTP_LIB
CONFIG_HTTP_SERVER
CONFIG_WEBSOCKET_CLIENT
CONFIG_LWM2M
CONFIG_QUIC
CONFIG_NET_DHCPV4_SERVER
CONFIG_NET_ZPERF
CONFIG_POSIX_NETWORKING
CONFIG_SHELL_BACKEND_TELNET
CONFIG_SHELL_BACKEND_WEBSOCKET
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_POLL`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_POLL)、[`CONFIG_ZVFS_SELECT`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_SELECT)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_SIWX91X_FIRMWARE_UPGRADE_SHELL`](P308_soc_silabs_配置项参考_1.md#CONFIG_SIWX91X_FIRMWARE_UPGRADE_SHELL)、[`CONFIG_WIFI_BFLB`](P192_drivers_wifi_配置项参考_5.md#CONFIG_WIFI_BFLB)、[`CONFIG_WIFI_ESWIFI`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI)、[`CONFIG_COAP_SERVER`](P391_subsys_net_配置项参考_1.md#CONFIG_COAP_SERVER)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_LLMNR_RESPONDER`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER)、[`CONFIG_NET_LATMON`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_LATMON)、[`CONFIG_MCP_TRANSPORT_HTTP`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_NETMIDI2_HOST`](P395_subsys_net_配置项参考_5.md#CONFIG_NETMIDI2_HOST)、[`CONFIG_MQTT_LIB`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_LIB)、[`CONFIG_MQTT_SN_TRANSPORT_UDP`](P395_subsys_net_配置项参考_5.md#CONFIG_MQTT_SN_TRANSPORT_UDP)、[`CONFIG_PTP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP)、[`CONFIG_RTP_TRANSPORT_SOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP_TRANSPORT_SOCKET)、[`CONFIG_TFTP_LIB`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TFTP_LIB)、[`CONFIG_HTTP_SERVER`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER)、[`CONFIG_WEBSOCKET_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CLIENT)、[`CONFIG_LWM2M`](P392_subsys_net_配置项参考_2.md#CONFIG_LWM2M)、[`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC)、[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NET_ZPERF`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF)、[`CONFIG_POSIX_NETWORKING`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_NETWORKING)、[`CONFIG_SHELL_BACKEND_TELNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_BACKEND_WEBSOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_WEBSOCKET)。

<a id="CONFIG_NET_SOCKETS_CAN"></a>

## 404.12 `CONFIG_NET_SOCKETS_CAN`

**提示（Prompt）**：套接字 CAN（SocketCAN）支持

**说明（Help）**

该值取决于网络需求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_CANBUS_RAW
CONFIG_NET_CONNECTION_SOCKETS
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:451`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L451)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_L2_CANBUS_RAW`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_CANBUS_RAW)、[`CONFIG_NET_CONNECTION_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONNECTION_SOCKETS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_CONNECTION_SOCKETS`。

<a id="CONFIG_NET_SOCKETS_CAN_RECEIVERS"></a>

## 404.13 `CONFIG_NET_SOCKETS_CAN_RECEIVERS`

**提示（Prompt）**：允许同时存在的 SocketCAN 接收者（Receiver）数量

**说明（Help）**

指定多少个套接字（Socket）可以从同一个 SocketCAN 接口接收数据。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_CAN && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:458`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L458)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 套接字 CAN（SocketCAN）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_CAN`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_CAN)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_CONNECT_TIMEOUT"></a>

## 404.14 `CONFIG_NET_SOCKETS_CONNECT_TIMEOUT`

**提示（Prompt）**：连接（CONNECT）的超时时间（毫秒）

**说明（Help）**

指定调用 `connect()` 后，如果尚未收到对端的 SYN-ACK，则经过多少毫秒判定调用超时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
3000
```

**取值范围（Ranges）**

```text
[0, 300000]
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_DNS_BACKOFF_INTERVAL"></a>

## 404.15 `CONFIG_NET_SOCKETS_DNS_BACKOFF_INTERVAL`

**提示（Prompt）**：DNS 超时的退避间隔（Backoff interval）

**说明（Help）**

此变量与 DNS 超时有关。如果 DNS 超时小于此值，则忽略此值；如果超时更大，则本变量指定重新尝试 DNS 查询前的等待时间，单位为毫秒。没有收到响应时，将退避间隔（Backoff interval）翻倍并再次查询。例如，`CONFIG_NET_SOCKETS_DNS_TIMEOUT` 为 17000，即 17 秒，本值为 5000，即 5 秒。如果 5 秒内未收到 DNS 服务器响应，则发起第二次查询，并将等待时间设为 10 秒，即 `5 * 2`。若仍无响应，则从开始起经过 15 秒，即 `5 + 5 * 2`，发起第三次查询，将等待时间设为剩余的 2 秒，以使总超时保持为 17 秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5000
```

**取值范围（Ranges）**

```text
[1000, 300000]
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_DNS_TIMEOUT"></a>

## 404.16 `CONFIG_NET_SOCKETS_DNS_TIMEOUT`

**提示（Prompt）**：DNS 查询超时时间（毫秒）

**说明（Help）**

指定 DNS 查询经过多少毫秒后视为超时。最短超时为 1 秒，最长为 5 分钟。如果此值大于 `CONFIG_NET_SOCKETS_DNS_BACKOFF_INTERVAL`，则采用指数退避（Exponential backoff）多次尝试，直到达到总超时。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_DNS_RESOLVER && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2000
```

**取值范围（Ranges）**

```text
[1000, 300000] if !CONFIG_NET_TEST
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:35`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L35)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_TEST`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_TEST)。

<a id="CONFIG_NET_SOCKETS_DTLS_MAX_FRAGMENT_LENGTH"></a>

## 404.17 `CONFIG_NET_SOCKETS_DTLS_MAX_FRAGMENT_LENGTH`

**提示（Prompt）**：DTLS 最大分片大小（Maximum fragment size，字节）

**说明（Help）**

当 `MBEDTLS_SSL_OUT_CONTENT_LEN` 和 `MBEDTLS_SSL_IN_CONTENT_LEN` 为 TLS 配置为较大值时，本变量指定 DTLS 连接使用的最大分片长度（Maximum Fragment Length，MFL）。DTLS 的 MFL 应保持在网络最大传输单元（MTU）以下，以避免 IP 分片（IP fragmentation）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_ENABLE_DTLS && CONFIG_NET_SOCKETS_TLS_SET_MAX_FRAGMENT_LENGTH && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1024
```

**取值范围（Ranges）**

```text
[512, 4096]
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:202`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L202)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → DTLS 套接字（Socket）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_ENABLE_DTLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_ENABLE_DTLS)、[`CONFIG_NET_SOCKETS_TLS_SET_MAX_FRAGMENT_LENGTH`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_TLS_SET_MAX_FRAGMENT_LENGTH)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_DTLS_SENDMSG_BUF_SIZE"></a>

## 404.18 `CONFIG_NET_SOCKETS_DTLS_SENDMSG_BUF_SIZE`

**提示（Prompt）**：DTLS `sendmsg()` 的中间缓冲区大小（Intermediate buffer size）

**说明（Help）**

设置 DTLS `sendmsg()` 函数的中间缓冲区（Intermediate buffer）大小。数据报（DGRAM）的 `sendmsg()` 应将全部数据发送在一个数据报中，因此必须先将 `msghdr` 结构提供的全部数据整理为连续数据，再传给 mbed TLS，这就需要中间缓冲区。大小可设为 0，此时禁用 DTLS 套接字的数据连续化（Linearization），`sendmsg()` 仅接受恰有一个非空 `iov` 缓冲区的 `msghdr`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_ENABLE_DTLS && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
0
```

**取值范围（Ranges）**

```text
[0, 65535]
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:216`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L216)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → DTLS 套接字（Socket）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_ENABLE_DTLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_ENABLE_DTLS)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_DTLS_TIMEOUT"></a>

## 404.19 `CONFIG_NET_SOCKETS_DTLS_TIMEOUT`

**提示（Prompt）**：DTLS 连接超时时间（毫秒）

**说明（Help）**

指定经过多少毫秒后，TLS 服务器将 DTLS 连接视为失效，并释放 DTLS 资源。此功能用于处理 DTLS 客户端直接关闭、未正常关闭连接的情况，避免遗留连接阻碍其他对端连接。设为 0 表示不超时，仅当对端通过发送 TLS 通知正常关闭连接，或套接字（Socket）关闭时，才释放资源。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_ENABLE_DTLS && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
5000
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:189`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L189)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → DTLS 套接字（Socket）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_ENABLE_DTLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_ENABLE_DTLS)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_ENABLE_DTLS"></a>

## 404.20 `CONFIG_NET_SOCKETS_ENABLE_DTLS`

**提示（Prompt）**：DTLS 套接字（Socket）支持

**说明（Help）**

启用 DTLS 套接字（Socket）支持。默认只支持运行在 TCP 之上的 TLS。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS_SSL_PROTO_TLS1_2 if CONFIG_NET_NATIVE
CONFIG_MBEDTLS_SSL_PROTO_DTLS if CONFIG_NET_NATIVE
```

**被选择（Selected by）**

```text
CONFIG_MCUMGR_TRANSPORT_UDP_DTLS
CONFIG_UPDATEHUB_DTLS
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:181`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L181)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MBEDTLS_SSL_PROTO_TLS1_2`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_TLS1_2)、[`CONFIG_NET_NATIVE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_NATIVE)、[`CONFIG_MBEDTLS_SSL_PROTO_DTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_PROTO_DTLS)、[`CONFIG_MCUMGR_TRANSPORT_UDP_DTLS`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP_DTLS)、[`CONFIG_UPDATEHUB_DTLS`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB_DTLS)。

<a id="CONFIG_NET_SOCKETS_INET_RAW"></a>

## 404.21 `CONFIG_NET_SOCKETS_INET_RAW`

**提示（Prompt）**：`AF_INET`/`AF_INET6` 与 `SOCK_RAW` 套接字支持

**说明（Help）**

为 `AF_INET`/`AF_INET6` 套接字启用 `SOCK_RAW` 类型支持，可在后续处理发生之前接收原始 IP 数据报（Raw IP datagram）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_IP && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:444`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L444)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_IP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE_IP)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_NATIVE_IP`。

<a id="CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE"></a>

## 404.22 `CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：BSD 套接字兼容 API 调用日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_SOCKETS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_SOCKETS_LOG_LEVEL_OFF
CONFIG_NET_SOCKETS_LOG_LEVEL_ERR
CONFIG_NET_SOCKETS_LOG_LEVEL_WRN
CONFIG_NET_SOCKETS_LOG_LEVEL_INF
CONFIG_NET_SOCKETS_LOG_LEVEL_DBG
CONFIG_NET_SOCKETS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS_LOG_LEVEL_DEFAULT`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_SOCKETS_LOG_LEVEL_OFF`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_LOG_LEVEL_OFF)、[`CONFIG_NET_SOCKETS_LOG_LEVEL_ERR`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_LOG_LEVEL_ERR)、[`CONFIG_NET_SOCKETS_LOG_LEVEL_WRN`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_LOG_LEVEL_WRN)、[`CONFIG_NET_SOCKETS_LOG_LEVEL_INF`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_LOG_LEVEL_INF)、[`CONFIG_NET_SOCKETS_LOG_LEVEL_DBG`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_SOCKETS_LOG_LEVEL_DBG"></a>

## 404.23 `CONFIG_NET_SOCKETS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → BSD 套接字兼容 API 调用日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_SOCKETS_LOG_LEVEL_DEFAULT"></a>

## 404.24 `CONFIG_NET_SOCKETS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → BSD 套接字兼容 API 调用日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_SOCKETS_LOG_LEVEL_ERR"></a>

## 404.25 `CONFIG_NET_SOCKETS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → BSD 套接字兼容 API 调用日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_SOCKETS_LOG_LEVEL_INF"></a>

## 404.26 `CONFIG_NET_SOCKETS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → BSD 套接字兼容 API 调用日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_SOCKETS_LOG_LEVEL_OFF"></a>

## 404.27 `CONFIG_NET_SOCKETS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → BSD 套接字兼容 API 调用日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_SOCKETS_LOG_LEVEL_WRN"></a>

## 404.28 `CONFIG_NET_SOCKETS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → BSD 套接字兼容 API 调用日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_SOCKETS_NET_MGMT"></a>

## 404.29 `CONFIG_NET_SOCKETS_NET_MGMT`

**提示（Prompt）**：网络管理套接字（Network management socket）支持［实验性，Experimental］

**说明（Help）**

若希望通过套接字 API（Socket API）让应用接收网络管理事件，请选中此项。注意，使用 `net_mgmt` 套接字的线程，其优先级应至少等于处理网络事件的线程，参见 `CONFIG_NET_MGMT_EVENT_WORKER`；否则，突发事件到来时可能丢失部分事件。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_MGMT_EVENT && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT_EVENT_INFO
CONFIG_EXPERIMENTAL
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:510`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L510)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_MGMT_EVENT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT_EVENT_INFO`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT_EVENT_INFO)、[`CONFIG_EXPERIMENTAL`](P003_Kconfig.zephyr_配置项参考_1.md#CONFIG_EXPERIMENTAL)。

<a id="CONFIG_NET_SOCKETS_NET_MGMT_MAX_LISTENERS"></a>

## 404.30 `CONFIG_NET_SOCKETS_NET_MGMT_MAX_LISTENERS`

**提示（Prompt）**：可监听的套接字（Socket）最大数量

**说明（Help）**

设置可通过套接字接口配置的 `net_mgmt` 套接字最大数量。例如，使用两个独立套接字监听事件时，应将此值设为 2。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_NET_MGMT && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:523`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L523)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 网络管理套接字（Network management socket）支持［实验性，Experimental］

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_NET_MGMT`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_NET_MGMT)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_OBJ_CORE"></a>

## 404.31 `CONFIG_NET_SOCKETS_OBJ_CORE`

**提示（Prompt）**：对象核心（Object core）的套接字支持

**说明（Help）**

若希望将对象核心（Object core）与套接字 API 结合，通过对象核心获取网络套接字信息和统计信息，请选中此项。网络命令行（net-shell）的 `net sockets` 命令将用它显示套接字信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_OBJ_CORE && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_OBJ_CORE_STATS
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:539`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L539)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_OBJ_CORE`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_OBJ_CORE_STATS`](P001_kernel_配置项参考_1.md#CONFIG_OBJ_CORE_STATS)。

<a id="CONFIG_NET_SOCKETS_OFFLOAD"></a>

## 404.32 `CONFIG_NET_SOCKETS_OFFLOAD`

**提示（Prompt）**：卸载套接字 API（Offload Socket APIs）

**说明（Help）**

允许将套接字操作直接卸载到专用 TCP/IP 硬件。在系统只需一个网络接口时，此功能通过绕过 Zephyr TCP/IP 协议栈节省资源，并提供完整的 BSD 套接字卸载（Socket offload）能力。因此，它也绕过 Zephyr 可能在多个网络接口之间提供的 IP 路由。若需要更深入的集成方式，参见 `NET_OFFLOAD`，它在 Zephyr IP 协议栈内部从 `net_context()` API 层进行卸载。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_ETH_CH9120
CONFIG_MODEM_QUECTEL_BG9X
CONFIG_MODEM_SIM7080
CONFIG_MODEM_ST87MXX
CONFIG_MODEM_UBLOX_SARA
```

**被弱选择（Implied by）**

```text
CONFIG_WIFI_ESWIFI
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:321`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L321)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_ETH_CH9120`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_CH9120)、[`CONFIG_MODEM_QUECTEL_BG9X`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_QUECTEL_BG9X)、[`CONFIG_MODEM_SIM7080`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_SIM7080)、[`CONFIG_MODEM_ST87MXX`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_ST87MXX)、[`CONFIG_MODEM_UBLOX_SARA`](P128_drivers_modem_配置项参考_4.md#CONFIG_MODEM_UBLOX_SARA)、[`CONFIG_WIFI_ESWIFI`](P193_drivers_wifi_配置项参考_6.md#CONFIG_WIFI_ESWIFI)。

<a id="CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER"></a>

## 404.33 `CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER`

**提示（Prompt）**：套接字卸载中间层（Intermediate socket offloading layer）

**说明（Help）**

启用后，包含称为套接字分派器（Socket dispatcher）的卸载中间层，允许通过 `SO_BINDTODEVICE` 套接字选项选择卸载网络接口，进而选择套接字实现。系统中有多个卸载式套接字实现时，此功能可方便地将套接字绑定到特定实现。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_OFFLOAD && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:345`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L345)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_OFFLOAD`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_OFFLOAD)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER_CONTEXT_MAX"></a>

## 404.34 `CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER_CONTEXT_MAX`

**提示（Prompt）**：可创建的分派器套接字（Dispatcher socket）最大数量

**说明（Help）**

可同时创建的分派器套接字（Dispatcher socket）最大数量。注意，只有尚未完成分派的套接字计入此限制。当给定文件描述符（File descriptor）对应的实际套接字创建完成后，分派器上下文会释放，可供复用。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:356`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L356)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 套接字卸载中间层（Intermediate socket offloading layer）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_OFFLOAD_DISPATCHER)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING"></a>

## 404.35 `CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING`

**提示（Prompt）**：无提示（No Prompt），不可直接由用户赋值。

**说明（Help）**

记录每个卸载式套接字（Offloaded socket）绑定的本地端口，让套接字层的端口占用检查将其报告为已使用。卸载式套接字在 `net_context` 层之外执行绑定；若没有此功能，通过此类套接字绑定的端口看起来仍是空闲的。此项由需要该检查的子系统选择，不应手动设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_OFFLOAD && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_DNS_SD
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:366`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L366)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_OFFLOAD`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_OFFLOAD)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_DNS_SD`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_SD)。

<a id="CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING_COUNT"></a>

## 404.36 `CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING_COUNT`

**提示（Prompt）**：可跟踪的已绑定卸载式套接字（Offloaded bound socket）最大数量

**说明（Help）**

为套接字层的端口占用检查，同时跟踪其已绑定本地端口的卸载式套接字数量。卸载式套接字绑定本地端口时占用一个槽位，关闭时释放；原生套接字以及从未绑定的套接字不占槽位。如果同时绑定的卸载式套接字数量超过默认容量，应增大此值，否则可能漏记一次绑定，将已占用端口误报为空闲。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
8 if CONFIG_NET_IPV4 && CONFIG_NET_IPV6
4
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:376`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L376)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_OFFLOAD_PORT_TRACKING)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)。

<a id="CONFIG_NET_SOCKETS_OFFLOAD_PRIORITY"></a>

## 404.37 `CONFIG_NET_SOCKETS_OFFLOAD_PRIORITY`

**提示（Prompt）**：卸载式套接字（Offloaded socket）的默认处理优先级

**说明（Help）**

卸载式套接字（Offloaded socket）的处理优先级。如果启用了原生 TLS，数值小于 `NET_SOCKETS_TLS_PRIORITY` 表示 TLS 也会被卸载，前提是卸载式套接字实现支持；数值大于 `NET_SOCKETS_TLS_PRIORITY` 则表示使用原生 TLS。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
40
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:334`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L334)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_PACKET"></a>

## 404.38 `CONFIG_NET_SOCKETS_PACKET`

**提示（Prompt）**：数据包套接字（Packet socket）支持

**说明（Help）**

这是数据包套接字（Packet socket）支持的初始版本，属于特殊的原始套接字（Raw socket）。数据包与设备驱动之间传递时不会修改报头。发送时，API 调用者负责提供第二层、第三层（L2、L3）等全部报头。接收时，驱动提供的数据包连同全部报头原样交给套接字。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_CONNECTION_SOCKETS
```

**被选择（Selected by）**

```text
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_WIFI_NM_WPA_SUPPLICANT
CONFIG_PTP_IEEE_802_3_PROTOCOL
CONFIG_POSIX_RAW_SOCKETS
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:389`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L389)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_NATIVE)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_CONNECTION_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CONNECTION_SOCKETS)、[`CONFIG_WIFI_NM_WPA_SUPPLICANT`](P235_modules_hostap_配置项参考.md#CONFIG_WIFI_NM_WPA_SUPPLICANT)、[`CONFIG_PTP_IEEE_802_3_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_IEEE_802_3_PROTOCOL)、[`CONFIG_POSIX_RAW_SOCKETS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_POSIX_RAW_SOCKETS)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_CONNECTION_SOCKETS`。

<a id="CONFIG_NET_SOCKETS_PACKET_DGRAM"></a>

## 404.39 `CONFIG_NET_SOCKETS_PACKET_DGRAM`

**提示（Prompt）**：数据包套接字（Packet socket）的 `SOCK_DGRAM` 支持

**说明（Help）**

对于 `AF_PACKET` 地址族的 `SOCK_DGRAM` 套接字，数据包交给用户前会移除第二层（L2）报头。通过此类套接字发送的数据包，在入队前会根据目的地址 `net_sockaddr_ll` 中的信息补上合适的 L2 报头。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_PACKET && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:401`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L401)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 数据包套接字（Packet socket）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_PACKET`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_PACKET)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP"></a>

## 404.40 `CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP`

**提示（Prompt）**：数据包套接字多播成员关系（Packet socket multicast membership）支持

**说明（Help）**

为 `AF_PACKET` 套接字添加 `ZSOCK_PACKET_ADD_MEMBERSHIP` 和 `ZSOCK_PACKET_DROP_MEMBERSHIP` 选项支持。这些选项工作在第二层（L2），告知网卡（NIC）的接收过滤器应放行哪些链路层多播地址。目前只有以太网链路层支持此功能；其他链路层也具备支持后，即可放宽对以太网的依赖。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_PACKET && CONFIG_NET_L2_ETHERNET && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_PTP_IEEE_802_3_PROTOCOL
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:412`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L412)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 数据包套接字（Packet socket）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_PACKET`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_PACKET)、[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_PTP_IEEE_802_3_PROTOCOL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PTP_IEEE_802_3_PROTOCOL)。

<a id="CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP_COUNT"></a>

## 404.41 `CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP_COUNT`

**提示（Prompt）**：数据包套接字多播组成员关系（Multicast group membership）的数量

**说明（Help）**

可同时生效的第二层多播组成员关系（L2 multicast group membership）的最大数量。套接字针对尚未加入的组成功执行一次 `ZSOCK_PACKET_ADD_MEMBERSHIP`，就占用一个表项；通过 `ZSOCK_PACKET_DROP_MEMBERSHIP` 或关闭套接字释放。两个不同套接字加入同一组时，占用两个表项。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2
```

**取值范围（Ranges）**

```text
[1, 255]
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:422`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L422)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 数据包套接字（Packet socket）支持 → 数据包套接字多播成员关系（Packet socket multicast membership）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_PACKET_MCAST_MEMBERSHIP)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_PRIORITY_DEFAULT"></a>

## 404.42 `CONFIG_NET_SOCKETS_PRIORITY_DEFAULT`

**提示（Prompt）**：套接字（Socket）的默认处理优先级

**说明（Help）**

套接字实现的默认处理优先级，决定创建新套接字时尝试各个实现的顺序。数值越小越早处理。例如，可使创建时优先考虑卸载式套接字（Offloaded socket），再考虑原生实现，或反过来。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
50
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_SERVICE"></a>

## 404.43 `CONFIG_NET_SOCKETS_SERVICE`

**提示（Prompt）**：套接字服务（Socket service）支持

**说明（Help）**

套接字服务（Socket service）可以监测多个套接字，只使用一个线程监听数据，从而节省内存。受监测的套接字收到数据时，调用用户提供的工作处理。注意，必须将 `CONFIG_ZVFS_POLL_MAX` 设得足够大，以容纳要服务的套接字表项。具体值取决于系统需求，因为不同网络配置可能同时激活多个服务。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_ZVFS
CONFIG_ZVFS_EVENTFD
```

**被选择（Selected by）**

```text
CONFIG_DNS_RESOLVER
CONFIG_MDNS_RESPONDER
CONFIG_LLMNR_RESPONDER
CONFIG_DNS_SOCKET_DISPATCHER
CONFIG_NETMIDI2_HOST
CONFIG_RTP_TRANSPORT_SOCKET
CONFIG_SNTP_SERVER
CONFIG_QUIC
CONFIG_NET_DHCPV4_SERVER
CONFIG_NET_ZPERF_SERVER
CONFIG_SHELL_BACKEND_TELNET
CONFIG_SHELL_BACKEND_WEBSOCKET
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:79`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L79)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_ZVFS`](P199_lib_配置项参考_3.md#CONFIG_ZVFS)、[`CONFIG_ZVFS_EVENTFD`](P199_lib_配置项参考_3.md#CONFIG_ZVFS_EVENTFD)、[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_LLMNR_RESPONDER`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER)、[`CONFIG_DNS_SOCKET_DISPATCHER`](P392_subsys_net_配置项参考_2.md#CONFIG_DNS_SOCKET_DISPATCHER)、[`CONFIG_NETMIDI2_HOST`](P395_subsys_net_配置项参考_5.md#CONFIG_NETMIDI2_HOST)、[`CONFIG_RTP_TRANSPORT_SOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_RTP_TRANSPORT_SOCKET)、[`CONFIG_SNTP_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SNTP_SERVER)、[`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC)、[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NET_ZPERF_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_SERVER)、[`CONFIG_SHELL_BACKEND_TELNET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_TELNET)、[`CONFIG_SHELL_BACKEND_WEBSOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SHELL_BACKEND_WEBSOCKET)。

<a id="CONFIG_NET_SOCKETS_SERVICE_STACK_SIZE"></a>

## 404.44 `CONFIG_NET_SOCKETS_SERVICE_STACK_SIZE`

**提示（Prompt）**：处理套接字服务的线程栈大小（Thread stack size）

**说明（Help）**

设置轮询套接字（Poll sockets）的线程所用内部栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SERVICE && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
2400 if CONFIG_QUIC
2400 if CONFIG_NET_DHCPV4_SERVER
2048 if CONFIG_NET_ZPERF_IPERF3 && CONFIG_NET_ZPERF_SERVER
1536 if CONFIG_MDNS_RESPONDER
1200
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:121`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L121)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SERVICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SERVICE)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC)、[`CONFIG_NET_DHCPV4_SERVER`](P397_subsys_net_配置项参考_7.md#CONFIG_NET_DHCPV4_SERVER)、[`CONFIG_NET_ZPERF_IPERF3`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_ZPERF_IPERF3)、[`CONFIG_NET_ZPERF_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ZPERF_SERVER)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)。

<a id="CONFIG_NET_SOCKETS_SERVICE_THREAD_PRIO"></a>

## 404.45 `CONFIG_NET_SOCKETS_SERVICE_THREAD_PRIO`

**提示（Prompt）**：套接字服务分派线程（Dispatcher thread）的优先级

**说明（Help）**

设置套接字服务分派线程（Dispatcher thread）的优先级。此处理程序轮询套接字，并直接调用用户提供的回调。数值大于或等于 0 表示抢占式线程（Preemptive thread）优先级；原文给出的最低抢占式优先级数值为 `NUM_PREEMPT_PRIORITIES`，最高为 0。最低协作式线程（Cooperative thread）优先级为 -1，最高为 `-NUM_COOP_PRIORITIES`。

译注：这里保留原文的 `NUM_PREEMPT_PRIORITIES`；它与其他配置帮助中使用 `NUM_PREEMPT_PRIORITIES-1` 的边界写法不同，未擅自统一。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SERVICE && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NUM_PREEMPT_PRIORITIES
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SERVICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SERVICE)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NUM_PREEMPT_PRIORITIES`](P001_kernel_配置项参考_1.md#CONFIG_NUM_PREEMPT_PRIORITIES)。

<a id="CONFIG_NET_SOCKETS_SOCKOPT_TLS"></a>

## 404.46 `CONFIG_NET_SOCKETS_SOCKOPT_TLS`

**提示（Prompt）**：TCP TLS 套接字选项（Socket option）支持

**说明（Help）**

启用 TLS 套接字选项（Socket option）支持，以自动建立到远程主机的 TLS 连接。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_MBEDTLS if CONFIG_NET_NATIVE
CONFIG_PSA_CRYPTO if CONFIG_NET_NATIVE
```

**被选择（Selected by）**

```text
CONFIG_MCUMGR_TRANSPORT_UDP_DTLS
CONFIG_UPDATEHUB_DTLS
CONFIG_HTTP_SERVER_VERSION_3
```

**弱选择（Implies）**

```text
CONFIG_TLS_CREDENTIALS
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:132`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L132)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MBEDTLS`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS)、[`CONFIG_NET_NATIVE`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_NATIVE)、[`CONFIG_PSA_CRYPTO`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_CRYPTO)、[`CONFIG_MCUMGR_TRANSPORT_UDP_DTLS`](P386_subsys_mgmt_配置项参考_3.md#CONFIG_MCUMGR_TRANSPORT_UDP_DTLS)、[`CONFIG_UPDATEHUB_DTLS`](P387_subsys_mgmt_配置项参考_4.md#CONFIG_UPDATEHUB_DTLS)、[`CONFIG_HTTP_SERVER_VERSION_3`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_3)、[`CONFIG_TLS_CREDENTIALS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_TLS_CREDENTIALS)。

<a id="CONFIG_NET_SOCKETS_TLS_CERT_VERIFY_CALLBACK"></a>

## 404.47 `CONFIG_NET_SOCKETS_TLS_CERT_VERIFY_CALLBACK`

**提示（Prompt）**：TLS 证书校验回调（Certificate verification callback）支持

**说明（Help）**

控制是否提供 `TLS_CERT_VERIFY_CALLBACK` TLS 套接字选项。该选项允许注册证书校验回调（Certificate verification callback），由 TLS 后端在 TLS 握手（Handshake）期间调用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:313`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L313)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_TLS_CONNECT_TIMEOUT"></a>

## 404.48 `CONFIG_NET_SOCKETS_TLS_CONNECT_TIMEOUT`

**提示（Prompt）**：TLS 握手超时时间（Handshake timeout，毫秒）

**说明（Help）**

指定安全套接字（Secure socket）上的 TLS 握手在报告超时前最多可持续多少毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10000
```

**取值范围（Ranges）**

```text
[0, 300000]
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:141`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L141)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → TCP TLS 套接字选项（Socket option）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_TLS_MAX_APP_PROTOCOLS"></a>

## 404.49 `CONFIG_NET_SOCKETS_TLS_MAX_APP_PROTOCOLS`

**提示（Prompt）**：支持的应用层协议（Application-layer protocol）最大数量

**说明（Help）**

设置可通过套接字选项显式指定的、TLS/DTLS 之上支持的应用层协议（Application-layer protocol）最大数量。默认不设置受支持的应用层协议。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_MBEDTLS_SSL_ALPN && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4 if CONFIG_HTTP_SERVER_VERSION_1 && CONFIG_HTTP_SERVER_VERSION_2 && CONFIG_HTTP_SERVER_VERSION_3
3 if !CONFIG_HTTP_SERVER_VERSION_1 && CONFIG_HTTP_SERVER_VERSION_2 && CONFIG_HTTP_SERVER_VERSION_3
3 if CONFIG_HTTP_SERVER_VERSION_1 && !CONFIG_HTTP_SERVER_VERSION_2 && CONFIG_HTTP_SERVER_VERSION_3
3 if CONFIG_HTTP_SERVER_VERSION_1 && CONFIG_HTTP_SERVER_VERSION_2 && !CONFIG_HTTP_SERVER_VERSION_3
2
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:272`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L272)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_MBEDTLS_SSL_ALPN`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_ALPN)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_HTTP_SERVER_VERSION_1`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_1)、[`CONFIG_HTTP_SERVER_VERSION_2`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_2)、[`CONFIG_HTTP_SERVER_VERSION_3`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_3)。

<a id="CONFIG_NET_SOCKETS_TLS_MAX_CIPHERSUITES"></a>

## 404.50 `CONFIG_NET_SOCKETS_TLS_MAX_CIPHERSUITES`

**提示（Prompt）**：每个套接字的 TLS/DTLS 密码套件（Cipher suite）最大数量

**说明（Help）**

设置通过套接字选项显式指定时，某个套接字可使用的 TLS/DTLS 密码套件（Cipher suite）最大数量。默认情况下，套接字可使用系统中全部可用的密码套件。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:262`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L262)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_TLS_MAX_CLIENT_SESSION_COUNT"></a>

## 404.51 `CONFIG_NET_SOCKETS_TLS_MAX_CLIENT_SESSION_COUNT`

**提示（Prompt）**：可存储的客户端 TLS/DTLS 会话（Session）最大数量

**说明（Help）**

指定可存储的 TLS/DTLS 会话（Session）最大数量，用于 TLS/DTLS 会话恢复（Session resumption）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:285`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L285)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_TLS_MAX_CONTEXTS"></a>

## 404.52 `CONFIG_NET_SOCKETS_TLS_MAX_CONTEXTS`

**提示（Prompt）**：TLS/DTLS 上下文（Context）的最大数量

**说明（Help）**

指定可同时分配的 TLS/DTLS 上下文（Context）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
1
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:230`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L230)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_TLS_MAX_CREDENTIALS"></a>

## 404.53 `CONFIG_NET_SOCKETS_TLS_MAX_CREDENTIALS`

**提示（Prompt）**：每个套接字的 TLS/DTLS 凭据（Credential）最大数量

**说明（Help）**

设置某个套接字可使用的 TLS/DTLS 凭据（Credential）的最大数量。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
4
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:254`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L254)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_TLS_MAX_SESSION_CONTEXTS"></a>

## 404.54 `CONFIG_NET_SOCKETS_TLS_MAX_SESSION_CONTEXTS`

**提示（Prompt）**：TLS/DTLS 会话（Session）的最大数量

**说明（Help）**

指定可同时建立的 TLS/DTLS 会话（Session）的最大数量。通常一个 TLS 上下文需要一个会话；DTLS 服务器套接字可能每个套接字使用多个会话，以同时与多个客户端通信。此值不应小于 `NET_SOCKETS_TLS_MAX_CONTEXTS`。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_SOCKETS_TLS_MAX_CONTEXTS
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:243`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L243)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_SOCKETS_TLS_MAX_CONTEXTS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_TLS_MAX_CONTEXTS)。

<a id="CONFIG_NET_SOCKETS_TLS_PRIORITY"></a>

## 404.55 `CONFIG_NET_SOCKETS_TLS_PRIORITY`

**提示（Prompt）**：TLS 套接字（Socket）的默认处理优先级

**说明（Help）**

TLS 套接字的处理优先级数值应小于 `NET_SOCKETS_PRIORITY_DEFAULT`，以确保正确的处理顺序。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
45
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:150`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L150)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_TLS_SESSION_CACHE_PERSISTENT"></a>

## 404.56 `CONFIG_NET_SOCKETS_TLS_SESSION_CACHE_PERSISTENT`

**提示（Prompt）**：跨重启持久保存 TLS 会话缓存（Persistent session cache）

**说明（Help）**

使用设置子系统（Settings subsystem）持久存储 TLS/DTLS 客户端会话。启用后，每次 TLS 握手成功都会保存会话，并在系统初始化时恢复，从而允许设备重启后恢复会话（Session resumption）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_SOCKOPT_TLS && CONFIG_SETTINGS && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:293`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L293)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_SOCKOPT_TLS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_SOCKOPT_TLS)、[`CONFIG_SETTINGS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_SETTINGS)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_TLS_SESSION_CACHE_PERSISTENT_PREFIX"></a>

## 404.57 `CONFIG_NET_SOCKETS_TLS_SESSION_CACHE_PERSISTENT_PREFIX`

**提示（Prompt）**：持久 TLS 会话缓存前缀（Persistent session cache prefix）

**说明（Help）**

持久 TLS 会话缓存表项使用的设置键前缀（Settings key prefix）。如果默认前缀与应用中的其他设置键冲突，请修改此值。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_TLS_SESSION_CACHE_PERSISTENT && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
"tls_cache"
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:304`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L304)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API） → 跨重启持久保存 TLS 会话缓存（Persistent session cache）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_TLS_SESSION_CACHE_PERSISTENT`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_TLS_SESSION_CACHE_PERSISTENT)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKETS_TLS_SET_MAX_FRAGMENT_LENGTH"></a>

## 404.58 `CONFIG_NET_SOCKETS_TLS_SET_MAX_FRAGMENT_LENGTH`

**提示（Prompt）**：设置最大分片长度（Maximum Fragment Length，MFL）

**说明（Help）**

对已创建 TLS 上下文的配置调用 `mbedtls_ssl_conf_max_frag_len()`，通过 RFC 6066 的 `max_fragment_length` 扩展向对端发送最大分片长度（Maximum Fragment Length，MFL）。默认根据 mbed TLS 宏 `MBEDTLS_SSL_OUT_CONTENT_LEN` 和 `MBEDTLS_SSL_IN_CONTENT_LEN` 自动选择 MFL；使用默认 mbed TLS 配置时，这两个宏由 `CONFIG_MBEDTLS_SSL_IN_CONTENT_LEN` 和 `CONFIG_MBEDTLS_SSL_OUT_CONTENT_LEN` 配置。即便缓冲区已达到 TLS 的最大值 16384 字节，也仍会推导并通告 MFL，不因达到上限而例外。可通过 `TLS_MAX_FRAGMENT_LENGTH` 套接字选项逐个套接字覆盖此值。对于 DTLS，MFL 还可能受 `NET_SOCKETS_DTLS_MAX_FRAGMENT_LENGTH` 进一步限制。此功能主要用于 TLS 客户端告知 TLS 服务器自身支持的最大接收记录长度（Receive record length）。禁用本选项会关闭全部 MFL 处理，包括自动推导和通过 `TLS_MAX_FRAGMENT_LENGTH` 逐套接字覆盖的功能。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_MBEDTLS_SSL_MAX_FRAGMENT_LENGTH && CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:157`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L157)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_MBEDTLS_SSL_MAX_FRAGMENT_LENGTH`](P241_modules_mbedtls_配置项参考_1.md#CONFIG_MBEDTLS_SSL_MAX_FRAGMENT_LENGTH)、[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_SOCKET_MAX_SEND_WAIT"></a>

## 404.59 `CONFIG_NET_SOCKET_MAX_SEND_WAIT`

**提示（Prompt）**：等待发送命令（Send command）的最长时间（毫秒）

**说明（Help）**

套接字等待受阻连接（Blocked connection）的最长时间，超过后返回 `ENOBUFS` 错误。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
10000
```

**定义位置（Location）**：[`subsys/net/lib/sockets/Kconfig:72`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/sockets/Kconfig#L72)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → 网络库（Network Libraries） → BSD 套接字兼容 API（BSD Sockets compatible API）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS"></a>

## 404.60 `CONFIG_NET_STATISTICS`

**提示（Prompt）**：网络统计（Network statistics）

**说明（Help）**

管理统计计数（Statistics accounting）。此功能占用内存；不确定是否需要时选择 `n`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_NET_PKT_RXTIME_STATS
CONFIG_NET_PKT_TXTIME_STATS
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:6`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L6)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_PKT_RXTIME_STATS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_RXTIME_STATS)、[`CONFIG_NET_PKT_TXTIME_STATS`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_PKT_TXTIME_STATS)。

<a id="CONFIG_NET_STATISTICS_DNS"></a>

## 404.61 `CONFIG_NET_STATISTICS_DNS`

**提示（Prompt）**：域名服务（Domain Name Service，DNS）统计

**说明（Help）**

跟踪 DNS 相关统计信息（Statistics）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_DNS_RESOLVER || CONFIG_MDNS_RESPONDER || CONFIG_LLMNR_RESPONDER) && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:117`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L117)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_DNS_RESOLVER`](P391_subsys_net_配置项参考_1.md#CONFIG_DNS_RESOLVER)、[`CONFIG_MDNS_RESPONDER`](P395_subsys_net_配置项参考_5.md#CONFIG_MDNS_RESPONDER)、[`CONFIG_LLMNR_RESPONDER`](P392_subsys_net_配置项参考_2.md#CONFIG_LLMNR_RESPONDER)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_ETHERNET"></a>

## 404.62 `CONFIG_NET_STATISTICS_ETHERNET`

**提示（Prompt）**：以太网统计（Ethernet statistics）

**说明（Help）**

跟踪以太网相关统计信息（Statistics）。注意，此功能要求以太网驱动支持，并由驱动负责收集统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_L2_ETHERNET || CONFIG_ETH_DRIVER_RAW_MODE) && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:138`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L138)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_ETHERNET`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_L2_ETHERNET)、[`CONFIG_ETH_DRIVER_RAW_MODE`](P087_drivers_ethernet_配置项参考_1.md#CONFIG_ETH_DRIVER_RAW_MODE)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_ETHERNET_VENDOR"></a>

## 404.63 `CONFIG_NET_STATISTICS_ETHERNET_VENDOR`

**提示（Prompt）**：供应商专用以太网统计（Vendor-specific Ethernet statistics）

**说明（Help）**

允许以太网驱动以键值对（Key-value pair）的形式，提供供应商专用硬件寄存器中的统计信息。理解这些信息可能需要查阅供应商文档。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_STATISTICS_ETHERNET && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics） → 以太网统计（Ethernet statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_STATISTICS_ETHERNET`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_ETHERNET)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_ICMP"></a>

## 404.64 `CONFIG_NET_STATISTICS_ICMP`

**提示（Prompt）**：互联网控制消息协议（ICMP）统计

**说明（Help）**

根据启用 IPv4、IPv6 或两者的情况，跟踪相应的 ICMPv4/ICMPv6 统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
(CONFIG_NET_IPV6 || CONFIG_NET_IPV4) && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_IGMP"></a>

## 404.65 `CONFIG_NET_STATISTICS_IGMP`

**提示（Prompt）**：互联网组管理协议（IGMP）统计

**说明（Help）**

跟踪互联网组管理协议（IGMP）相关统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_IGMP && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:110`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L110)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_IGMP`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_IGMP)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_IPV4"></a>

## 404.66 `CONFIG_NET_STATISTICS_IPV4`

**提示（Prompt）**：IPv4 统计（Statistics）

**说明（Help）**

跟踪 IPv4 相关统计信息（Statistics）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4 && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:39`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L39)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_IPV4_PMTU"></a>

## 404.67 `CONFIG_NET_STATISTICS_IPV4_PMTU`

**提示（Prompt）**：IPv4 路径 MTU（PMTU）统计

**说明（Help）**

跟踪 IPv4 路径 MTU 发现（Path MTU Discovery）相关统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV4_PMTU && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:67`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L67)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV4_PMTU`](P399_subsys_net_配置项参考_9.md#CONFIG_NET_IPV4_PMTU)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_IPV6"></a>

## 404.68 `CONFIG_NET_STATISTICS_IPV6`

**提示（Prompt）**：IPv6 统计（Statistics）

**说明（Help）**

跟踪 IPv6 相关统计信息（Statistics）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6 && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:46`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L46)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_IPV6_ND"></a>

## 404.69 `CONFIG_NET_STATISTICS_IPV6_ND`

**提示（Prompt）**：IPv6 统计（Statistics）

**说明（Help）**

跟踪 IPv6 邻居发现（Neighbor Discovery）相关统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ND && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:53`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L53)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_IPV6_PMTU"></a>

## 404.70 `CONFIG_NET_STATISTICS_IPV6_PMTU`

**提示（Prompt）**：IPv6 路径 MTU（PMTU）统计

**说明（Help）**

跟踪 IPv6 路径 MTU 发现（Path MTU Discovery）相关统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_PMTU && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_PMTU`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_PMTU)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE"></a>

## 404.71 `CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE`

**提示（Prompt）**：网络统计（Network statistics）日志级别（Log level）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
CONFIG_NET_STATISTICS_LOG_LEVEL_DEFAULT
```

**可选项（Choices）**

```text
CONFIG_NET_STATISTICS_LOG_LEVEL_OFF
CONFIG_NET_STATISTICS_LOG_LEVEL_ERR
CONFIG_NET_STATISTICS_LOG_LEVEL_WRN
CONFIG_NET_STATISTICS_LOG_LEVEL_INF
CONFIG_NET_STATISTICS_LOG_LEVEL_DBG
CONFIG_NET_STATISTICS_LOG_LEVEL_DEFAULT
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:7`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L7)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_STATISTICS_LOG_LEVEL_DEFAULT`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_LOG_LEVEL_DEFAULT)、[`CONFIG_NET_STATISTICS_LOG_LEVEL_OFF`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_LOG_LEVEL_OFF)、[`CONFIG_NET_STATISTICS_LOG_LEVEL_ERR`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_LOG_LEVEL_ERR)、[`CONFIG_NET_STATISTICS_LOG_LEVEL_WRN`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_LOG_LEVEL_WRN)、[`CONFIG_NET_STATISTICS_LOG_LEVEL_INF`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_LOG_LEVEL_INF)、[`CONFIG_NET_STATISTICS_LOG_LEVEL_DBG`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_LOG_LEVEL_DBG)。

<a id="CONFIG_NET_STATISTICS_LOG_LEVEL_DBG"></a>

## 404.72 `CONFIG_NET_STATISTICS_LOG_LEVEL_DBG`

**提示（Prompt）**：调试（Debug）

**说明（Help）**

除前述级别外，还记录通过 `NET_DBG` 或 `LOG_DBG` 输出的调试日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:36`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L36)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics） → 网络统计（Network statistics）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_STATISTICS_LOG_LEVEL_DEFAULT"></a>

## 404.73 `CONFIG_NET_STATISTICS_LOG_LEVEL_DEFAULT`

**提示（Prompt）**：默认（Default）

**说明（Help）**

使用默认日志级别（default log level）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:41`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L41)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics） → 网络统计（Network statistics）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_STATISTICS_LOG_LEVEL_ERR"></a>

## 404.74 `CONFIG_NET_STATISTICS_LOG_LEVEL_ERR`

**提示（Prompt）**：错误（Error）。

**说明（Help）**

仅记录通过 `NET_ERR` 或 `LOG_ERR` 输出的错误日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:21`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L21)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics） → 网络统计（Network statistics）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_STATISTICS_LOG_LEVEL_INF"></a>

## 404.75 `CONFIG_NET_STATISTICS_LOG_LEVEL_INF`

**提示（Prompt）**：信息（Info）

**说明（Help）**

除前述级别外，还记录通过 `NET_INFO` 或 `LOG_INF` 输出的信息日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:31`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L31)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics） → 网络统计（Network statistics）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_STATISTICS_LOG_LEVEL_OFF"></a>

## 404.76 `CONFIG_NET_STATISTICS_LOG_LEVEL_OFF`

**提示（Prompt）**：关闭（Off）

**说明（Help）**

不输出日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:16`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L16)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics） → 网络统计（Network statistics）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_STATISTICS_LOG_LEVEL_WRN"></a>

## 404.77 `CONFIG_NET_STATISTICS_LOG_LEVEL_WRN`

**提示（Prompt）**：警告（Warning）

**说明（Help）**

除前一级别外，还记录通过 `NET_WARN` 或 `LOG_WRN` 输出的警告日志。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
<choice CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE>
```

**定义位置（Location）**：[`subsys/net/Kconfig.template.log_config.net:26`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/Kconfig.template.log_config.net#L26)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics） → 网络统计（Network statistics）日志级别（Log level）

**配置项引用（Symbol References）**：[`CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS_LOG_LEVEL_CHOICE)。

<a id="CONFIG_NET_STATISTICS_MLD"></a>

## 404.78 `CONFIG_NET_STATISTICS_MLD`

**提示（Prompt）**：多播侦听者发现（Multicast Listener Discovery，MLD）统计

**说明（Help）**

跟踪多播侦听者发现（MLD）相关统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_MLD && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:103`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L103)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_MLD`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_MLD)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_PERIODIC_OUTPUT"></a>

## 404.79 `CONFIG_NET_STATISTICS_PERIODIC_OUTPUT`

**提示（Prompt）**：简单周期输出（Simple periodic output）

**说明（Help）**

定期通过日志（Logging）打印全部统计信息，主要用于测试。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOG && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:32`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L32)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_LOG`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_LOG)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_PER_INTERFACE"></a>

## 404.80 `CONFIG_NET_STATISTICS_PER_INTERFACE`

**提示（Prompt）**：按网络接口收集统计信息（Per-interface statistics）

**说明（Help）**

同时为每个网络接口分别收集统计信息（Statistics）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:19`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L19)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_PKT_FILTER"></a>

## 404.81 `CONFIG_NET_STATISTICS_PKT_FILTER`

**提示（Prompt）**：网络数据包过滤器统计（Network packet filter statistics）

**说明（Help）**

跟踪网络数据包过滤器（Network packet filter）相关统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PKT_FILTER && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:124`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L124)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_PKT_FILTER`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_PKT_FILTER)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_POWER_MANAGEMENT"></a>

## 404.82 `CONFIG_NET_STATISTICS_POWER_MANAGEMENT`

**提示（Prompt）**：电源管理统计（Power management statistics）

**说明（Help）**

提供网络接口进入挂起（Suspend）的次数、最近一次挂起时长，以及平均挂起时长。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_POWER_MANAGEMENT && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:156`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L156)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_POWER_MANAGEMENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_POWER_MANAGEMENT)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_POWER_MANAGEMENT`。

<a id="CONFIG_NET_STATISTICS_PPP"></a>

## 404.83 `CONFIG_NET_STATISTICS_PPP`

**提示（Prompt）**：点对点协议（PPP）统计

**说明（Help）**

跟踪点对点协议（PPP）相关统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:131`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L131)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_PPP)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_QUIC"></a>

## 404.84 `CONFIG_NET_STATISTICS_QUIC`

**提示（Prompt）**：QUIC 统计（Statistics）

**说明（Help）**

跟踪 QUIC 相关统计信息（Statistics）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_QUIC && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:186`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L186)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_RAW"></a>

## 404.85 `CONFIG_NET_STATISTICS_RAW`

**提示（Prompt）**：原始数据包套接字（Raw Packet Socket）统计信息。

**说明（Help）**

跟踪原始数据包套接字（Raw packet socket）相关统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_SOCKETS_PACKET && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:96`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L96)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_SOCKETS_PACKET`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_SOCKETS_PACKET)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_TCP"></a>

## 404.86 `CONFIG_NET_STATISTICS_TCP`

**提示（Prompt）**：TCP 统计（Statistics）

**说明（Help）**

跟踪 TCP 相关统计信息（Statistics）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:89`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L89)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_UDP"></a>

## 404.87 `CONFIG_NET_STATISTICS_UDP`

**提示（Prompt）**：UDP 统计（Statistics）

**说明（Help）**

跟踪 UDP 相关统计信息（Statistics）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_UDP && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:82`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L82)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_UDP`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_UDP)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_USER_API"></a>

## 404.88 `CONFIG_NET_STATISTICS_USER_API`

**提示（Prompt）**：通过网络管理 API（NET MGMT API）提供统计信息

**说明（Help）**

若需要在代码中获取相关统计信息，请启用此项，并使用相应的 `NET_REQUEST_STATS_GET_*` 命令调用 `net_mgmt()`。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**主动选择（Selects）**

```text
CONFIG_NET_MGMT
```

**被选择（Selected by）**

```text
CONFIG_QUIC
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:25`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L25)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_NET_MGMT`](P402_subsys_net_配置项参考_12.md#CONFIG_NET_MGMT)、[`CONFIG_QUIC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_QUIC)。

<a id="CONFIG_NET_STATISTICS_VIA_PROMETHEUS"></a>

## 404.89 `CONFIG_NET_STATISTICS_VIA_PROMETHEUS`

**提示（Prompt）**：通过 Prometheus 导出统计信息（Export statistics）

**说明（Help）**

启用后，向 Prometheus 监测系统（Monitoring system）提供网络统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PROMETHEUS && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_PROMETHEUS`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_PROMETHEUS)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_VPN"></a>

## 404.90 `CONFIG_NET_STATISTICS_VPN`

**提示（Prompt）**：虚拟专用网络（VPN）统计

**说明（Help）**

跟踪虚拟专用网络（VPN）相关统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_VPN && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:179`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L179)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_VPN`](P405_subsys_net_配置项参考_15.md#CONFIG_NET_VPN)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_STATISTICS_WIFI"></a>

## 404.91 `CONFIG_NET_STATISTICS_WIFI`

**提示（Prompt）**：Wi‑Fi 统计信息（Wi-Fi statistics）。

**说明（Help）**

跟踪 Wi-Fi 相关统计信息（Statistics）。注意，此功能要求 Wi-Fi 驱动支持，并由驱动负责收集统计信息。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_WIFI_MGMT && CONFIG_NET_STATISTICS && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.stats:163`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.stats#L163)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 网络统计（Network statistics）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_WIFI_MGMT`](P401_subsys_net_配置项参考_11.md#CONFIG_NET_L2_WIFI_MGMT)、[`CONFIG_NET_STATISTICS`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_STATISTICS)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP"></a>

## 404.92 `CONFIG_NET_TCP`

**提示（Prompt）**：传输控制协议（TCP）

**说明（Help）**

该值取决于网络需求。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**被选择（Selected by）**

```text
CONFIG_MCP_TRANSPORT_HTTP
CONFIG_HTTP_SERVER_VERSION_1
CONFIG_HTTP_SERVER_VERSION_2
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:8`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L8)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack）

**配置项引用（Symbol References）**：[`CONFIG_NET_IP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_IP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)、[`CONFIG_MCP_TRANSPORT_HTTP`](P395_subsys_net_配置项参考_5.md#CONFIG_MCP_TRANSPORT_HTTP)、[`CONFIG_HTTP_SERVER_VERSION_1`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_1)、[`CONFIG_HTTP_SERVER_VERSION_2`](P392_subsys_net_配置项参考_2.md#CONFIG_HTTP_SERVER_VERSION_2)。

> 译注：本数据库快照未收录以下引用的独立定义，保留原始搜索链接，不将其视为已验证的定义：`CONFIG_NET_IP`。

<a id="CONFIG_NET_TCP_ACK_DELAY"></a>

## 404.93 `CONFIG_NET_TCP_ACK_DELAY`

**提示（Prompt）**：TCP 延迟确认超时（Delayed ACK timeout，毫秒）

**说明（Help）**

对于未按 RFC 1122“每收到第二个完整大小的报文段就确认”的规则立即确认的数据，例如收到的报文段未设置 PSH 时，TCP 最多可延迟多少毫秒再发送确认（ACK）。设为 0 表示立即调度 ACK。

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
[0, 1000]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_CHECKSUM"></a>

## 404.94 `CONFIG_NET_TCP_CHECKSUM`

**提示（Prompt）**：检查 TCP 校验和（Checksum）

**说明（Help）**

让 TCP 处理程序检查 TCP 校验和（Checksum）；校验和无效时，丢弃数据包。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:175`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L175)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_CONGESTION_AVOIDANCE"></a>

## 404.95 `CONFIG_NET_TCP_CONGESTION_AVOIDANCE`

**提示（Prompt）**：在 TCP 中实现拥塞避免算法（Congestion avoidance algorithm）

**说明（Help）**

一旦开始丢包，就降低传输速率，以避免给链路造成过大压力。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:193`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L193)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_FAST_RETRANSMIT"></a>

## 404.96 `CONFIG_NET_TCP_FAST_RETRANSMIT`

**提示（Prompt）**：基于重复确认（Duplicate ACK）次数的快速重试算法（Fast-retry algorithm）

**说明（Help）**

数据包丢失时，原文说明接收方会持续确认最后正确接收字节的序号。发送方收到一连串相同序号的确认（ACK）时，可据此推断后续数据包丢失，并立即触发重传（Retransmission），无需等待重传计时器到期。

译注：原文将 ACK 序号描述为“最后正确接收字节的序号”；这里保留其叙述，未将该措辞作为 TCP ACK 字段语义的新定义。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:182`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L182)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_INIT_RETRANSMISSION_TIMEOUT"></a>

## 404.97 `CONFIG_NET_TCP_INIT_RETRANSMISSION_TIMEOUT`

**提示（Prompt）**：重传超时（Retransmission Timeout，RTO）的初始值（毫秒）

**说明（Help）**

影响 TCP 数据包初始重传之间的超时时间，单位为毫秒。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
200
```

**取值范围（Ranges）**

```text
[100, 60000]
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:63`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L63)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_IPV6_ND_REACHABILITY_HINT"></a>

## 404.98 `CONFIG_NET_TCP_IPV6_ND_REACHABILITY_HINT`

**提示（Prompt）**：向 IPv6 邻居发现提供可达性提示（Reachability hint）

**说明（Help）**

启用后，TCP 协议栈通过通知近期发生的前向进展（Forward progress）事件，告知 IPv6 邻居发现（Neighbor Discovery）过程与特定邻居之间的链路处于活动状态，详见 RFC 4861。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_IPV6_ND && CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:247`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L247)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_IPV6_ND`](P400_subsys_net_配置项参考_10.md#CONFIG_NET_IPV6_ND)、[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_ISN_RFC6528"></a>

## 404.99 `CONFIG_NET_TCP_ISN_RFC6528`

**提示（Prompt）**：使用 RFC 6528 的初始序列号（ISN）算法

**说明（Help）**

按 [RFC 6528 第 3 节](https://tools.ietf.org/html/rfc6528) 实现初始序列号（Initial Sequence Number，ISN）计算。若未启用，则通过 `sys_rand32_get()` 获取 ISN。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_PSA_WANT_ALG_SHA_256 && CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:231`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L231)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_PSA_WANT_ALG_SHA_256`](P242_modules_mbedtls_配置项参考_2.md#CONFIG_PSA_WANT_ALG_SHA_256)、[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<a id="CONFIG_NET_TCP_KEEPALIVE"></a>

## 404.100 `CONFIG_NET_TCP_KEEPALIVE`

**提示（Prompt）**：TCP 保活（Keep-alive）支持

**说明（Help）**

启用后，TCP 协议栈可以周期性发送 TCP 保活探测（Keep-alive probe），并支持处理 `SO_KEEPALIVE`、`TCP_KEEPIDLE`、`TCP_KEEPINTVL` 和 `TCP_KEEPCNT` 选项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_TCP && !CONFIG_NET_RAW_MODE && CONFIG_NETWORKING
```

**定义位置（Location）**：[`subsys/net/ip/Kconfig.tcp:200`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/ip/Kconfig.tcp#L200)。

**菜单路径（Menu Path）**：顶层（Top） → 子系统与操作系统服务（Subsystems and OS Services） → 网络（Networking） → 链路层与网络功能（Link layer and networking，含 IP） → IP 协议栈（IP stack） → 传输控制协议（TCP）

**配置项引用（Symbol References）**：[`CONFIG_NET_TCP`](P404_subsys_net_配置项参考_14.md#CONFIG_NET_TCP)、[`CONFIG_NET_RAW_MODE`](P403_subsys_net_配置项参考_13.md#CONFIG_NET_RAW_MODE)、[`CONFIG_NETWORKING`](P395_subsys_net_配置项参考_5.md#CONFIG_NETWORKING)。

<!-- kconfig-navigation -->

[上一章](P403_subsys_net_配置项参考_13.md) · [返回大纲](大纲.md) · [下一章](P405_subsys_net_配置项参考_15.md)
