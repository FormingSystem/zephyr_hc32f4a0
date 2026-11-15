---
id: learning.zephyr-docs.networking.page-134
title: SO_TXTIME定时发送示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/txtime/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第134章\_SO_TXTIME定时发送示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/txtime/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 1. 概述（Overview）

本示例是一个简单的 UDP 发送／接收应用。它设置 `SO_TXTIME` 套接字选项，要求以太网驱动在预期发送时刻（TX Time）发送数据。

应用要求开发板支持 PTP 时钟（PTP Clock）。`qemu_x86` 提供模拟 PTP 时钟；原文还列出 `frdm_k64f` 和 `sam_e70_xplained/same70q21`，并指出其他使用 `mcux` 或 `gmac` 以太网驱动的开发板也应可工作。

可[在 GitHub 查看官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/txtime/README.rst/..)。

通过 [`CONFIG_NET_SAMPLE_PACKET_INTERVAL`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/txtime/Kconfig) 控制相邻发包之间的等待时间。也可以设置 [`CONFIG_NET_SAMPLE_PACKET_TXTIME`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/txtime/Kconfig) 指定 TXTIME；该值作为相对于当前时间的偏移使用。

> 译注——单位和时钟来源：官方 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/txtime/Kconfig) 中，发包间隔以毫秒为单位，TXTIME 偏移以微秒为单位；两者默认都写作 `1000`，但实际分别表示 1 秒和 1 毫秒。比较大小时应先统一单位。官方 [`src/main.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/txtime/src/main.c) 将它们换算成纳秒，读取 PTP 时钟，并通过 `SCM_TXTIME` 辅助数据提供发送时间。拥有 PTP 时钟本身不代表驱动一定支持定时发送，示例还检查 `ETHERNET_TXTIME` 能力。

## 2. 构建和运行（Building and Running）

应用运行后开始发送 UDP 包。可以在对端启动 [net-tools](https://github.com/zephyrproject-rtos/net-tools) 项目中的 `echo-server`，接收这些包并把数据发回应用。

也可以启用 [`CONFIG_NET_SAMPLE_PACKET_SOCKET`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/txtime/Kconfig)，让应用创建 `AF_PACKET` 类型的套接字。此时不能使用上述 `echo-server` 作为对端。

按照[与主机系统联网](P007_与主机系统联网.md#networking-with-host)中的说明，可以在 `qemu_x86` 中构建、运行示例。

> 译注——发送方式边界：该示例的 Kconfig 说明，`AF_PACKET` 分支发送的是用于测量发送耗时的演示数据，不是有效的以太网帧。不能把普通 UDP 回显是否成功当作这一分支的测试标准。模拟 PTP 时钟和驱动能力检查也不替代真实网卡的发送精度测量。

## 3. 另请参阅（See Also）

- [兼容 BSD 套接字的 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)。
- [以太网支持函数](https://docs.zephyrproject.org/latest/doxygen/html/group__ethernet.html)。


<a id="so_txtime"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P133_数据包套接字示例.md) · [返回大纲](大纲.md) · [下一章](P135_网络数据包管理入口.md)
