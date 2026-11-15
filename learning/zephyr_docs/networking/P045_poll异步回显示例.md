---
id: learning.zephyr-docs.networking.page-45
title: poll异步回显示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/echo_async/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第45章\_poll异步回显示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/echo_async/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 45.1 概览（Overview）

Zephyr 的 `sockets/echo-async` 示例通过 BSD 套接字兼容 API（BSD Sockets Compatible API），结合非阻塞套接字（Non-blocking Socket）和 `poll()`，实现异步（Asynchronous）IPv4/IPv6 TCP 回显服务器（Echo Server）。TCP 是传输控制协议（Transmission Control Protocol）。

它扩展了[简单回显服务器](P044_简单回显服务器示例.md#sockets-echo)，支持 IPv4 和 IPv6 的并发连接（Concurrent Connection），限制同时连接的最大数量，并提供基本错误处理。源码目录实际使用下划线：[samples/net/sockets/echo_async](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_async)；也可[在 GitHub 浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/echo_async/README.rst/..)。

## 45.2 运行要求（Requirements）

使用[与主机系统联网](P007_与主机系统联网.md#networking-with-host)的环境，或使用具有硬件联网能力的开发板，包括通过低功耗无线个域网上的 IPv6（IPv6 over Low-Power Wireless Personal Area Networks，6LoWPAN）联网的开发板。

## 45.3 构建与运行（Building and Running）

构建 `sockets/echo_async` 的 Zephyr 版本：

```shell
west build -b <board_to_use> samples/net/sockets/echo_async
```

`<board_to_use>` 是实际开发板目标的占位符；示例路径相对于 Zephyr 源码根目录。

启动后，示例在 IPv4 地址 `192.0.2.1` 或 IPv6 地址 `2001:db8::1` 的 `4242` 端口等待连接：

```shell
$ telnet 192.0.2.1 4242     # use this for IPv4
$ telnet 2001:db8::1 4242   # or this for IPv6
```

第一条用于 IPv4，第二条用于 IPv6。连接建立后，应用会回显收到的任意一行。与[简单回显服务器](P044_简单回显服务器示例.md#sockets-echo)不同，本例支持多个客户端同时连接，可以另开终端执行相同的 Telnet 命令。

原文说明默认最多支持三个客户端，可通过修改源码中的 `NUM_FDS` 调整。

> 源码核对译注：官方 [`socket_echo.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_async/src/socket_echo.c) 中，Zephyr 构建的 `NUM_FDS` 来自 `CONFIG_ZVFS_POLL_MAX`；未定义该配置时才使用常量 `5`。官方 [`prj.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_async/prj.conf) 将配置设为 `5`。同时监听 IPv4、IPv6 时，两项用于监听套接字，剩余三项用于客户端。因此调整 Zephyr 版本容量时，应同时考虑配置与实际监听集合，不能只修改未生效的备用常量。

### Wi-Fi

通过[Wi-Fi 配置片段（Snippet）](../snippets/P027_WiFi_IPv4配置片段.md#snippet-wifi-ipv4)，可以启用示例的 IPv4 Wi-Fi 支持。

### 在 POSIX 主机上运行（Running on POSIX Host）

同一份源码可在 Linux 等 POSIX 系统上构建。原文指出，Zephyr 与 POSIX 使用不同的头文件，Linux 还需要额外设置一个选项，使 IPv6 套接字只接收 IPv6。

在示例目录中构建：

```shell
$ make -f Makefile.host
```

运行：

```shell
$ ./socket_echo
```

测试 IPv4 或 IPv6：

```shell
$ telnet 127.0.0.1 4242   # use this for IPv4
$ telnet ::1 4242         # or this for IPv6
```

行为与 Zephyr 版本相同。`127.0.0.1` 和 `::1` 分别是 IPv4、IPv6 回环地址（Loopback Address）；`$` 是原文提示符。

> 源码核对译注：Linux 分支使用 `IPV6_V6ONLY`，让 IPv4 与 IPv6 监听套接字能分别绑定同一端口。源码称本例为“半异步”（Semi-async）服务器：接收通过 `poll()` 等待，但发送时会临时切换为阻塞模式，因此不要把标题中的“异步”理解为所有读写永远不会阻塞。主机生成目标见官方 [Makefile.host](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_async/Makefile.host)。本轮未执行构建或并发连接测试。

## 45.4 相关参考（See Also）

参见[BSD 套接字兼容 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)。


<a id="async-sockets-echo"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="wi-fi"></a>
<a id="running-application-on-posix-host"></a>
<a id="see-also"></a>

[上一章](P044_简单回显服务器示例.md) · [返回大纲](大纲.md) · [下一章](P046_select异步回显示例.md)
