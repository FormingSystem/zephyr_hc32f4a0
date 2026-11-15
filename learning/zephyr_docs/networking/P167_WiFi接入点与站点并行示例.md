---
id: learning.zephyr-docs.networking.page-167
title: WiFi接入点与站点并行示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/wifi/apsta_mode/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第167章\_WiFi接入点与站点并行示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/wifi/apsta_mode/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

Wi-Fi 开发板的 AP-STA 模式使设备能够同时作为接入点（Access Point，AP）和站点（Station，STA）。本示例展示该模式的配置与使用，涉及两个接口：

- AP 接口（`AP mode`）：配置并启用接入点，同时配置 DHCPv4 服务器，为接入的站点分配 IP 地址。
- STA 接口（`STA mode`）：提供路由器的服务集标识符（Service Set Identifier，SSID）和预共享密钥（Pre-Shared Key，PSK）。

示例先启用 AP，再启用 STA。驱动检查 AP 是否已启用；若已启用，则把开发板切换到 AP-STA 模式，同时支持两种角色，并尝试连接所给 SSID／PSK 指定的接入点。

官方[示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/wifi/apsta_mode)可用于对照接口配置、连接事件和 DHCPv4 处理。

## 2. 要求（Requirements）

原文指出，本例应能够在常见 ESP32-DevKitC 开发板上运行，无需额外硬件。通过修改示例 `prj.conf` 中的 [`CONFIG_WIFI_USAGE_MODE_STA_AP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WIFI_USAGE_MODE_STA_AP) 启用或关闭 AP-STA 模式。

原文称 AP-STA 模式默认关闭。

> 源码对照：当前官方[prj.conf](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/apsta_mode/prj.conf)已明确设置 `CONFIG_WIFI_USAGE_MODE_STA_AP=y`，与原文“默认关闭”不一致。当前[Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/apsta_mode/Kconfig)分别定义本设备接入点的 [`CONFIG_WIFI_SAMPLE_AP_SSID`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/apsta_mode/Kconfig)／[`CONFIG_WIFI_SAMPLE_AP_PSK`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/apsta_mode/Kconfig)，以及设备作为 STA 要连接的路由器的 [`CONFIG_WIFI_SAMPLE_SSID`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/apsta_mode/Kconfig)／[`CONFIG_WIFI_SAMPLE_PSK`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/wifi/apsta_mode/Kconfig)；这两组凭据属于不同连接角色，需按自己的测试网络设置。此处描述官方示例，不表示本仓库 HC32 开发板已有 Wi-Fi 支持。

## 3. 构建、烧写与运行

前提是已具备 Zephyr 构建环境及 ESP32 目标所需依赖，并连接所选开发板。从读者自己的 Zephyr 源码根目录执行原文命令：

```sh
west build -b esp32_devkitc/esp32/procpu samples/net/wifi/apsta_mode
west flash
```

`west build` 生成固件，`west flash` 将固件写入所选开发板。随后查看设备串口日志，判断两个角色是否启动和连接成功；若连接失败，先核对两组 SSID／PSK、目标板及最终配置，再比较事件日志。

## 4. 示例输出（Sample Output）

以下为原文提供的输出，保留版本串、时间戳、地址和全部日志；它不代表本次翻译已执行硬件测试。

```console
*** Booting Zephyr OS build v3.7.0-rc3-104-gd1e5c5b3f9b7 ***
[00:00:05.171,000] <inf> MAIN: Turning on AP Mode
[00:00:05.172,000] <dbg> net_dhcpv4_server: net_dhcpv4_server_start: Started DHCPv4 server, address pool:
[00:00:05.172,000] <dbg> net_dhcpv4_server: net_dhcpv4_server_start:     0: 192.168.4.11
[00:00:05.172,000] <dbg> net_dhcpv4_server: net_dhcpv4_server_start:     1: 192.168.4.12
[00:00:05.172,000] <dbg> net_dhcpv4_server: net_dhcpv4_server_start:     2: 192.168.4.13
[00:00:05.172,000] <dbg> net_dhcpv4_server: net_dhcpv4_server_start:     3: 192.168.4.14
[00:00:05.172,000] <inf> MAIN: DHCPv4 server started...

[00:00:05.350,000] <inf> MAIN: AP Mode is enabled. Waiting for sta to connect ESP32-AP
[00:00:05.350,000] <inf> MAIN: Connecting to SSID: ZIN-Dummy

[00:00:09.498,000] <inf> net_dhcpv4: Received: 192.168.43.44
[00:00:09.499,000] <inf> MAIN: Connected to ZIN-Dummy
[00:00:32.739,000] <inf> MAIN: station: 7C:50:79:17:89:19 joined
[00:00:32.832,000] <dbg> net_dhcpv4_server: dhcpv4_handle_discover: DHCPv4 processing Discover - reserved 192.168.4.11
[00:00:33.839,000] <dbg> net_dhcpv4_server: dhcpv4_handle_request: DHCPv4 processing Request - allocated 192.168.4.11
```

日志先显示 AP 模式启动和 DHCPv4 地址池 `192.168.4.11` 至 `192.168.4.14`，随后 AP 等待客户端，STA 尝试连接 `ZIN-Dummy` 并获得 `192.168.43.44`。最后显示另一站点加入本设备的 AP，并获得 `192.168.4.11`。这些事件对应设备同时参与的两个不同网络；原文并未由此证明它提供跨接口路由或网络地址转换（Network Address Translation，NAT）。

## 5. 另见（See Also）

- [Wi-Fi 管理（Wi-Fi Management）](https://docs.zephyrproject.org/latest/doxygen/html/group__wifi__mgmt.html)。
- [DHCPv4 服务器（DHCPv4 Server）](https://docs.zephyrproject.org/latest/doxygen/html/group__dhcpv4__server.html)。


<a id="wifi-ap-sta-mode"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-flashing-and-running"></a>
<a id="sample-output"></a>
<a id="see-also"></a>

[上一章](P166_WiFi示例目录.md) · [返回大纲](大纲.md) · [下一章](P168_通过低功耗蓝牙配置WiFi.md)
