---
id: learning.zephyr-docs.board-samples.page-110
title: WiFi网状网络IP通信
kind: reference
status: maintained
domains: [zephyr, boards, samples]
source_url: https://docs.zephyrproject.org/latest/samples/boards/espressif/wifi_mesh_ip/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="wifi-mesh-ip"></a>

# 第110章\_Wi-Fi 网状网络 IP 通信（Wi-Fi Mesh IP）

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/boards/espressif/wifi_mesh_ip/README.html)。快照读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

[在 GitHub 浏览源码（Browse source code on GitHub）](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/boards/espressif/wifi_mesh_ip/README.rst/..)

<a id="overview"></a>

## 110.1 概述（Overview）

本示例在自组织 Wi-Fi 网状网络上传输 IP，使每个节点都能直接运行未经修改的单播 IPv4 套接字；网状传输不支持的内容见限制说明。它建立在 Wi-Fi 网状网络（Wi-Fi Mesh）示例之上：节点组成相同的自组织网络，同时启用 AP 和 Station 模式，按路由器可达性选举根节点；本示例则在网状传输上增加 IP 层。 相关链接：[限制（Limitations）](#limitations)；[Wi-Fi 网状网络 IP 通信（Wi-Fi Mesh IP）](P109_WiFi网状网络.md#wifi-mesh)。

Wi-Fi 驱动通过 `CONFIG_WIFI_ESP32_MESH_IP` 提供一个小型以太网接口，把 Zephyr 网络协议栈接到网状网络上：发出的数据包经网状发送 API 传输，收到的网状帧交给协议栈。所有 IP 层功能都由 Zephyr 原生子系统提供。

> 译注——两条接收路径：当前 esp_wifi_mesh.h 在 CONFIG_WIFI_ESP32_MESH_IP 启用时不声明原始 esp_wifi_mesh_send／recv 接口，源码说明两者会争用同一接收队列，因此按构建配置互斥。IP 示例使用驱动提供的以太网传输路径，不能简单把前一示例的原始收发循环叠加进来。

根节点在网状接口上为子节点提供 DHCP，子网为 192.168.4.0/24，并通过 NAT 把它们的流量转换后从 Station 接口转发出去。子节点经网状网络从根节点取得地址，例如 192.168.4.2，并安装指向根节点的默认路由。根节点的 Station 从路由器取得上行地址租约后，子节点即可通过根节点 NAT 访问外部网络。

> 译注——两侧地址与路由：192.168.4.0/24 是示例内网，根节点为 .1、DHCP 池从 .2 开始；根节点 Station 的地址由上游路由器另行分配。上游网络不要与该内网重叠；需要调整时修改 mesh_bridge.c 中对应子网定义。该文件为 TCP、UDP、ICMP 分别添加 NAT 规则和网状子网路由，而不是仅配置一个网关地址。

网状传输不能承载子节点为解析根网关地址而发送的地址解析协议（Address Resolution Protocol，ARP）广播，因此根节点周期性发送免费 ARP（Gratuitous ARP），再由网状网络转送给每个子节点。刚加入的子节点可能需要等待最多 `CONFIG_NET_ARP_GRATUITOUS_INTERVAL` 秒，直到下一条免费 ARP 到来，才能解析上行网关并开始传输外部流量。

> 译注——等待时间：prj.conf 将 CONFIG_NET_ARP_GRATUITOUS_INTERVAL 设为 10 秒。子节点获得 DHCP 地址和学会网关 MAC 是不同阶段；首次有地址却暂时不能上网时，还要检查根节点的上行租约、ARP、路由与NAT状态，不能把“拿到地址”当作全部链路已就绪。

<a id="limitations"></a>

### 110.1.1 限制（Limitations）

IP-over-mesh 传输只支持单播 IPv4。以下限制属于网状传输的特性，并非缺陷，但决定了哪些功能可在其上运行：

- 不支持多播（Multicast）。网状网络没有多播原语，因此 IPv4 多播、IPv6 邻居发现、mDNS 和基于多播的服务发现都不能穿过该网状网络。

- 广播（Broadcast）通过向每个已知节点分别发送单播来模拟，按路由表规模需要 O(N) 次发送；这里只用于前述免费 ARP 网关解决方案，不能扩展为通用广播传输。

- 仅支持 IPv4。寻址、DHCP 和根节点 NAT 都使用 IPv4，没有 IPv6 通路。

- 最大传输单元（Maximum Transmission Unit，MTU）较小，而且不分片。网状接口 MTU 小于普通以太网链路；大于网状负载上限的帧会被拒绝，而非分片，所以必须遵守路径 MTU。

> 译注——实际 MTU：驱动按 MESH_MPS 减去以太网头大小设置网状接口 MTU，发送队列中的帧也受此大小约束。不要默认采用普通以太网的 1500 字节 IP MTU，也不要把队列暂存误认为自动分片；应以所用库和当前接口的实际值检查应用负载。

因此，未经修改的单播 IPv4，包括 TCP 和 UDP，可跨网状网络运行；依赖多播、广播或 IPv6 的功能则不能。

<a id="requirements"></a>

## 110.2 硬件与配置要求（Requirements）

- 至少两块受支持的 ESP32 开发板，可采用 esp32、esp32s2、esp32s3、esp32c3、esp32c5 或 esp32c6。ESP32-C2 和 ESP32-H2 不提供网状网络库。

- 一台可以访问互联网的 2.4 GHz 路由器。根节点关联到该路由器，并转发子节点到外部网络的流量。

<a id="memory"></a>

### 110.2.1 内存（Memory）

当前配置按内存需求最大的根节点设置：包括直接子节点使用的 Wi-Fi 缓冲池，以及子网所需的 DHCP 服务器、NAT 和路由状态。由于任何节点都可能被选为根节点，各板烧录同一镜像。

对 ESP32 和 ESP32-S2 等 RAM 预算较小、无法容纳该配置的 SoC，应缩减网状网络的子节点数量及 Wi-Fi 缓冲池，见 `boards/` 下的板级文件。如此配置的节点作为叶子节点（Leaf child）运行。

> 译注——内存配置与角色：本次两块板的 .conf 将堆降到 98304 字节、最大子连接数设为 1，并缩小 Wi-Fi 缓冲池；默认 prj.conf 的堆为 131072 字节。这些文件没有自动设置 FORCE_CHILD，也没有关闭 DHCP 服务器与 NAT。“作为叶子使用”是部署要求，不能由减小内存配置推断已强制成为子节点。

设置 `CONFIG_NET_DHCPV4_SERVER=n` 和 `CONFIG_NET_IPV4_NAT=n` 会完全去掉根节点转发功能，并释放其所需内存。这样的节点不能为网状子网提供服务，因此仅在保证其他节点担任根节点时才应使用该构建；若它被选为根节点，会报告错误。

<a id="building-and-running"></a>

## 110.3 构建与运行（Building and Running）

> 译注——执行前提：主机命令在读者自己的 Zephyr 源码根目录，用 UCRT64 Bash 或 Linux Bash 执行；先按[入门指南](../getting_started/大纲.md)准备模块、工具链和目标板。网络示例须按本文准备对端、信道与路由器；加密示例须先满足引导程序前提。设备 Shell 命令与主机命令分别执行，日志仅为原文预期输出。本次未构建、烧录、配网、改写密钥或eFuse。

```text
west build -b esp32c6_devkitc/esp32c6/hpcore samples/boards/espressif/wifi_mesh_ip
west flash
```

在 `src/main.c` 中，通过运行时调用 `esp_wifi_mesh_set_config()` 配置网状网络信道和路由器凭据，见 `esp_wifi_mesh.h`。默认路由器凭据是 `myssid`／`mypassword` 占位值，必须改为实际路由器的信息；保留占位值的节点找不到该网络，会持续搜索父节点。信道应与路由器一致。将同一镜像烧录到每块开发板。

根节点选举由路由器可达性驱动，因此都处于路由器范围内的开发板会各自成为根节点；只有超出路由器范围的节点才以子节点身份加入网状网络。所有板都靠近路由器进行台架测试时，应为预期子节点启用 `CONFIG_WIFI_ESP32_MESH_FORCE_CHILD=y`，让它们连接到选出的根节点。

<a id="sample-output"></a>

## 110.4 示例输出（Sample Output）

根节点建立上行链路和 NAT，子节点则通过网状网络获取地址：

> 译注——成功日志的边界：mesh_bridge_setup_root() 对路由、DHCP服务器和NAT规则添加失败分别记录错误，但最后仍打印 DHCP + NAT up。因此应先检查前面的错误和实际接口状态，再用子节点的设备 Shell 执行下方 net ping；串口提示符不是主机命令。本次没有连接网络或发送该测试流量。

```text
<inf> wifi_mesh_ip: Wi-Fi mesh starting (router SSID "myssid")
<inf> wifi_mesh_ip: parent connected, layer 1 (root)
<inf> wifi_mesh_ip: mesh root IP: gateway 192.168.4.1, DHCP + NAT up
<inf> wifi_mesh_ip: child connected
<inf> wifi_mesh_ip: root external network reachable
<inf> wifi_mesh_ip: child got IP 192.168.4.2 over mesh
```

子节点取得地址后，从其 Shell 向一个公网主机发送 ping，确认它能通过根节点 NAT 访问外部网络：

```text
uart:~$ net ping 1.1.1.1
```

> 译注——源码入口：[src/main.c](../../../samples/boards/espressif/wifi_mesh_ip/src/main.c)；[src/mesh_bridge.c](../../../samples/boards/espressif/wifi_mesh_ip/src/mesh_bridge.c)；[prj.conf](../../../samples/boards/espressif/wifi_mesh_ip/prj.conf)；[boards/esp32_devkitc_procpu.conf](../../../samples/boards/espressif/wifi_mesh_ip/boards/esp32_devkitc_procpu.conf)；[boards/esp32s2_devkitc.conf](../../../samples/boards/espressif/wifi_mesh_ip/boards/esp32s2_devkitc.conf)；[include/zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h](../../../include/zephyr/drivers/wifi/esp_wifi/esp_wifi_mesh.h)；[drivers/wifi/esp32/src/esp_wifi_mesh.c](../../../drivers/wifi/esp32/src/esp_wifi_mesh.c)；[drivers/wifi/esp32/src/esp_wifi_mesh_netif.c](../../../drivers/wifi/esp32/src/esp_wifi_mesh_netif.c)。本地源码使用相对链接；上游快照及官方补充说明的摘要见来源记录，本地版本可能不同。

对应官方文档源码：[samples/boards/espressif/wifi_mesh_ip/README.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/samples/boards/espressif/wifi_mesh_ip/README.rst)。

> 译注——源码跟踪：本仓库[对应源码](../../../samples/boards/espressif/wifi_mesh_ip/README.rst)可用于对照，版本可能与网页不同。本批仅翻译和核对文档，未构建、烧录、运行无线通信或改写密钥与eFuse。

[上一章](P109_WiFi网状网络.md) · [返回大纲](大纲.md) · [下一章](P111_Espressif示例目录.md)
