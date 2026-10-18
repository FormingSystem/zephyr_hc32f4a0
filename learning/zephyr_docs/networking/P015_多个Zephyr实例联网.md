---
id: learning.zephyr-docs.networking.page-15
title: 多个Zephyr实例联网
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/networking_with_multiple_instances.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第15章\_多个Zephyr实例联网

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/networking_with_multiple_instances.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 15.1\_前提（Prerequisites）

本页说明如何让多个 Zephyr 实例通过 Linux 主机联网。实例可以运行在 QEMU 或 `native_sim` 上，主机负责网络连接。

需要官方 [net-tools 网络工具](https://github.com/zephyrproject-rtos/net-tools)。它通常位于标准 Zephyr 工作区的 `tools/net-tools`，也可以克隆该仓库：

```sh
git clone https://github.com/zephyrproject-rtos/net-tools
```

> 译注：克隆命令在读者选择的工作区目录执行，创建外部工具目录 [`net-tools`](https://github.com/zephyrproject-rtos/net-tools)；下面涉及 `net-setup.sh` 的操作从这个工具目录执行。Zephyr 示例构建则从 Zephyr 源码根目录执行。二者是不同目录，不依赖本译文仓库在磁盘上的位置。

## 15.2\_基本安排（Basic Setup）

需要五个终端窗口：终端 1、2 进入工具目录（`cd net-tools`），分别运行 [`net-tools`](https://github.com/zephyrproject-rtos/net-tools) 设置网络接口；终端 3 设置主机网络桥接（Network Bridging）；终端 4、5 为已初始化 Zephyr 环境的开发终端，分别启动两个 Zephyr 实例。

为简化说明，原文以 `qemu_x86` 的 E1000 以太网驱动和 `native_sim` 为例。QEMU 上的其他以太网驱动见[QEMU 以太网联网](P010_QEMU以太网联网.md#networking-with-eth-qemu)。也可以连接两个或更多 `native_sim` 实例。

## 15.3\_创建配置文件（Create Configuration Files）

在启动带网络连接的 QEMU 前，必须为每个 Zephyr 实例创建主机接口。默认的单实例网络设置只用于连接一个 Zephyr 实例与主机，不能直接用于这里的多实例配置。

在 [`net-tools`](https://github.com/zephyrproject-rtos/net-tools) 目录创建 `zephyr1.conf`，写入下面内容。也可将配置放在其他目录，但后续 `-c` 参数必须指向对应文件。

```sh
# Configuration file for setting IP addresses for a network interface.
INTERFACE="$1"
HWADDR="00:00:5e:00:53:11"
IPV6_ADDR_1="2001:db8:100::2"
IPV6_ROUTE_1="2001:db8:100::/64"
IPV4_ADDR_1="198.51.100.2/24"
IPV4_ROUTE_1="198.51.100.0/24"
ip link set dev $INTERFACE up
ip link set dev $INTERFACE address $HWADDR
ip -6 address add $IPV6_ADDR_1 dev $INTERFACE nodad
ip -6 route add $IPV6_ROUTE_1 dev $INTERFACE
ip address add $IPV4_ADDR_1 dev $INTERFACE
ip route add $IPV4_ROUTE_1 dev $INTERFACE > /dev/null 2>&1
```

这是第一个实例对应主机接口的配置：设置接口 MAC 地址，添加 IPv6、IPv4 地址和对应路由。

再创建 `zephyr2.conf`，写入第二个实例对应的配置：

```sh
# Configuration file for setting IP addresses for a network interface.
INTERFACE="$1"
HWADDR="00:00:5e:00:53:22"
IPV6_ADDR_1="2001:db8:200::2"
IPV6_ROUTE_1="2001:db8:200::/64"
IPV4_ADDR_1="203.0.113.2/24"
IPV4_ROUTE_1="203.0.113.0/24"
ip link set dev $INTERFACE up
ip link set dev $INTERFACE address $HWADDR
ip -6 address add $IPV6_ADDR_1 dev $INTERFACE nodad
ip -6 route add $IPV6_ROUTE_1 dev $INTERFACE
ip address add $IPV4_ADDR_1 dev $INTERFACE
ip route add $IPV4_ROUTE_1 dev $INTERFACE > /dev/null 2>&1
```

两个配置采用不同地址组：IPv6 为 `2001:db8:100::/64` 与 `2001:db8:200::/64`，IPv4 为 `198.51.100.0/24` 与 `203.0.113.0/24`。

## 15.4\_创建以太网接口（Create Ethernet Interfaces）

在终端 1 的 [`net-tools`](https://github.com/zephyrproject-rtos/net-tools) 目录执行，创建 `zeth.1`：

```sh
./net-setup.sh -c zephyr1.conf -i zeth.1
```

在终端 2 的相同工具目录执行，创建 `zeth.2`：

```sh
./net-setup.sh -c zephyr2.conf -i zeth.2
```

## 15.5\_设置网络桥接（Setup Network Bridging）

在终端 3 的 Linux 主机终端执行。以下命令创建 `zeth-br` 网桥，将两个接口加入，并启用网桥；需要相应主机网络管理权限：

```sh
sudo brctl addbr zeth-br
sudo brctl addif zeth-br zeth.1
sudo brctl addif zeth-br zeth.2
sudo ifconfig zeth-br up
```

## 15.6\_启动 Zephyr 实例（Start Zephyr Instances）

下面使用[高级回显服务器（Echo server）](P047_高级回显服务器示例.md#sockets-echo-server)和[高级回显客户端（Echo client）](P048_高级回显客户端示例.md#sockets-echo-client)两个应用，也可按需要换用其他应用。每个终端选择与运行平台对应的一组命令，不需要同时启动同一角色的 QEMU 和 native 版本。

在终端 4 的 Zephyr 源码根目录构建并启动 QEMU 服务器：

```sh
west build -d build/server -b qemu_x86 -t run \
   samples/net/sockets/echo_server -- \
   -DEXTRA_CONF_FILE=overlay-e1000.conf \
   -DCONFIG_NET_CONFIG_MY_IPV4_ADDR=\"198.51.100.1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV4_ADDR=\"203.0.113.1\" \
   -DCONFIG_NET_CONFIG_MY_IPV6_ADDR=\"2001:db8:100::1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV6_ADDR=\"2001:db8:200::1\" \
   -DCONFIG_NET_CONFIG_MY_IPV4_GW=\"203.0.113.1\" \
   -DCONFIG_ETH_QEMU_IFACE_NAME=\"zeth.1\" \
   -DCONFIG_NET_QEMU_DEVICE_EXTRA_ARGS=\"mac=00:00:5e:00:53:01\"
```

或者使用 `native_sim` 服务器：

```sh
west build -d build/server -b native_sim \
   samples/net/sockets/echo_server -- \
   -DCONFIG_NET_CONFIG_MY_IPV4_ADDR=\"198.51.100.1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV4_ADDR=\"203.0.113.1\" \
   -DCONFIG_NET_CONFIG_MY_IPV6_ADDR=\"2001:db8:100::1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV6_ADDR=\"2001:db8:200::1\" \
   -DCONFIG_NET_CONFIG_MY_IPV4_GW=\"203.0.113.1\"
build/server/zephyr/zephyr.exe --eth-if=zeth.1 --mac-addr=00:00:5e:00:53:01
```

在终端 5 的 Zephyr 源码根目录构建并启动 QEMU 客户端：

```sh
west build -d build/client -b qemu_x86 -t run \
   samples/net/sockets/echo_client -- \
   -DEXTRA_CONF_FILE=overlay-e1000.conf \
   -DCONFIG_NET_CONFIG_MY_IPV4_ADDR=\"203.0.113.1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV4_ADDR=\"198.51.100.1\" \
   -DCONFIG_NET_CONFIG_MY_IPV6_ADDR=\"2001:db8:200::1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV6_ADDR=\"2001:db8:100::1\" \
   -DCONFIG_NET_CONFIG_MY_IPV4_GW=\"198.51.100.1\" \
   -DCONFIG_ETH_QEMU_IFACE_NAME=\"zeth.2\" \
   -DCONFIG_NET_QEMU_DEVICE_EXTRA_ARGS=\"mac=00:00:5e:00:53:02\"
```

或者使用 `native_sim` 客户端：

```sh
west build -d build/client -b native_sim \
   samples/net/sockets/echo_client -- \
   -DCONFIG_NET_CONFIG_MY_IPV4_ADDR=\"203.0.113.1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV4_ADDR=\"198.51.100.1\" \
   -DCONFIG_NET_CONFIG_MY_IPV6_ADDR=\"2001:db8:200::1\" \
   -DCONFIG_NET_CONFIG_PEER_IPV6_ADDR=\"2001:db8:100::1\" \
   -DCONFIG_NET_CONFIG_MY_IPV4_GW=\"198.51.100.1\"
build/client/zephyr/zephyr.exe --eth-if=zeth.2 --mac-addr=00:00:5e:00:53:02
```

主机防火墙（Firewall）必须允许 `zeth.1`、`zeth.2` 和 `zeth-br` 之间的流量。

> 译注：这里完整保留官方配置中的地址、对端地址、网关和接口组合。调整地址时，应一起检查子网、路由及网关可达性；网桥负责二层帧转发，本身不会自动替读者修正三层 IP 配置。`build/server`、`build/client` 是上述命令生成的构建目录；本文未把这些示例记作已执行的联网实验。


<a id="networking-with-multiple-zephyr-instances"></a>
<a id="networking-with-multiple-instances"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="id6"></a>
<a id="prerequisites"></a>
<a id="basic-setup"></a>
<a id="step-1-create-configuration-files"></a>
<a id="step-2-create-ethernet-interfaces"></a>
<a id="step-3-setup-network-bridging"></a>
<a id="step-4-start-zephyr-instances"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：USB设备联网](P014_USB设备联网.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：native_sim以太网桥](P016_native_sim以太网桥.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P014_USB设备联网.md) · [返回大纲](大纲.md) · [下一章](P016_native_sim以太网桥.md)

</details>

<!-- reading-navigation:end -->
