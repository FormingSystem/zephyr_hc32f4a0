---
id: learning.zephyr-docs.networking.page-11
title: QEMU用户网络
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/qemu_user_setup.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第11章\_QEMU用户网络

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/qemu_user_setup.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

本页面向希望在Zephyr中使用QEMU SLIRP用户网络（User Networking）的读者。

## 11.1\_工作原理

SLIRP是网络后端（Network Backend），在QEMU内提供完整TCP/IP协议栈，实现带NAT的虚拟网络。因不依赖额外主机网络配置，设置较简单。

QEMU默认使用 `10.0.2.X/24` 网络，网关位于 `10.0.2.2`。发往主机网络的流量都经过该网关，它按QEMU命令行参数过滤分组。网关同时充当客户机操作系统（Guest Operating System，GOS）的DHCP服务器，从 `10.0.2.15` 起自动分配IP地址。更多说明见[QEMU用户网络文档](https://wiki.qemu.org/Documentation/Networking#User_Networking_.28SLIRP.29)。

## 11.2\_在Zephyr中启用

通过Kconfig启用用户网络：

```kconfig
CONFIG_NET_QEMU_USER=y
```

启用后，QEMU启动使用SLIRP。默认情况下，Zephyr只启用用户网络，不额外传入参数。原文据此称客户机只能与QEMU网关通信，发往主机的数据会被QEMU丢弃。

用户网络通常接受多类参数，包括：

- 主机／客户机端口转发（Port Forwarding）信息，原文说明需用它建立双方通信通道。
- 网络地址，例如替代默认 `10.0.2.X` 网络。
- 用户指定的DHCP服务器地址。
- ID及其他信息。

各用途差异很大，难以提供适合所有场景的默认值，因此Zephyr让用户按需求通过Kconfig字符串补充：

```kconfig
CONFIG_NET_QEMU_USER_EXTRA_ARGS="net=192.168.0.0/24,hostfwd=tcp::8080-:8080"
```

该字符串原样追加到QEMU命令行，所以其中的问题只会由QEMU报告。此例将网络改为 `192.168.0.0/24`；原文称将主机8080端口的TCP数据转发到客户机8080端口，“反向亦然”。

> 译注：本轮Zephyr启动脚本默认构造 `user,id=n1`，并未加入禁止外部访问的 `restrict=on`。QEMU当前官方说明区分客户机主动向外通信与主机主动连接客户机；不能把“没有hostfwd”理解为客户机只能访问网关。`hostfwd` 建立主机监听端口到客户机端口的入站映射；已有连接的返回数据不等于另建一个反向端口映射。核对依据见[QEMU调用文档](https://www.qemu.org/docs/master/system/invocation.html)和[来源记录](../SOURCES.md)。

## 11.3\_限制

若只需从客户机访问网页，没有其他特别网络需求，SLIRP是一个合适选择。原文列出以下限制：

- 开销较大，性能较差。
- 主机和外部网络不能直接访问客户机。
- 通常不能使用ICMP，因此客户机内不能使用ping。
- 端口映射必须在QEMU启动前定义，因此使用动态生成端口的客户端不能与外部网络通信。
- 原文引用[历史SLIRP问题1724590](https://bugs.launchpad.net/qemu/+bug/1724590)，称客户机发出的所有IPv6分组被过滤，因此用户网络不支持IPv6。

> 译注：这些限制包含旧版本或过宽的描述。当前QEMU官方用户网络选项支持 `ipv4`、`ipv6`，未显式指定时两者默认启用，因此不能把历史缺陷当作所有版本都不支持IPv6的结论；端口映射也主要约束主动进入客户机的连接。ICMP能力与主机及版本有关，应按所用QEMU确认。本轮未运行连通性测试，原文限制与更新依据分别保留。


> 源码跟踪译注：本轮网络后端与设备参数的拼接依据为[官方 net_nic.cmake](https://github.com/zephyrproject-rtos/zephyr/blob/main/cmake/emu/qemu/net_nic.cmake)。这是随 `main` 变化的官方链接，已读取的文件摘要保存在[来源记录](../SOURCES.md)。


<a id="networking-with-qemu-user"></a>
<a id="networking-with-user-qemu"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="introduction"></a>
<a id="using-slirp-with-zephyr"></a>
<a id="limitations"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：QEMU以太网联网](P010_QEMU以太网联网.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：QEMU与IEEE802154联网](P012_QEMU与IEEE802154联网.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P010_QEMU以太网联网.md) · [返回大纲](大纲.md) · [下一章](P012_QEMU与IEEE802154联网.md)

</details>

<!-- reading-navigation:end -->
