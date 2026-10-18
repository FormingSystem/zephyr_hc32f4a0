---
id: learning.zephyr-docs.networking.page-16
title: native_sim以太网桥
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/eth_bridge_native_sim_setup.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_native_sim以太网桥

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/eth_bridge_native_sim_setup.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 16.1\_用途与主机接口

本页说明如何在 Linux 主机与 [`native_sim`](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim) 上运行的 Zephyr 应用之间建立桥接以太网（Bridged Ethernet）。这适合测试由 [`CONFIG_NET_ETHERNET_BRIDGE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_ETHERNET_BRIDGE) 启用的以太网桥（Ethernet Bridge）功能。

在此配置中，`net-tools` 创建主机接口 `zeth0`、`zeth1`，并将它们连接到 Zephyr 的 [`native_sim`](../native_reference/P004_Native_Simulator本机模拟器.md#native_sim) 应用。先在 Linux 主机创建这两个接口：

```sh
cd $ZEPHYR_BASE/../tools/net-tools
./net-setup.sh -c zeth-multiface.conf -i zeth0 -t 2
```

`-c` 指定配置文件；工具自带的 `zeth-multiface.conf` 专门用于在主机创建多个接口。`-i` 指定第一个主机接口的名称，`-t` 指定接口数量。

> 译注：`ZEPHYR_BASE` 是当前 Zephyr 源码根目录；命令沿用官方工作区中外部工具位于 `tools/net-tools` 的布局。网络接口创建需要相应主机权限；它们不是仓库中的文件。

主机接口的原始输出示例如下：

```text
zeth0: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
       inet 192.0.2.2  netmask 255.255.255.255  broadcast 0.0.0.0
       inet6 2001:db8::2  prefixlen 128  scopeid 0x0<global>
       inet6 fe80::200:5eff:fe00:5300  prefixlen 64  scopeid 0x20<link>
       ether 00:00:5e:00:53:00  txqueuelen 1000  (Ethernet)
       RX packets 33  bytes 2408 (2.4 KB)
       RX errors 0  dropped 0  overruns 0  frame 0
       TX packets 49  bytes 4092 (4.0 KB)
       TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

zeth1: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
       inet 198.51.100.1  netmask 255.255.255.255  broadcast 0.0.0.0
       inet6 fe80::200:5eff:fe00:5301  prefixlen 64  scopeid 0x20<link>
       inet6 2001:db8:2::1  prefixlen 128  scopeid 0x0<global>
       ether 00:00:5e:00:53:01  txqueuelen 1000  (Ethernet)
       RX packets 21  bytes 1340 (1.3 KB)
       RX errors 0  dropped 0  overruns 0  frame 0
       TX packets 45  bytes 3916 (3.9 KB)
       TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

## 16.2\_添加第二个 TAP 接口并运行应用

接下来使用[高级回显服务器（Echo server）示例](P047_高级回显服务器示例.md#sockets-echo-server)并启用以太网桥接支持。桥接需要第二个 TAP 接口（TAP Interface）；创建名为 `second-iface.overlay` 的设备树覆盖文件（Devicetree Overlay），添加第二个 `zephyr,native-tap` 接口：

```dts
/ {
    zeth1: zeth1 {
        compatible = "zephyr,native-tap";
        status = "okay";
        zephyr,random-mac-address;
        host-interface = "zeth1";
    };
};
```

> 译注：该 overlay 是按本页说明自行创建的文件。下面命令以 Zephyr 源码根目录为当前位置，使用应用内的相对 overlay 名称；默认应用配置目录下可将文件保存为 `samples/net/sockets/echo_server/second-iface.overlay`。如果改用其他应用配置目录，应随之调整文件位置及 `EXTRA_DTC_OVERLAY_FILE` 输入。它不是已随本译文生成的实验文件。

在 Linux 主机的 Zephyr 源码根目录构建并运行应用，同时指定该 overlay：

```sh
west build -p -b native_sim -d ../build/echo-server \
   samples/net/sockets/echo_server -- \
   -DCONFIG_UART_NATIVE_PTY_AUTOATTACH_DEFAULT_CMD="\"gnome-terminal -- screen %s\"" \
   -DCONFIG_NET_ETHERNET_BRIDGE=y \
   -DCONFIG_NET_ETHERNET_BRIDGE_SHELL=y \
   -DEXTRA_DTC_OVERLAY_FILE=second-iface.overlay \
   -DCONFIG_NET_IF_MAX_IPV6_COUNT=2 \
   -DCONFIG_NET_IF_MAX_IPV4_COUNT=2
../build/echo-server/zephyr/zephyr.exe -attach_uart
```

命令创建并运行支持桥接的高级回显服务器，但此时桥接尚未配置。`../build/echo-server` 是命令指定并生成的构建目录；自动打开串口窗口的原例依赖 `gnome-terminal` 与 `screen`。

## 16.3\_配置并检查网桥

可以通过网桥 shell（Bridge Shell）配置，也可以在应用中直接调用桥接 API。原文在 **Zephyr shell** 中执行：

```text
net bridge addif 1 3 2
net iface up 1
```

此例网桥接口索引（Interface Index）为 `1`，以太网接口索引为 `2`、`3`，它们对应主机的 `zeth0`、`zeth1`。

Zephyr 侧通过 `net iface` 查看接口，原始示例输出如下：

```text
net iface
Hostname: zephyr

Interface bridge0 (0x8090ebc) (Virtual) [1]
==================================
Virtual name : <enabled>
No attached network interface.
Link addr : 3B:DB:31:0F:CC:B6
MTU       : 1500
Flags     : NO_AUTO_START
Device    : BRIDGE_0 (0x8088354)
Promiscuous mode : disabled
IPv6 not enabled for this interface.
IPv4 not enabled for this interface.

Interface eth0 (0x8090fcc) (Ethernet) [2]
===================================
Link addr : 02:00:5E:00:53:D2
MTU       : 1500
Flags     : AUTO_START,IPv4,IPv6
Device    : zeth0 (0x808837c)
Promiscuous mode : disabled
Ethernet capabilities supported:
        TXTIME
        Promiscuous mode
Ethernet PHY device: <none> (0)
IPv6 unicast addresses (max 3):
        fe80::5eff:fe00:53d2 autoconf preferred infinite
        2001:db8::1 manual preferred infinite
IPv6 multicast addresses (max 4):
        ff02::1
        ff02::1:ff00:53d2
        ff02::1:ff00:1
IPv6 prefixes (max 2):
        <none>
IPv6 hop limit           : 64
IPv6 base reachable time : 30000
IPv6 reachable time      : 18476
IPv6 retransmit timer    : 0
IPv4 unicast addresses (max 1):
        192.0.2.1/255.255.255.0 manual preferred infinite
IPv4 multicast addresses (max 2):
        224.0.0.1
IPv4 gateway : 0.0.0.0

Interface eth1 (0x80910dc) (Ethernet) [3]
===================================
Link addr : 02:00:5E:00:53:87
MTU       : 1500
Flags     : AUTO_START,IPv4,IPv6
Device    : zeth1 (0x8088368)
Promiscuous mode : disabled
Ethernet capabilities supported:
        TXTIME
        Promiscuous mode
Ethernet PHY device: <none> (0)
IPv6 unicast addresses (max 3):
        fe80::5eff:fe00:5387 autoconf preferred infinite
IPv6 multicast addresses (max 4):
        ff02::1
        ff02::1:ff00:5387
IPv6 prefixes (max 2):
        <none>
IPv6 hop limit           : 64
IPv6 base reachable time : 30000
IPv6 reachable time      : 25158
IPv6 retransmit timer    : 0
IPv4 unicast addresses (max 1):
        <none>
IPv4 multicast addresses (max 2):
        224.0.0.1
IPv4 gateway : 0.0.0.0
```

`net bridge` 显示当前桥接状态：

```text
net bridge
Bridge Status   Config   Interfaces
1      up       ok       2 3
```

`addif` 将以太网接口 `2`、`3` 加入网桥接口 `1`。仅执行 `addif` 后，桥接仍处于禁用状态，因为网桥接口默认未启动；`net iface up` 才会启用桥接。

在主机使用 Wireshark 同时监视 `zeth0`、`zeth1`，应能在两个接口上看到相同网络流量。接口索引不是固定值，实际环境中的网桥与以太网接口编号可能不同，应先根据 `net iface` 的结果确认。

## 16.4\_关闭桥接并移除接口

将网桥接口置为关闭状态（Down）即可禁用桥接；再使用 `delif` 从网桥移除以太网接口。在 Zephyr shell 执行：

```text
net iface down 1
net bridge delif 1 2 3
```


<a id="ethernet-bridge-with-native-sim-board"></a>
<a id="networking-with-native-sim-eth-bridge"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：多个Zephyr实例联网](P015_多个Zephyr实例联网.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：监视网络流量](P017_监视网络流量.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P015_多个Zephyr实例联网.md) · [返回大纲](大纲.md) · [下一章](P017_监视网络流量.md)

</details>

<!-- reading-navigation:end -->
