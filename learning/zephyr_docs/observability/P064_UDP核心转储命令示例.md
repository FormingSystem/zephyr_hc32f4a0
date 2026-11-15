---
id: learning.zephyr-docs.observability.dbsample-2
title: UDP核心转储命令示例
kind: reference
status: maintained
domains: [zephyr, observability]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/debug/coredump_udp_demos/demo_shell/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="coredump-udp-demo-shell"></a>

# 第64章\_UDP核心转储命令示例

原文：[UDP coredump via shell](https://docs.zephyrproject.org/latest/samples/subsys/debug/coredump_udp_demos/demo_shell/README.html)。读取日期：2026-10-13，`latest`。

## 64.1\_概述

Zephyr 命令解释器（Shell）持续运行在串行控制台（Serial Console）上。运行 `coredump_crash` 会使开发板发生故障；启用 `CONFIG_DEBUG_COREDUMP_BACKEND_LOGGING_UDP` 后，核心转储（Core Dump）字节流同时以 `#CD:` 十六进制文本输出到通用异步收发器（Universal Asynchronous Receiver/Transmitter，UART），并以分帧的用户数据报协议（User Datagram Protocol，UDP）数据发送到 `CONFIG_DEBUG_COREDUMP_LOGGING_UDP_HOST`。

目标地址采用 `net_ipaddr_parse()` 接受的语法，例如 `192.0.2.2`、`192.0.2.2:17777`、`[2001:db8::1]:17777`；省略端口时使用默认端口 `17777`。

开发板叠加配置（Overlay）`boards/versalnet_apu.conf` 设置了实验室环境的静态网际协议第4版（Internet Protocol version 4，IPv4）地址，应按自己的实验环境调整。网络及 UDP 核心转储选项位于 `prj.conf`，应用叠加配置之前的默认地址属于 `192.0.2.x`。

另见[核心转储](P002_核心转储.md)和[核心转储 UDP 日志后端源码](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/debug/coredump/coredump_backend_logging_udp.c)。

## 64.2\_构建

```shell
west build -b versalnet_apu samples/subsys/debug/coredump_udp_demos/demo_shell
```

---

[上一章：断言示例](P063_断言示例.md) · [下一章：调试监视器示例](P065_调试监视器示例.md) · [返回大纲](大纲.md)
