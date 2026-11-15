---
id: learning.zephyr-docs.networking.page-173
title: OpenThread边界路由器
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/openthread/border_router/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第173章\_OpenThread边界路由器

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/openthread/border_router/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

本示例通过 OpenThread 和 Wi-Fi 命令行（Shell），在不同开发板上测试 Thread 协议及 Thread 边界路由器（Thread Border Router）功能。

官方[示例源码](https://github.com/zephyrproject-rtos/zephyr/tree/main/samples/net/openthread/border_router)提供配置和实现。

## 2. 构建与运行

先确认目标开发板和芯片同时支持 IEEE 802.15.4 与 Wi-Fi。原文称不同开发板和组合的配置文件位于 `shell` 目录；本示例实际路径为 `samples/net/openthread/border_router`，以下文件位于该目录：

| 文件 | 用途 |
| --- | --- |
| `prj.conf` | 通用配置。 |
| `overlay-ot-rcp-host-wifi-nxp.conf` | 启用 NXP 芯片上经 IMU 接口运行的 OpenThread 无线电协处理器主机（Radio Co-Processor Host，RCP Host），并启用 Wi-Fi。 |
| `overlay-webserver.conf` | 启用提供 REST API 的 HTTP Web 服务器。 |

在已配置 Zephyr 构建环境的主机上，从读者自己的 Zephyr 源码根目录构建：

```sh
west build -b <board to use> samples/net/openthread/border_router -- -DCONF_FILE=<config file to use>
```

`<board to use>` 和 `<config file to use>` 是需替换的目标及配置占位符。`CONF_FILE` 指定应用配置文件集合；只有显式列出的文件才属于这次指定集合，不应把只含补充设置的覆盖文件误当完整基础配置。

以 NXP RW612 FRDM 开发板运行 RCP Host 为例：

```sh
west build -b frdm_rw612 samples/net/openthread/border_router -- -DCONF_FILE="prj.conf overlay-ot-rcp-host-wifi-nxp.conf"
```

同一目标启用 Web 服务器时：

```sh
west build -b frdm_rw612 samples/net/openthread/border_router -- -DCONF_FILE="prj.conf overlay-ot-rcp-host-wifi-nxp.conf overlay-webserver.conf"
```

> 源码对照：当前[NXP Wi-Fi 覆盖配置](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/openthread/border_router/overlay-ot-rcp-host-wifi-nxp.conf)启用 IMU、固件加载器及 HDLC RCP 接口，并设置 `CONFIG_OPENTHREAD_MANUAL_START=y`。因此，构建成功或进入 Shell 不代表已经加入 Thread 网络；还需配置实际 Wi-Fi／Thread 网络并按设备交互结果判断。本页原文没有给出完整配网过程，本译文不把它补写成已验证实验。

## 3. Web 服务器（Web Server）

加入 `overlay-webserver.conf` 构建后，应用包含 HTTP Web 服务器，提供：

- Web 界面（Web Interface）：原文地址为 `http://<device-ip>:8080`，或通过多播 DNS（Multicast DNS，mDNS）访问 `http://zephyr-otbr:8080`。
- REST API：使用 JSON 的端点（Endpoints），用于 Thread 网络管理。REST 指表述性状态转移（Representational State Transfer）。

> 译注：`<device-ip>` 是设备实际地址，不是需原样输入的主机名。若使用 IPv6 地址作为 URL 主机部分，需要方括号。`zephyr-otbr` 的解析依赖主机和局域网的名称解析环境；当前[覆盖配置](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/openthread/border_router/overlay-webserver.conf)启用 mDNS／DNS-SD 并设置该主机名，实际也可能需通过 `.local` 名称访问。访问失败时先确认设备地址、网络可达性与所构建的 Web 功能。本次只核对文档和配置，没有启动服务器或改变主机网络。


<a id="openthread-border-router"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="web-server"></a>

[上一章](P172_OpenThread示例目录.md) · [返回大纲](大纲.md) · [下一章](P174_OpenThread的CoAP示例.md)
