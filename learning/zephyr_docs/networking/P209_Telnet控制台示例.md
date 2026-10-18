---
id: learning.zephyr-docs.networking.page-209
title: Telnet控制台示例
kind: reference
status: maintained
domains: [zephyr, networking, documentation]
source_url: https://docs.zephyrproject.org/latest/samples/net/telnet/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="telnet-console"></a>

# 第209章\_Telnet控制台示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/telnet/README.html)。读取日期：2026-10-14；保存的latest页面及HTML摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 209.1 概述（Overview）

此应用在默认网络接口上设置IPv4／IPv6地址。内核透明地启动Telnet控制台服务、Shell，以及`net`和`kernel`两个Shell模块。运行后，可通过Telnet客户端从网络连接目标设备。

<a id="requirements"></a>

## 209.2 要求（Requirements）

先阅读[与QEMU联网（Networking with QEMU）](P009_QEMU联网概览.md#networking-with-qemu)。

<a id="building-and-running"></a>

## 209.3 构建与运行（Building and Running）

<a id="qemu-x86"></a>

### 209.3.1 QEMU x86（QEMU x86）

以下步骤说明如何在Linux主机的QEMU中运行示例；原文设定该主机连接到提供动态主机配置协议（Dynamic Host Configuration Protocol，DHCP）服务的网络。使用QEMU测试前，按照[与QEMU联网](P009_QEMU联网概览.md#networking-with-qemu)指南准备环境。

在QEMU中运行Zephyr的`samples/net/telnet`应用：

```sh
west build -b qemu_x86 samples/net/telnet
west build -t run
```

启动后，应能看到类似以下IP地址信息：

```text
[Setup] [INF] main: Starting Telnet sample
[Setup] [INF] setup_ipv4: IPv4 address: 192.0.2.1
[Setup] [INF] setup_ipv6: IPv6 address: 2001:db8::1
```

此时QEMU来宾系统（Guest）已经运行。从Linux主机连接Telnet控制台：

```console
$ telnet 192.0.2.1
Telnet escape character is '^]'.
Trying 192.0.2.1...
Connected to 192.0.2.1.
Escape character is '^]'.
```

按回车后出现Shell提示符，可输入命令，例如`help`。

<a id="freedom-k64f-board"></a>

### 209.3.2 Freedom-K64F开发板（Freedom-K64F Board）

以下步骤说明如何在[Freedom-K64F开发板](https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#frdm_k64f)上运行。原文说明，与QEMU不同，该开发板的IPv4配置依赖DHCPv4；确实需要静态IPv4地址时，可以修改`prj_frdm_k64f.conf`。

构建、烧录和串口日志的详细说明见[Freedom-K64F开发板文档](https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#frdm_k64f)。将[Freedom-K64F](https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#frdm_k64f)通过以太网线连接到提供DHCPv4地址配置的局域网；自行建立DHCP服务器不在本README范围内。

构建Zephyr的`samples/net/telnet`应用：

```sh
west build -b frdm_k64f samples/net/telnet
```

按照上述[Freedom-K64F](https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#frdm_k64f)开发板文档烧录生成的Zephyr二进制文件。在主机打开连接开发板的串口控制台：

```console
$ sudo screen /dev/ttyACM0 115200
```

将以太网线插入[Freedom-K64F](https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#frdm_k64f)，复位开发板，控制台首先应出现：

```text
[dev/eth_mcux] [INF] eth_0_init: Enabled 100M full-duplex mode.
[dev/eth_mcux] [DBG] eth_0_init: MAC 00:04:9f:69:c7:36
shell> [Setup] [INF] main: Starting Telnet sample
[Setup] [INF] setup_dhcpv4: Running dhcpv4 client...
[Setup] [INF] setup_ipv6: IPv6 address: 2001:db8::1
```

如果DHCPv4客户端成功，随后很快会看到类似信息：

```text
[Setup] [INF] ipv4_addr_add_handler: IPv4 address: 192.168.0.21
[Setup] [INF] ipv4_addr_add_handler: Lease time: 86400 seconds
[Setup] [INF] ipv4_addr_add_handler: Subnet: 255.255.255.0
[Setup] [INF] ipv4_addr_add_handler: Router: 192.168.0.1
```

结果取决于本地网络。此时应可以通过网络连接Telnet；在Linux主机输入：

```console
$ telnet 192.168.0.21
Telnet escape character is '^]'.
Trying 192.168.0.21...
Connected to 192.168.0.1.
Escape character is '^]'.
```

连接建立后，与UART控制台一样，可以输入命令，并通过Telnet客户端取得输出。

> 译注——当前配置与原日志：原文的`prj_frdm_k64f.conf`属于旧说明；当前所核对示例的`prj.conf`设置`CONFIG_NET_DHCPV4=n`，使用静态地址，`tests.yaml`也未为该板附加原文所述DHCP配置。因此不要将旧DHCP流程视为当前默认行为，应先确认实际加载的配置。最后一段日志尝试连接`192.168.0.21`却显示连接到`192.168.0.1`，这是原示例中的不一致，实际应使用开发板取得的地址。上述日志保持原样，未作为本次实测结果。

<a id="wi-fi"></a>

### 209.3.3 Wi-Fi（Wi-Fi）

可通过[Wi-Fi配置片段（Wi-Fi snippet）](../snippets/P027_WiFi_IPv4配置片段.md#snippet-wifi-ipv4)为此示例启用IPv4 Wi-Fi支持。

<a id="see-also"></a>

## 209.4 另请参阅（See also）

[命令行Shell（Shell）](../shell_core_reference/P001_Shell核心接口.md)、[网络核心库（Network Core Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html)、[网络接口抽象层（Network Interface abstraction layer）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html)、[网络管理（Network Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html)。


> 译注——实现依据：[samples/net/telnet/prj.conf](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/telnet/prj.conf)、[samples/net/telnet/tests.yaml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/telnet/tests.yaml)、[samples/net/telnet/src/telnet.c](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/telnet/src/telnet.c)。以上为本次核对的官方来源；分支内容可能继续变化，保存快照的摘要见[来源记录](../SOURCES.md)。下方本仓库相对链接用于版本对照。

对应官方文档源码：[samples/net/telnet/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/net/telnet/README.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../samples/net/telnet/README.rst)可用于对照，版本可能与网页不同。源码跟踪和实现依据不绑定作者机器目录；项目环境与实验路线另见[项目实验补充](../../zephyr_project_notes/README.md)。


[上一章](P208_远程系统日志示例.md) · [返回大纲](大纲.md) · [下一章](P210_虚拟网络接口示例.md)
