---
id: learning.zephyr-docs.networking.page-13
title: ArmFVP用户网络
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/armfvp_user_networking_setup.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_ArmFVP用户网络

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/armfvp_user_networking_setup.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 13.1\_简介（Introduction）

本页为在 Zephyr 中使用 Arm 固定虚拟平台（Fixed Virtual Platform，FVP）的用户模式网络（User Mode Networking）提供起点。

用户模式网络模拟一个内置 IP 路由器（Router）和 DHCP 服务器，在客户机（Guest）与主机（Host）之间转发 TCP、UDP 流量。它借助主机的用户模式套接字层（Socket Layer）与其他主机通信，因此无需管理员权限，也无需在运行模型的主机上安装独立驱动，就能使用多种 IP 网络服务。

Arm FVP 默认使用 `172.20.51.0/24` 网络，网关地址为 `172.20.51.254`。该网关也充当客户机操作系统（Guest Operating System，GOS）的 DHCP 服务器，使客户机自动获得 `172.20.51.1`。

更多信息参见 [Arm 用户模式网络说明](https://developer.arm.com/documentation/100964/latest/Introduction-to-Fast-Models/User-mode-networking)。这些地址是官方模型的默认网络示例，与读者存放仓库的位置无关。

## 13.2\_在 Zephyr 中使用（Using Arm FVP User Mode Networking with Zephyr）

Arm FVP 用户模式网络可以在应用中启用，主机系统不需要额外网络配置。[DHCPv4 客户端（DHCPv4 client）示例](P035_DHCPv4客户端示例.md#dhcpv4-client)已启用此功能，可作为使用入口。

## 13.3\_限制（Limitations）

- 支持 IP 上的 TCP 和 UDP，不支持 ICMP，因此不能使用 `ping`。
- 不支持将主机的 UDP 端口转发给模型。
- DHCP 只能用于私有网络（Private Network）内部。
- 外部发起的入站连接只能通过将主机 TCP 端口映射到模型来建立。原文指出，这是通过网络地址转换（Network Address Translation，NAT）提供主机连接的实现共有的约束。
- 需要特权源端口（Privileged Source Port）的操作不能工作，例如默认配置下的 NFS。
- 设置失败或参数语法错误时，不会报告错误。


<a id="networking-with-arm-fvp-user-mode"></a>
<a id="networking-with-armfvp"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="introduction"></a>
<a id="using-arm-fvp-user-mode-networking-with-zephyr"></a>
<a id="limitations"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：QEMU与IEEE802154联网](P012_QEMU与IEEE802154联网.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：USB设备联网](P014_USB设备联网.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P012_QEMU与IEEE802154联网.md) · [返回大纲](大纲.md) · [下一章](P014_USB设备联网.md)

</details>

<!-- reading-navigation:end -->
