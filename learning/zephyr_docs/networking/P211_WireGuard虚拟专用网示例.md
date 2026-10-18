---
id: learning.zephyr-docs.networking.page-211
title: WireGuard虚拟专用网示例
kind: reference
status: maintained
domains: [zephyr, networking, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/net/wireguard/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->


# 第211章\_WireGuard虚拟专用网示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/wireguard/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="wireguard-vpn"></a>

## 211.1 WireGuard虚拟专用网（Wireguard VPN）

面向`native_sim`目标，可以按以下方式构建WireGuard虚拟专用网（Virtual private network，VPN）演示，随后按该目标的运行方式启动：

```sh
west build -b native_sim samples/net/wireguard -- -DCONF_FILE=<config file to use>
```

在Linux GNOME桌面环境中，向构建命令加入`-DCONFIG_NATIVE_UART_AUTOATTACH_DEFAULT_CMD="\"gnome-terminal -- screen %s\""`参数可能会有帮助。

主机侧WireGuard VPN设置如下：

```console
$ cd tools/net-setup
$ ./net-setup.sh -c wireguard-vpn.conf
```

示例配置会建立以下结构。

**主机侧：**

- 创建普通`zeth`接口，地址为`192.0.2.2/24`；发往Zephyr的全部网络流量都经过它。
- VPN接口`zwg0`是WireGuard隧道端点，IPv4地址为`198.51.100.2`，IPv6地址为`2001:db8:100::2`。全部VPN流量经过这个接口。

**Zephyr侧（使用native_sim开发板时）：**

- `eth0`为主接口，地址为`192.0.2.1/24`，连接主机。
- `wg0`为虚拟接口。应用应通过它发送数据，以便网络流量经WireGuard VPN隧道传输。地址为`198.51.100.1/24`与`2001:db8:100::1/64`。
- `wg_ctrl`为VPN控制接口。全部VPN虚拟接口都附着于它；它自身没有IP地址。

主机侧网络接口示例：

```text
zeth: flags=4099<UP,BROADCAST,MULTICAST>  mtu 1500
      inet 192.0.2.2  netmask 255.255.255.0  broadcast 0.0.0.0
      inet6 2001:db8::2  prefixlen 64  scopeid 0x0<global>
      inet6 fe80::200:5eff:fe00:53ff  prefixlen 64  scopeid 0x20<link>
      ether 00:00:5e:00:53:ff  txqueuelen 1000  (Ethernet)
      RX packets 16  bytes 2356 (2.3 KB)
      RX errors 0  dropped 0  overruns 0  frame 0
      TX packets 27  bytes 2688 (2.6 KB)
      TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0

zwg0: flags=209<UP,POINTOPOINT,RUNNING,NOARP>  mtu 1420
      inet 198.51.100.2  netmask 255.255.255.255  destination 198.51.100.1
      inet6 2001:db8:100::2  prefixlen 128  scopeid 0x0<global>
      unspec 00-00-00-00-00-00-00-00-00-00-00-00-00-00-00-00  txqueuelen 1000  (UNSPEC)
      RX packets 3  bytes 364 (364.0 B)
      RX errors 0  dropped 0  overruns 0  frame 0
      TX packets 4  bytes 452 (452.0 B)
      TX errors 0  dropped 0 overruns 0  carrier 0  collisions 0
```

主机侧设置的路由：

```text
192.0.2.0/24 dev zeth proto kernel scope link src 192.0.2.2 linkdown
198.51.100.1 dev zwg0 proto kernel scope link src 198.51.100.2
2001:db8::/64 dev zeth proto kernel metric 256 linkdown pref medium
2001:db8::/64 dev zeth metric 1024 linkdown pref medium
2001:db8:100::2 dev zwg0 proto kernel metric 256 pref medium
2001:db8:100::/64 dev zwg0 metric 1024 pref medium
```

此示例会自动完成Zephyr网络设置，也可以手动配置WireGuard。手动配置时，先将以下Kconfig字符串选项清空：

```cfg
CONFIG_NET_SAMPLE_COMMON_VPN_PEER_IP_ADDR=""
CONFIG_NET_SAMPLE_COMMON_VPN_MY_ADDR=""
CONFIG_NET_SAMPLE_COMMON_VPN_ALLOWED_PEER_ADDR=""
CONFIG_NET_SAMPLE_COMMON_VPN_MY_PRIVATE_KEY=""
CONFIG_NET_SAMPLE_COMMON_VPN_PEER_PUBLIC_KEY=""
```

执行以下命令完成手动设置：

```sh
# Add IPv4 and IPv6 address to the VPN interface
net ipv4 add 2 198.51.100.1 255.255.255.0
net ipv6 add 2 2001:db8:100::1

# Setup our private key
net wg setup -k lmAIbJR8PQOpgJxmfOydBiDbexTMEKsjglZ1sj3kIjs= -i 2

# Setup peers
net wg add -k v/xiHtIDhnnMJV3SbqI+cChcSqfrU4zlhLUUbL1J8x4= -a 2001:db8:100::/64,198.51.100.0/24 -e 192.0.2.2:51820
```

VPN接口2应自动进入UP状态；如果Zephyr主机配置正确，应可以连接对端。

> 警告：演示中的IPv4与IPv6地址只能用于这些网络示例，不能用于实际网络。这些地址专供文档使用，不具备公网可路由性。不要在实际网络设备上使用示例WireGuard VPN配置文件里的私钥；需要时应生成新私钥。生成方法见[WireGuard快速入门（WireGuard Quick Start）](https://www.wireguard.com/quickstart/)。

> 译注——工作目录与接口编号：原命令中的`tools/net-setup`是旧目录写法。当前官方West清单把工具项目放在工作区的`tools/net-tools`，应在实际包含`net-setup.sh`和`wireguard-vpn.conf`的工具目录执行主机脚本。Zephyr Shell里的接口2也只是示例编号，应先根据`net iface`确认VPN接口。正文保留的私钥／公钥均为官方公开演示值，未读取或替换个人凭据；原路由中的`linkdown`是示例快照状态，不能作为隧道已连通的证据。

<a id="see-also"></a>

## 211.2 另请参阅（See also）

[BSD套接字兼容API（BSD Sockets compatible API）](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)。


> 译注——实现依据：[west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)、[samples/net/wireguard/Kconfig](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/wireguard/Kconfig)、[samples/net/wireguard/src/wg.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/wireguard/src/wg.c)、[net-tools/wireguard-vpn.conf](https://raw.githubusercontent.com/zephyrproject-rtos/net-tools/master/wireguard-vpn.conf)。以上为本次核对的官方来源；分支内容可能继续变化，保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库相对链接用于版本对照。

对应官方文档源码：[samples/net/wireguard/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/wireguard/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/net/wireguard/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。

> 译注——示例实现：仓库内的[main.c](../../../samples/net/wireguard/src/main.c)用于实现跟踪；它可能与上方网页及main分支版本不同。本文没有执行固件构建、烧录或接线实验。


[上一章](P210_虚拟网络接口示例.md) · [返回大纲](大纲.md) · [下一章](P212_网络示例目录.md)
