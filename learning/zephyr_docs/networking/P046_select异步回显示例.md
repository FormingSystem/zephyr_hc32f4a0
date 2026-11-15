---
id: learning.zephyr-docs.networking.page-46
title: select异步回显示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/echo_async_select/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第46章\_select异步回显示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/echo_async_select/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 46.1 概览（Overview）

Zephyr 的 `sockets/echo_async_select` 示例通过 BSD 套接字兼容 API（BSD Sockets Compatible API），结合非阻塞套接字（Non-blocking Socket）和 `select()`，实现异步（Asynchronous）IPv4/IPv6 TCP 回显服务器（Echo Server）。TCP 是传输控制协议（Transmission Control Protocol）。

它是[使用 poll() 的异步回显服务器](P045_poll异步回显示例.md#async-sockets-echo)的变体。源码位于[samples/net/sockets/echo_async_select](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_async_select)，也可[在 GitHub 浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/echo_async_select/README.rst/..)。

## 46.2 运行要求（Requirements）

使用[与主机系统联网](P007_与主机系统联网.md#networking-with-host)的环境，或使用具有硬件联网能力的开发板，包括低功耗无线个域网上的 IPv6（IPv6 over Low-Power Wireless Personal Area Networks，6LoWPAN）开发板。

## 46.3 构建与运行（Building and Running）

构建 Zephyr 版本：

```shell
west build -b <board_to_use> samples/net/sockets/echo_async_select
```

> 译注：原文引导句把应用写作 `sockets/echo_async`，实际命令和本页源码目录为 `sockets/echo_async_select`。`<board_to_use>` 需要替换为实际开发板目标；路径相对于 Zephyr 源码根目录。

启动后，在 IPv4 地址 `192.0.2.1` 或 IPv6 地址 `2001:db8::1` 的 `4242` 端口等待连接：

```shell
$ telnet 192.0.2.1 4242     # use this for IPv4
$ telnet 2001:db8::1 4242   # or this for IPv6
```

第一条用于 IPv4，第二条用于 IPv6。连接建立后，应用会回显发送给它的每一行。与[简单回显服务器](P044_简单回显服务器示例.md#sockets-echo)不同，本例支持多个并发客户端，可以另开终端执行相同的 Telnet 命令。

原文说明最多支持三个客户端，并可通过修改 `NUM_FDS` 调整。

> 源码核对译注：这一限制说明不能直接按 `poll()` 版本套用。读取的官方 [`socket_echo_select.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_async_select/src/socket_echo_select.c) 虽然定义了 `NUM_FDS`，但添加连接的 `pollfds_add()` 只是更新 `fd_set` 和最大描述符范围，没有使用 `NUM_FDS` 执行应用层连接计数限制。官方 [`prj.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_async_select/prj.conf) 中的 `CONFIG_ZVFS_POLL_MAX=5` 也不能等同于源码已经实现“三客户端拒绝逻辑”。实际资源限制还取决于平台与配置，本轮没有进行容量测试。

### 在 POSIX 主机上运行（Running on POSIX Host）

同一份源码可在 Linux 等 POSIX 系统上构建。原文说明主要区别为头文件，以及 Linux 需要设置 IPv6-only 选项，使 IPv6 套接字仅接收 IPv6。

在示例目录构建：

```shell
$ make -f Makefile.host
```

原文运行命令为：

```shell
$ ./socket_echo
```

> 源码核对译注：官方 [Makefile.host](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/echo_async_select/Makefile.host) 的目标名实际是 `socket_echo_select`，所以应运行 `./socket_echo_select`。上方 `./socket_echo` 按原页保留，以便辨认上游说明与当前源码的差异。

测试 IPv4 或 IPv6：

```shell
$ telnet 127.0.0.1 4242   # use this for IPv4
$ telnet ::1 4242         # or this for IPv6
```

应用行为与 Zephyr 版本相同。`127.0.0.1` 和 `::1` 是主机回环地址（Loopback Address），`$` 是提示符，不属于命令。

> 源码核对译注：代码还用 `READ`／`WRITE` 宏适配 POSIX 的 `read()`／`write()` 与 Zephyr 的 `recv()`／`send()`。`IPV6_V6ONLY` 用于区分同端口的 IPv4、IPv6 监听。发送时会临时改为阻塞模式，因而属于半异步（Semi-async）处理；“异步”不表示每次发送都不会阻塞。本轮未执行主机编译、固件构建或通信测试。

## 46.4 相关参考（See Also）

参见[BSD 套接字兼容 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)。


<a id="async-sockets-echo-select"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="running-application-on-posix-host"></a>
<a id="see-also"></a>

[上一章](P045_poll异步回显示例.md) · [返回大纲](大纲.md) · [下一章](P047_高级回显服务器示例.md)
