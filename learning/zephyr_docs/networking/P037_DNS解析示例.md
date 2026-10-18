---
id: learning.zephyr-docs.networking.page-37
title: DNS解析示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/dns_resolve/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第37章\_DNS解析示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/dns_resolve/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 37.1\_概览（Overview）

本应用先设置设备 IP 地址，再按用户配置解析不同主机名：启用 IPv4 时查询 `www.zephyrproject.org` 的 A 记录，启用 IPv6 时查询其 AAAA 记录，启用 mDNS 时解析 `zephyr.local`。

官方源码见 [`samples/net/dns_resolve`](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/dns_resolve)。

## 37.2\_前提（Requirements）

- 完成[与主机系统联网](P007_与主机系统联网.md#networking-with-host)所需设置。
- 准备 `screen` 终端仿真器（Terminal Emulator）或等效工具。
- 原文指出，多数没有以太网的开发板需要 ENC28J60 以太网模块。
- 准备 `dnsmasq`。原文所用版本如下，首行查询版本，后续是当时输出：

```text
dnsmasq -v
Dnsmasq version 2.76  Copyright (c) 2000-2016 Simon Kelley
```

## 37.3\_网络配置（Network Configuration）

打开目标平台的项目配置文件。原文以 [FRDM-K64F](https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#frdm_k64f) 的 `prj_frdm_k64f.conf` 为例。示例支持静态地址或 DHCPv4 地址，静态地址可写入项目配置，例如：

```kconfig
CONFIG_NET_CONFIG_MY_IPV6_ADDR="2001:db8::1"
CONFIG_NET_CONFIG_PEER_IPV6_ADDR="2001:db8::2"
```

两个 IPv6 地址分别对应运行 Zephyr 的 DNS 客户端和 DNS 服务器。

> 源码跟踪译注：本轮核对的官方 `samples/net/dns_resolve` 目录已使用 `prj.conf`，不存在原文提到的 `prj_frdm_k64f.conf`；其 `boards` 子目录也未提供该板的同名配置。应查看所用版本实际文件，不把旧文件名当作必需新建文件。当前配置入口为[官方 prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/dns_resolve/prj.conf)，来源与目录核对记录见[来源记录](../SOURCES.md)。

## 37.4\_DNS 服务器与 mDNS

测试时可使用 dnsmasq。其启动脚本位于官方 [net-tools](https://github.com/zephyrproject-rtos/net-tools) 项目；标准工作区可能已提供，也可从该项目取得。在 Linux 主机终端执行：

```sh
$ cd net-tools
$ sudo ./dnsmasq.sh
```

示例默认使用 Google 公共 DNS 服务器。要改用本地主机的 dnsmasq，编辑对应 `prj.conf`，更新服务器地址。使用常见测试地址时，原例为：

```kconfig
CONFIG_DNS_SERVER1="192.0.2.2:5353"
CONFIG_DNS_SERVER2="[2001:db8::2]:5353"
```

**原文注意（Note）**：DNS 默认端口是 `53`，但 net-tools 提供的 `dnsmasq.conf` 使用 `5353`，以便无需超级用户权限运行守护进程。原启动脚本示例仍写有 `sudo`，此处按原文保留。

如果启动出现端口占用错误：

```text
dnsmasq: failed to create listening socket for port 5353: Address already in use
```

原文要求在终端执行以下命令后重新启动 dnsmasq：

```sh
$ killall -s KILL dnsmasq
```

> 译注：该原命令会强制结束所有名为 dnsmasq 的进程。实际处理冲突时，应先确认谁占用了测试端口，停止自己为本实验启动的相应实例，避免把主机其他网络服务一起结束。本轮仅保存、翻译命令，没有执行它。

测试 mDNS 时，使用 net-tools 中的 Avahi 脚本：

```sh
$ cd net-tools
$ ./avahi-daemon.sh
```

以上 `cd net-tools` 从工具目录的父目录执行；如果终端已在该目录，无需再进入一次。

## 37.5\_LLMNR 响应器（LLMNR Responder）

若要让 Zephyr 回答 Windows 主机发出的链路本地组播名称解析（LLMNR）请求，可以设置：

```kconfig
CONFIG_NET_HOSTNAME_ENABLE=y
CONFIG_NET_HOSTNAME="zephyr-device"
CONFIG_DNS_RESOLVER=y
CONFIG_LLMNR_RESPONDER=y
```

Zephyr 必须具有主机名才能回答名称查询；这里的主机名不能包含点号。

## 37.6\_QEMU、FRDM-K64F 与 Wi-Fi

QEMU x86 测试按[QEMU 联网指南](P009_QEMU联网概览.md#networking-with-qemu)准备。

FRDM-K64F 构建与烧录从 Zephyr 源码根目录执行：

```sh
west build -b frdm_k64f samples/net/dns_resolve
west flash
```

板卡信息见[Freedom-K64F 官方文档](https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#frdm_k64f)。在 Linux 主机另开终端连接串口：

```sh
$ screen /dev/ttyACM0 115200
```

通过 `dmesg` 确认正确的 USB 设备节点，不必固定为 `/dev/ttyACM0`。固件加载到板上后，按 RESET 按钮启动。

通过 [Wi-Fi 配置片段（Snippet）](../snippets/P027_WiFi_IPv4配置片段.md#snippet-wifi-ipv4)可在示例中启用 IPv4 Wi-Fi 支持。

## 37.7\_相关接口

- [DNS 解析库](https://docs.zephyrproject.org/latest/doxygen/html/group__dns__resolve.html)。
- [网络管理 API](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html)。


<a id="dns-resolve"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="network-configuration"></a>
<a id="dns-server"></a>
<a id="llmnr-responder"></a>
<a id="qemu-x86"></a>
<a id="frdm-k64f"></a>
<a id="wi-fi"></a>
<a id="see-also"></a>

[上一章](P036_DHCPv6前缀委派示例.md) · [返回大纲](大纲.md) · [下一章](P038_SNTP客户端示例.md)
