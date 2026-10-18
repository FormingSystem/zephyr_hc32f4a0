---
id: learning.zephyr-docs.kconfig-reference.page-131
title: "`drivers/net`配置项参考"
kind: reference
status: evolving
domains: [zephyr, kconfig, configuration]
source_url: https://docs.zephyrproject.org/latest/kconfig.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；分册、相对路径和明确标注的译注为本地新增。 -->

# 第131章\_`drivers/net`配置项参考

本章翻译官方 Kconfig 数据库中 `drivers/net` 的 34 条定义记录。提示（Prompt）、帮助（Help）与菜单路径均已翻译；条件表达式、默认值和配置标识符保留原值。原页：[Kconfig Search](https://docs.zephyrproject.org/latest/kconfig.html)。来源数据库版本为 `main`，快照摘要与完整覆盖范围见[本册大纲](大纲.md)。

`main` 源码链接随上游变化；行号来自本次数据库快照，不能视为固定提交定位。无提示的配置项保留其不可直接由用户赋值的属性。原库中存在未收录定义的交叉引用，本章在对应位置明确标出。

<a id="CONFIG_NET_CANBUS"></a>

## 131.1 `CONFIG_NET_CANBUS`

**提示（Prompt）**：控制器局域网（Controller Area Network，CAN）总线网络驱动

**说明（Help）**

启用 CAN 总线网络驱动。此驱动在 CAN 控制器驱动 API 之上提供网络接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_CAN && CONFIG_NET_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_CANBUS_RAW
```

**定义位置（Location）**：[`drivers/net/Kconfig:221`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L221)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers）

**配置项引用（Symbol References）**：[`CONFIG_CAN`](P060_drivers_can_配置项参考.md#CONFIG_CAN)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)、[`CONFIG_NET_L2_CANBUS_RAW`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_CANBUS_RAW)。

<a id="CONFIG_NET_CANBUS_INIT_PRIORITY"></a>

## 131.2 `CONFIG_NET_CANBUS_INIT_PRIORITY`

**提示（Prompt）**：CAN 总线网络设备初始化优先级

**说明（Help）**

CAN 总线网络设备的初始化优先级。数值需要低于网络协议栈，并高于 CAN 控制器驱动。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CANBUS && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
81
```

**定义位置（Location）**：[`drivers/net/Kconfig:237`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L237)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 控制器局域网（Controller Area Network，CAN）总线网络驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_CANBUS`](P131_drivers_net_配置项参考.md#CONFIG_NET_CANBUS)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_DRIVERS"></a>

## 131.3 `CONFIG_NET_DRIVERS`

**提示（Prompt）**：网络驱动（Network Drivers）

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**被弱选择（Implied by）**

```text
CONFIG_NET_QEMU_PPP
```

**定义位置（Location）**：[`drivers/net/Kconfig:4`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L4)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_QEMU_PPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_QEMU_PPP)。

<a id="CONFIG_NET_LOOPBACK"></a>

## 131.4 `CONFIG_NET_LOOPBACK`

**提示（Prompt）**：网络回环（Loopback）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_NET_L2_DUMMY
```

**定义位置（Location）**：[`drivers/net/Kconfig:192`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L192)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)、[`CONFIG_NET_L2_DUMMY`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_DUMMY)。

<a id="CONFIG_NET_LOOPBACK_MTU"></a>

## 131.5 `CONFIG_NET_LOOPBACK_MTU`

**提示（Prompt）**：回环接口最大传输单元（MTU）

**说明（Help）**

