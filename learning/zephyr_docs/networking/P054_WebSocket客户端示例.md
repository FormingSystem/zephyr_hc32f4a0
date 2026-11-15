---
id: learning.zephyr-docs.networking.page-54
title: WebSocket客户端示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/websocket_client/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第54章\_WebSocket客户端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/websocket_client/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 54.1 概览（Overview）

本示例实现 WebSocket 客户端（WebSocket Client）：先向 HTTP 服务器发出 HTTP 或 HTTPS 握手请求（Handshake Request），再开始发送数据并等待 WebSocket 服务器响应。

HTTP 是超文本传输协议（Hypertext Transfer Protocol）；HTTPS 表示使用传输层安全（Transport Layer Security，TLS）的 HTTP 通信。

源码位于[samples/net/sockets/websocket_client](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/websocket_client)，也可[在 GitHub 浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/websocket_client/README.rst/..)。

## 54.2 前置要求（Requirements）

准备[与主机系统联网](P007_与主机系统联网.md#networking-with-host)的环境。可在受支持的开发板上使用，也可按照[QEMU 联网](P009_QEMU联网概览.md#networking-with-qemu)说明在模拟器中运行。

## 54.3 构建与运行（Building and Running）

构建 WebSocket 客户端：

```shell
west build -b <board to use> samples/net/sockets/websocket_client -- -DCONF_FILE=<config file to use>
```

`<board to use>` 和 `<config file to use>` 分别替换为实际开发板目标和配置文件；示例路径相对于 Zephyr 源码根目录。

### 启用 TLS（Enabling TLS Support）

构建时加入 `overlay-tls.conf` 配置叠加文件（Configuration Overlay）：

```shell
west build -b qemu_x86 samples/net/sockets/websocket_client -- -DCONF_FILE="prj.conf overlay-tls.conf"
```

也可在 `west build` 或 `cmake` 命令中指定 `-DEXTRA_CONF_FILE=overlay-tls.conf`。

示例使用的证书（Certificate）和私钥（Private Key）位于[samples/net/sockets/websocket_client/src/](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/websocket_client/src/)。

## 54.4 在 Linux 主机运行服务器（Running websocket-server in Linux Host）

可以在 QEMU 中运行客户端，在 Linux 主机运行 net-tools 提供的 `zephyr-websocket-server.py`。另一种选择是安装并使用[websocketd](http://websocketd.com/)。

先按[QEMU 联网](P009_QEMU联网概览.md#networking-with-qemu)设置环境。在主机终端选择以下一种服务器：

```shell
$ ./zephyr-websocket-server.py
```

或：

```shell
$ websocketd --port=9001 cat
```

这里 [`websocketd`](http://websocketd.com/) 在端口 `9001` 启动服务，并使用 `cat` 回送收到的数据。然后在 Zephyr 源码根目录构建并运行 QEMU 客户端：

```shell
west build -b qemu_x86 samples/net/sockets/websocket_client -- -DCONF_FILE=prj.conf
west build -t run
```

启动 QEMU 客户端之前，必须先让 `zephyr-websocket-server.py` 或 [`websocketd`](http://websocketd.com/) 在 Linux 主机运行。退出 QEMU 时，按 `CTRL`+`A`，再按 `x`。

原文说明，[net-tools 项目](https://github.com/zephyrproject-rtos/net-tools)中的当前 `zephyr-websocket-server.py` 不支持 TLS。

> 源码核对译注：读取的官方 [`zephyr-websocket-server.py`](https://github.com/zephyrproject-rtos/net-tools/blob/master/zephyr-websocket-server.py) 以 `192.0.2.2:9001` 启动服务器，没有配置 TLS，收到消息后将其回送。该脚本从同目录下的 `python-websocket-server` 导入依赖，主机需先准备完整的工具及依赖。前面的客户端 TLS 构建能力，不表示这条未配置 TLS 的主机脚本能与之建立安全连接。

`./zephyr-websocket-server.py` 相对于主机工具目录，客户端源码路径相对于 Zephyr 根目录，两者都不要求固定仓库盘符。`$` 是原文提示符。本轮未安装 websocketd、启动主机服务器、构建或执行网络测试。

## 54.5 相关参考（See Also）

参见[BSD 套接字兼容 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)、[WebSocket API](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html)和[WebSocket 客户端指南](P053_WebSocket客户端.md)。


<a id="sockets-websocket-client"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="enabling-tls-support"></a>
<a id="running-websocket-server-in-linux-host"></a>
<a id="see-also"></a>

[上一章](P053_WebSocket客户端.md) · [返回大纲](大纲.md) · [下一章](P055_HTTP服务器库.md)
