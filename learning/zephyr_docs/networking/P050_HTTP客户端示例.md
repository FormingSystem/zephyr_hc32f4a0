---
id: learning.zephyr-docs.networking.page-50
title: HTTP客户端示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/http_client/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第50章\_HTTP客户端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/http_client/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 50.1 概览（Overview）

本示例实现 HTTP(S) 客户端（HTTP(S) Client）：发送 HTTP 或 HTTPS 请求，再等待 HTTP 服务器返回响应。HTTP 是超文本传输协议（Hypertext Transfer Protocol），HTTPS 是通过传输层安全（Transport Layer Security，TLS）保护的 HTTP 通信。

源码位于[samples/net/sockets/http_client](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_client)，也可[在 GitHub 浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/http_client/README.rst/..)。

## 50.2 前置要求（Requirements）

准备[与主机系统联网](P007_与主机系统联网.md#networking-with-host)的环境。该应用可在受支持的开发板上使用，也可按[QEMU 联网](P009_QEMU联网概览.md#networking-with-qemu)说明在模拟器中运行。

## 50.3 构建与运行（Building and Running）

构建 HTTP 客户端示例：

```shell
west build -b <board to use> samples/net/sockets/http_client -- -DCONF_FILE=<config file to use>
```

> 译注：`<board to use>` 和 `<config file to use>` 是原文占位符，应替换为实际开发板目标和配置文件。示例路径相对于 Zephyr 源码根目录，不依赖仓库在电脑上的固定位置。

### 启用 TLS（Enabling TLS Support）

构建时加入 `overlay-tls.conf` 配置叠加文件（Configuration Overlay）：

```shell
west build -b qemu_x86 samples/net/sockets/http_client -- -DCONF_FILE="prj.conf overlay-tls.conf"
```

另一种方式是在运行 `west build` 或 `cmake` 时指定 `-DEXTRA_CONF_FILE=overlay-tls.conf`。

示例使用的证书（Certificate）和私钥（Private Key）位于[samples/net/sockets/http_client/src/](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_client/src/)。Socket HTTP Client 和[net-tools 项目](https://github.com/zephyrproject-rtos/net-tools)中的 `https-server.py` 使用的默认证书，可以在这两个示例之间建立安全连接。

## 50.4 在 Linux 主机运行服务器（Running http-server in Linux Host）

可以在 QEMU 中运行 HTTP 客户端，同时在 Linux 主机上运行 net-tools 提供的 `http-server.py`。先按[QEMU 联网](P009_QEMU联网概览.md#networking-with-qemu)准备环境。

在已准备好 net-tools 的主机终端启动服务器：

```shell
$ ./http-server.py
```

然后在 Zephyr 源码根目录构建并运行 QEMU 客户端：

```shell
west build -b qemu_x86 samples/net/sockets/http_client -- -DCONF_FILE=prj.conf
west build -t run
```

必须先让 `http-server.py` 在 Linux 主机运行，再启动 QEMU 中的 HTTP 客户端。退出 QEMU 时，按 `CTRL`+`A`，再按 `x`。

也可以验证与 Linux 主机的 TLS 通信：将主机程序换成 net-tools 中的 `https-server.py`，同时使用前面启用 TLS 的客户端配置。

> 译注：`./http-server.py` 是主机工具目录中的脚本，[`samples/net/sockets/http_client`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_client) 则是 Zephyr 应用路径；两者的工作目录不同。原文的 `$` 为 Shell 提示符。本轮未启动主机服务、构建、运行 QEMU 或进行 HTTP／TLS 测试。

## 50.5 相关参考（See Also）

参见[BSD 套接字兼容 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)、[HTTP 客户端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html)、[TLS 凭据管理](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html)和[TLS 套接字选项](https://docs.zephyrproject.org/latest/doxygen/html/group__secure__sockets__options.html)。库的使用说明见[HTTP 客户端库](P049_HTTP客户端库.md)。


<a id="sockets-http-client"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="enabling-tls-support"></a>
<a id="running-http-server-in-linux-host"></a>
<a id="see-also"></a>

[上一章](P049_HTTP客户端库.md) · [返回大纲](大纲.md) · [下一章](P051_普通套接字HTTP_GET示例.md)
