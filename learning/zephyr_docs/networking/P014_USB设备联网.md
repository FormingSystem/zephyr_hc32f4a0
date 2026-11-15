---
id: learning.zephyr-docs.networking.page-14
title: USB设备联网
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/usbnet_setup.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第14章\_USB设备联网

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/usbnet_setup.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 14.1\_用途与基本设置（Basic Setup）

本页介绍如何让 Linux 主机与支持 USB 的设备上运行的 Zephyr 应用联网。开发板通过 USB 电缆连接主机，并向主机提供以太网接口（Ethernet Interface）。官方例子在支持的开发板上运行 Zephyr 源码发行版中的[高级回显服务器（Echo server）示例](P047_高级回显服务器示例.md#sockets-echo-server)。

要通过新建的以太网接口与 Zephyr 应用通信，需要为 Linux 主机配置 IP 地址和路由表（Routing Table）。插入 USB 电缆后，`cdc_ether` 驱动会使用设备提供的 MAC 地址注册新的以太网设备。

在 Linux 主机执行 `dmesg`，可检查设备是否创建、MAC 地址是否分配。原文的日志示例如下：

```text
cdc_ether 1-2.7:1.0 eth0: register 'cdc_ether' at usb-0000:00:01.2-2.7, CDC Ethernet Device, 00:00:5e:00:53:01
```

接着按下文配置地址。

## 14.2\_选择 IP 地址（Choosing IP Addresses）

主机接口应选择与 Zephyr 应用处于同一子网（Subnet）的地址。应用的 IP 地址通常写在项目配置文件中，也可以通过命令行查看。使用 PuTTY 等串口控制台（Serial Console）程序连接开发板，然后在 **Zephyr shell** 中执行 `net iface`：

```text
shell> net iface

Interface 0xa800e580 (Ethernet)
===============================
Link addr : 00:00:5E:00:53:00
MTU       : 1500
IPv6 unicast addresses (max 2):
        fe80::200:5eff:fe00:5300 autoconf preferred infinite
        2001:db8::1 manual preferred infinite
...
IPv4 unicast addresses (max 1):
        192.0.2.1 manual preferred infinite
```

上述原始输出中，开发板分配了一个 IPv4 地址和两个 IPv6 地址。可以根据板上的网络配置选择 IPv4 或 IPv6 连接。

下一步为 Linux 主机新出现的接口分配地址。原文主机的接口名称是 `enx00005e005301`。

> 译注：这个接口名是官方示例值，读者应替换为自己 Linux 主机实际创建的 USB 网络接口名；它不是固定的设备标识。下面 `#` 表示 root 终端提示符，`$` 表示普通用户提示符，复制命令时不包括提示符。接口地址、日志中的内存地址和 MAC 地址均为原文示例，并非作者机器目录。

## 14.3\_设置 IPv4 地址与路由（IPv4 Address and Routing）

在 Linux 主机的管理员终端执行。第一条添加地址，第二条启用接口，第三条指定到开发板所在子网的路由：

```sh
# ip address add dev enx00005e005301 192.0.2.2
# ip link set enx00005e005301 up
# ip route add 192.0.2.0/24 dev enx00005e005301
```

## 14.4\_设置 IPv6 地址与路由（IPv6 Address and Routing）

如使用 IPv6，在 Linux 主机的管理员终端执行对应配置：

```sh
# ip address add dev enx00005e005301 2001:db8::2
# ip link set enx00005e005301 up
# ip -6 route add 2001:db8::/64 dev enx00005e005301
```

## 14.5\_测试连接（Testing Connection）

在 Linux 主机通过 `ping` 访问开发板的 Zephyr IP 地址。原文命令与示例输出如下：

```text
$ ping 192.0.2.1
PING 192.0.2.1 (192.0.2.1) 56(84) bytes of data.
64 bytes from 192.0.2.1: icmp_seq=1 ttl=64 time=2.30 ms
64 bytes from 192.0.2.1: icmp_seq=2 ttl=64 time=1.43 ms
64 bytes from 192.0.2.1: icmp_seq=3 ttl=64 time=2.45 ms
...
```

收到回复说明对应地址可达。这里的时延和日志是官方示例，未作为本仓库实板测试结果；若没有回复，先返回前面的接口名称、地址选择和路由配置步骤检查。


<a id="usb-device-networking"></a>
<a id="usb-device-networking-setup"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="id5"></a>
<a id="basic-setup"></a>
<a id="choosing-ip-addresses"></a>
<a id="setting-ipv4-address-and-routing"></a>
<a id="setting-ipv6-address-and-routing"></a>
<a id="testing-connection"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：ArmFVP用户网络](P013_ArmFVP用户网络.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：多个Zephyr实例联网](P015_多个Zephyr实例联网.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P013_ArmFVP用户网络.md) · [返回大纲](大纲.md) · [下一章](P015_多个Zephyr实例联网.md)

</details>

<!-- reading-navigation:end -->