此选项设置回环接口的最大传输单元（MTU）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOOPBACK && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/net/Kconfig:204`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L204)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 网络回环（Loopback）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_LOOPBACK`](P131_drivers_net_配置项参考.md#CONFIG_NET_LOOPBACK)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_LOOPBACK_SIMULATE_PACKET_DROP"></a>

## 131.6 `CONFIG_NET_LOOPBACK_SIMULATE_PACKET_DROP`

**提示（Prompt）**：可控制丢包（Controllable Packet Drop）

**说明（Help）**

允许接口使用可控制的丢包率，仅用于测试，正常应用不应启用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_LOOPBACK && CONFIG_NET_DRIVERS
```

**定义位置（Location）**：[`drivers/net/Kconfig:198`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L198)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 网络回环（Loopback）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_LOOPBACK`](P131_drivers_net_配置项参考.md#CONFIG_NET_LOOPBACK)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_NATIVE_OFFLOADED_SOCKETS"></a>

## 131.7 `CONFIG_NET_NATIVE_OFFLOADED_SOCKETS`

**提示（Prompt）**：原生模拟器（Native Simulator）卸载式套接字

**说明（Help）**

原生模拟器的卸载式套接字（Offloaded Socket）使用主机 BSD 套接字 API，例如 `socket()`、`connect()`、`send()`、`recvfrom()` 等，提供网络功能。与原生 TAP 以太网驱动相比，其主要优势是主机侧无需额外设置即可使用。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_ARCH_POSIX && CONFIG_NET_SOCKETS_OFFLOAD && CONFIG_NET_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_NATIVE_USE_NSI_ERRNO
CONFIG_NATIVE_USE_NSI_FCNTL
```

**定义位置（Location）**：[`drivers/net/Kconfig:252`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L252)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers）

**配置项引用（Symbol References）**：[`CONFIG_ARCH_POSIX`](P026_arch_Kconfig_配置项参考_1.md#CONFIG_ARCH_POSIX)、[`CONFIG_NET_SOCKETS_OFFLOAD`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_OFFLOAD)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)、[`CONFIG_NATIVE_USE_NSI_ERRNO`](P033_arch_posix_配置项参考.md#CONFIG_NATIVE_USE_NSI_ERRNO)、[`CONFIG_NATIVE_USE_NSI_FCNTL`](P033_arch_posix_配置项参考.md#CONFIG_NATIVE_USE_NSI_FCNTL)。

<a id="CONFIG_NET_NATIVE_OFFLOADED_SOCKETS_CONNECTIVITY_SIM"></a>

## 131.8 `CONFIG_NET_NATIVE_OFFLOADED_SOCKETS_CONNECTIVITY_SIM`

**提示（Prompt）**：网络连接 API（Network Connectivity API）支持

**说明（Help）**

模拟一个根据网络连接 API 调用，经过一定延迟后进出休眠状态（Dormant State）的接口。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_OFFLOADED_SOCKETS && CONFIG_NET_DRIVERS
```

**定义位置（Location）**：[`drivers/net/Kconfig:288`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L288)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 原生模拟器（Native Simulator）卸载式套接字

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_OFFLOADED_SOCKETS`](P131_drivers_net_配置项参考.md#CONFIG_NET_NATIVE_OFFLOADED_SOCKETS)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_NATIVE_OFFLOADED_SOCKETS_CONNECTIVITY_SIM_AUTO_CONNECT"></a>

## 131.9 `CONFIG_NET_NATIVE_OFFLOADED_SOCKETS_CONNECTIVITY_SIM_AUTO_CONNECT`

**提示（Prompt）**：自动连接（Automatically Connect）

**说明（Help）**

设置此选项后，连接管理器（Connection Manager）会在网络接口启用后自动调用 connect。此选项设置默认值；它对应的标志可在运行时通过 `conn_mgr_if_set_flag()` 设置。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_OFFLOADED_SOCKETS_CONNECTIVITY_SIM && CONFIG_NET_NATIVE_OFFLOADED_SOCKETS && CONFIG_NET_DRIVERS
```

**定义位置（Location）**：[`drivers/net/Kconfig:294`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L294)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 原生模拟器（Native Simulator）卸载式套接字 → 网络连接 API（Network Connectivity API）支持

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_OFFLOADED_SOCKETS_CONNECTIVITY_SIM`](P131_drivers_net_配置项参考.md#CONFIG_NET_NATIVE_OFFLOADED_SOCKETS_CONNECTIVITY_SIM)、[`CONFIG_NET_NATIVE_OFFLOADED_SOCKETS`](P131_drivers_net_配置项参考.md#CONFIG_NET_NATIVE_OFFLOADED_SOCKETS)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_NATIVE_OFFLOADED_SOCKETS_EPOLL_WAIT_INTERVAL"></a>

## 131.10 `CONFIG_NET_NATIVE_OFFLOADED_SOCKETS_EPOLL_WAIT_INTERVAL`

**提示（Prompt）**：两次 `epoll_wait()` 调用之间的间隔，以模拟微秒计

**说明（Help）**

未检测到待处理事件时，到下一次 `epoll_wait()` 调用前等待的模拟微秒数。需要更低的网络流量延迟时，可减小此值，代价是更高的 CPU 处理开销。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_OFFLOADED_SOCKETS && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
1000
```

**定义位置（Location）**：[`drivers/net/Kconfig:267`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L267)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 原生模拟器（Native Simulator）卸载式套接字

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_OFFLOADED_SOCKETS`](P131_drivers_net_配置项参考.md#CONFIG_NET_NATIVE_OFFLOADED_SOCKETS)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_NATIVE_OFFLOADED_SOCKETS_HOST_IF_NAME"></a>

## 131.11 `CONFIG_NET_NATIVE_OFFLOADED_SOCKETS_HOST_IF_NAME`

**提示（Prompt）**：卸载接口所代表的主机接口（Represented Host Interface）

**说明（Help）**

卸载接口所代表的 Linux 主机网络接口名称。该接口地址会映射到 Zephyr `net_if`，其主机 `ifindex` 用于限定组播加入、出口和 IPv6 作用域。Zephyr 接口名称在主机上不存在，因此不能直接使用。留空时，使用默认路由（默认网关）对应的接口。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE_OFFLOADED_SOCKETS && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
""
```

**定义位置（Location）**：[`drivers/net/Kconfig:277`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L277)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 原生模拟器（Native Simulator）卸载式套接字

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE_OFFLOADED_SOCKETS`](P131_drivers_net_配置项参考.md#CONFIG_NET_NATIVE_OFFLOADED_SOCKETS)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP"></a>

## 131.12 `CONFIG_NET_PPP`

**提示（Prompt）**：基于 UART 的点对点协议（PPP）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_L2_PPP && CONFIG_NET_NATIVE && (CONFIG_NET_TEST || n) && CONFIG_NET_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_CRC
```

**定义位置（Location）**：[`drivers/net/Kconfig:15`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L15)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_L2_PPP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_L2_PPP)、[`CONFIG_NET_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE)、[`CONFIG_NET_TEST`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_TEST)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)、[`CONFIG_CRC`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_CRC)。

<a id="CONFIG_NET_PPP_ASYNC_UART"></a>

## 131.13 `CONFIG_NET_PPP_ASYNC_UART`

**提示（Prompt）**：使用异步 UART API。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_UART_ASYNC_API && CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**定义位置（Location）**：[`drivers/net/Kconfig:24`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L24)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_UART_ASYNC_API`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_ASYNC_API)、[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_ASYNC_UART_RX_ENABLE_TIMEOUT"></a>

## 131.14 `CONFIG_NET_PPP_ASYNC_UART_RX_ENABLE_TIMEOUT`

**提示（Prompt）**：`uart_rx_enable()` 的超时时间，单位为毫秒

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP_ASYNC_UART && CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
100
```

**定义位置（Location）**：[`drivers/net/Kconfig:130`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L130)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP_ASYNC_UART`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP_ASYNC_UART)、[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_ASYNC_UART_RX_RECOVERY_TIMEOUT"></a>

## 131.15 `CONFIG_NET_PPP_ASYNC_UART_RX_RECOVERY_TIMEOUT`

**提示（Prompt）**：UART 接收恢复超时（RX Recovery Timeout），单位为毫秒

**说明（Help）**

无法继续从 UART 接收数据时，UART 接收处于禁用状态的时间。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP_ASYNC_UART && CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
200
```

**定义位置（Location）**：[`drivers/net/Kconfig:123`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L123)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP_ASYNC_UART`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP_ASYNC_UART)、[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_ASYNC_UART_TX_BUF_LEN"></a>

## 131.16 `CONFIG_NET_PPP_ASYNC_UART_TX_BUF_LEN`

**提示（Prompt）**：写入数据的 UART 发送缓冲区长度。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP_ASYNC_UART && CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
2048
```

**定义位置（Location）**：[`drivers/net/Kconfig:115`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L115)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP_ASYNC_UART`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP_ASYNC_UART)、[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_ASYNC_UART_TX_TIMEOUT"></a>

## 131.17 `CONFIG_NET_PPP_ASYNC_UART_TX_TIMEOUT`

**提示（Prompt）**：UART 传输超时，单位为毫秒；0 表示无超时。

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP_ASYNC_UART && CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
0
```

**定义位置（Location）**：[`drivers/net/Kconfig:119`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L119)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP_ASYNC_UART`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP_ASYNC_UART)、[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_CAPTURE"></a>

## 131.18 `CONFIG_NET_PPP_CAPTURE`

**提示（Prompt）**：捕获收到的 PPP 数据包（Packet Capture）

**说明（Help）**

启用 PPP 数据包捕获。需要在核心网络协议栈中配置抓包，将捕获的数据包发送到外部系统。这要求使用一条非 PPP 网络连接，发送数据包以供处理。注意，不能使用 PPP 连接发送捕获的数据包，否则会造成递归。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_CAPTURE_COOKED_MODE && CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**定义位置（Location）**：[`drivers/net/Kconfig:74`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L74)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_CAPTURE_COOKED_MODE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_CAPTURE_COOKED_MODE)、[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_CAPTURE_BUF_SIZE"></a>

## 131.19 `CONFIG_NET_PPP_CAPTURE_BUF_SIZE`

**提示（Prompt）**：保存完整 PPP 数据包的捕获缓冲区（Capture Buffer）

**说明（Help）**

捕获的 PPP 帧暂存在此缓冲区。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP_CAPTURE && CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/net/Kconfig:85`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L85)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动 → 捕获收到的 PPP 数据包（Packet Capture）

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP_CAPTURE`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP_CAPTURE)、[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_DRV_NAME"></a>

## 131.20 `CONFIG_NET_PPP_DRV_NAME`

**提示（Prompt）**：PPP 驱动名称（Driver Name）

**说明（Help）**

此选项设置驱动名称（Driver Name）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
"ppp"
```

**定义位置（Location）**：[`drivers/net/Kconfig:28`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L28)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_MTU_MRU"></a>

## 131.21 `CONFIG_NET_PPP_MTU_MRU`

**提示（Prompt）**：PPP 最大传输／接收单元（MTU/MRU）

**说明（Help）**

此选项设置 PPP 链路的最大传输单元（MTU）和最大接收单元（MRU）。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
1500
```

**定义位置（Location）**：[`drivers/net/Kconfig:34`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L34)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_RINGBUF_SIZE"></a>

## 131.22 `CONFIG_NET_PPP_RINGBUF_SIZE`

**提示（Prompt）**：PPP 环形缓冲区大小（Ring Buffer Size）

**说明（Help）**

将数据从接收中断服务例程（RX ISR）传给工作线程时使用的 PPP 环形缓冲区大小；工作线程随后将数据交给 IP 协议栈。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
256
```

**定义位置（Location）**：[`drivers/net/Kconfig:47`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L47)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_RX_PRIORITY"></a>

## 131.23 `CONFIG_NET_PPP_RX_PRIORITY`

**提示（Prompt）**：接收工作队列线程优先级（RX Workqueue Thread Priority）

**说明（Help）**

设置接收工作队列线程的优先级。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
7
```

**定义位置（Location）**：[`drivers/net/Kconfig:60`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L60)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_RX_STACK_SIZE"></a>

## 131.24 `CONFIG_NET_PPP_RX_STACK_SIZE`

**提示（Prompt）**：为接收调制解调器数据分配的栈大小

**说明（Help）**

设置 PPP 接收工作队列使用的栈大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
768
```

**定义位置（Location）**：[`drivers/net/Kconfig:54`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L54)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_UART_BUF_LEN"></a>

## 131.25 `CONFIG_NET_PPP_UART_BUF_LEN`

**提示（Prompt）**：从 UART 读取数据时的缓冲区长度

**说明（Help）**

此选项设置接收所读数据的 UART 缓冲区大小。

**类型（Type）**：整数（Integer），`int`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
8
```

**定义位置（Location）**：[`drivers/net/Kconfig:40`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L40)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_NET_PPP_VERIFY_FCS"></a>

## 131.26 `CONFIG_NET_PPP_VERIFY_FCS`

**提示（Prompt）**：验证收到的帧校验序列（FCS）是否有效

**说明（Help）**

如果链路可靠，禁用此项可能有意义，因为验证收到的数据包需要花费一定时间。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**定义位置（Location）**：[`drivers/net/Kconfig:66`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L66)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_PPP_CLIENT_CLIENTSERVER"></a>

## 131.27 `CONFIG_PPP_CLIENT_CLIENTSERVER`

**提示（Prompt）**：用 CLIENTSERVER 响应 CLIENT 请求

**说明（Help）**

仅在需要与 Microsoft Windows PC 建立 PPP 连接时才需要此项。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**定义位置（Location）**：[`drivers/net/Kconfig:101`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L101)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_PPP_MAC_ADDR"></a>

## 131.28 `CONFIG_PPP_MAC_ADDR`

**提示（Prompt）**：接口 MAC 地址

**说明（Help）**

指定 PPP 接口的 MAC 地址，格式为六个以冒号分隔的十六进制 8 位值，例如 `aa:33:cc:22:e2:c0`。默认空字符串表示由代码生成 `00:00:5E:00:53:XX`，其中 `XX` 为随机值。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**定义位置（Location）**：[`drivers/net/Kconfig:92`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L92)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_PPP_NET_IF_NO_AUTO_START"></a>

## 131.29 `CONFIG_PPP_NET_IF_NO_AUTO_START`

**提示（Prompt）**：禁用 PPP 接口自动启动（Auto-start）

**说明（Help）**

此选项允许用户禁止 PPP 接口在初始化后立即自动启动。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_PPP && CONFIG_NET_DRIVERS
```

**定义位置（Location）**：[`drivers/net/Kconfig:107`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L107)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 基于 UART 的点对点协议（PPP）驱动

**配置项引用（Symbol References）**：[`CONFIG_NET_PPP`](P131_drivers_net_配置项参考.md#CONFIG_NET_PPP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_SLIP"></a>

## 131.30 `CONFIG_SLIP`

**提示（Prompt）**：串行线路互联网协议（SLIP）驱动

**说明（Help）**：原库未提供帮助正文。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_NET_NATIVE && CONFIG_NET_DRIVERS
```

**主动选择（Selects）**

```text
CONFIG_UART_PIPE
CONFIG_UART_INTERRUPT_DRIVEN
```

**被选择（Selected by）**

```text
CONFIG_NET_SLIP_TAP
```

**定义位置（Location）**：[`drivers/net/Kconfig:147`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L147)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers）

**配置项引用（Symbol References）**：[`CONFIG_NET_NATIVE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_NATIVE)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)、[`CONFIG_UART_PIPE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_PIPE)、[`CONFIG_UART_INTERRUPT_DRIVEN`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UART_INTERRUPT_DRIVEN)、[`CONFIG_NET_SLIP_TAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SLIP_TAP)。

<a id="CONFIG_SLIP_DRV_NAME"></a>

## 131.31 `CONFIG_SLIP_DRV_NAME`

**提示（Prompt）**：SLIP 驱动名称（Driver Name）

**说明（Help）**

此选项设置驱动名称（Driver Name）。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SLIP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
"slip"
```

**定义位置（Location）**：[`drivers/net/Kconfig:155`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L155)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 串行线路互联网协议（SLIP）驱动

**配置项引用（Symbol References）**：[`CONFIG_SLIP`](P131_drivers_net_配置项参考.md#CONFIG_SLIP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_SLIP_MAC_ADDR"></a>

## 131.32 `CONFIG_SLIP_MAC_ADDR`

**提示（Prompt）**：接口 MAC 地址

**说明（Help）**

指定 SLIP 接口的 MAC 地址，格式为六个以冒号分隔的十六进制 8 位值，例如 `aa:33:cc:22:e2:c0`。默认空字符串表示由代码生成 `00:00:5E:00:53:XX`，其中 `XX` 为随机值。

**类型（Type）**：字符串（String），`string`。

**依赖条件（Dependencies）**

```text
CONFIG_SLIP && CONFIG_NET_DRIVERS
```

**定义位置（Location）**：[`drivers/net/Kconfig:178`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L178)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 串行线路互联网协议（SLIP）驱动

**配置项引用（Symbol References）**：[`CONFIG_SLIP`](P131_drivers_net_配置项参考.md#CONFIG_SLIP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_SLIP_STATISTICS"></a>

## 131.33 `CONFIG_SLIP_STATISTICS`

**提示（Prompt）**：SLIP 网络连接统计（Connection Statistics）

**说明（Help）**

此选项启用 SLIP 驱动的统计支持。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SLIP && CONFIG_NET_DRIVERS
```

**定义位置（Location）**：[`drivers/net/Kconfig:167`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L167)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 串行线路互联网协议（SLIP）驱动

**配置项引用（Symbol References）**：[`CONFIG_SLIP`](P131_drivers_net_配置项参考.md#CONFIG_SLIP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)。

<a id="CONFIG_SLIP_TAP"></a>

## 131.34 `CONFIG_SLIP_TAP`

**提示（Prompt）**：使用 TAP 接口连接主机

**说明（Help）**

在 TAP 模式中，通过 SLIP 传输以太网帧（Ethernet Frame）。

**类型（Type）**：布尔值（Boolean），`bool`。

**依赖条件（Dependencies）**

```text
CONFIG_SLIP && CONFIG_NET_DRIVERS
```

**默认值（Defaults）**

```text
y
```

**被选择（Selected by）**

```text
CONFIG_NET_SLIP_TAP
```

**定义位置（Location）**：[`drivers/net/Kconfig:172`](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/net/Kconfig#L172)。

**菜单路径（Menu Path）**：顶层（Top） → 设备驱动（Device Drivers） → 网络驱动（Network Drivers） → 串行线路互联网协议（SLIP）驱动

**配置项引用（Symbol References）**：[`CONFIG_SLIP`](P131_drivers_net_配置项参考.md#CONFIG_SLIP)、[`CONFIG_NET_DRIVERS`](P131_drivers_net_配置项参考.md#CONFIG_NET_DRIVERS)、[`CONFIG_NET_SLIP_TAP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SLIP_TAP)。

<!-- kconfig-navigation -->

[上一章](P130_drivers_mux_配置项参考.md) · [返回大纲](大纲.md) · [下一章](P132_drivers_opamp_配置项参考.md)
