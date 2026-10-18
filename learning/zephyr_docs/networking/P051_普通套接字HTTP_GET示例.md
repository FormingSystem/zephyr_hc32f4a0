---
id: learning.zephyr-docs.networking.page-51
title: 普通套接字HTTP_GET示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/http_get/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第51章\_普通套接字HTTP_GET示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/http_get/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 51.1 概览（Overview）

Zephyr 的 `sockets/http_get` 示例使用 BSD 套接字兼容 API（BSD Sockets Compatible API）实现简单的 HTTP GET 客户端。HTTP 是超文本传输协议（Hypertext Transfer Protocol），GET 是获取资源的请求方法。

该示例演示如何编写能在 POSIX 系统与 Zephyr 之间移植的套接字应用，因此保持精简，仅支持 IPv4。源码位于[samples/net/sockets/http_get](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_get)，也可[在 GitHub 浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/http_get/README.rst/..)。

## 51.2 运行要求（Requirements）

需要[与主机系统联网](P007_与主机系统联网.md#networking-with-host)的环境，或具有硬件联网能力的开发板。还需要配置网络地址转换（Network Address Translation，NAT）／路由，使设备能够访问互联网；主机上应有可用的域名系统（Domain Name System，DNS）服务器，用于解析域名。

## 51.3 构建与运行（Building and Running）

构建应用的 Zephyr 版本：

```shell
west build -b <board_to_use> samples/net/sockets/http_get
```

`<board_to_use>` 为实际开发板目标的占位符。示例路径相对于 Zephyr 源码根目录。

启动后，示例向 `google.com:80` 发出 HTTP GET 请求并输出响应内容。可以修改源码，向其他互联网网站请求资源；也可以访问本地网络中的站点，此时不需要为访问互联网额外设置 NAT／路由。退出 QEMU 时，按 `CTRL`+`A`，再按 `x`。

### 启用 TLS（Enabling TLS Support）

通过 `overlay-tls.conf` 配置叠加文件（Configuration Overlay）启用传输层安全（Transport Layer Security，TLS）：

```shell
west build -b qemu_x86 samples/net/sockets/http_get -- -DCONF_FILE="prj.conf overlay-tls.conf"
```

也可在 `west build` 或 `cmake` 中指定 `-DEXTRA_CONF_FILE=overlay-tls.conf`。

对于支持 TLS 卸载（TLS Offloading）的开发板，例如 TI 的 `cc3220sf_launchxl`，使用 `overlay-tls-offload.conf` 代替 `overlay-tls.conf`。

示例证书位于 `src` 目录，选择它是为了访问示例默认配置的网站[https://google.com](https://google.com)。若要通过 TLS 访问其他站点，需要提供适合验证目标 Web 服务器的证书。

本示例的 TLS 支持依赖非 POSIX 的 TLS 套接字功能，因此本示例只能在 Zephyr 上运行 TLS 模式。

### 启用 TLS 会话缓存（TLS Session Cache）

要启用持久化会话缓存（Persistent Session Cache），在 TLS 配置上再叠加 `overlay-tls-session-cache.conf`：

```shell
west build -b <board_to_use> samples/net/sockets/http_get -- -DCONF_FILE="prj.conf overlay-tls.conf overlay-tls-session-cache.conf"
```

该配置通过设置子系统（Settings Subsystem）启用持久化会话缓存。每次成功完成 TLS 握手（Handshake）后保存会话，系统启动时恢复会话，使设备重启后可以恢复会话（Session Resumption），避免再次进行完整握手。

> 源码核对译注：官方 [`overlay-tls-session-cache.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_get/overlay-tls-session-cache.conf) 同时启用了 Flash、设置子系统及非易失性存储（Non-Volatile Storage，NVS）后端，目标平台需要具备相应存储支持。示例私有选项 `CONFIG_NET_SAMPLE_TLS_SESSION_CACHE` 定义在其 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_get/Kconfig) 中，源码 [`http_get.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_get/src/http_get.c) 用它设置 `TLS_SESSION_CACHE`。仅启用内存缓存不等于可以跨重启保留；原文的持久化能力依赖上述完整配置。本轮未验证重启后的会话恢复。

### Wi-Fi

通过[Wi-Fi 配置片段（Snippet）](../snippets/P027_WiFi_IPv4配置片段.md#snippet-wifi-ipv4)启用 IPv4 Wi-Fi 支持。

## 51.4 在 POSIX 主机运行（Running on POSIX Host）

同一应用源码也可在 Linux 等 POSIX 系统构建。原文说明，Zephyr 与 POSIX 主要使用不同的头文件。

在该示例目录中构建：

```shell
$ make -f Makefile.host
```

运行：

```shell
$ ./http_get
```

应用行为与 Zephyr 版本相同，但前述 TLS 模式仅适用于 Zephyr。主机目标名可在官方 [Makefile.host](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/http_get/Makefile.host) 中核对。`$` 是原文 Shell 提示符，不属于命令。

## 51.5 相关参考（See Also）

参见[BSD 套接字兼容 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)、[TLS 凭据管理](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html)及[TLS 套接字选项](https://docs.zephyrproject.org/latest/doxygen/html/group__secure__sockets__options.html)。本轮未构建、修改路由、发送示例请求或测试 TLS 会话缓存。


<a id="sockets-http-get"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="enabling-tls-support"></a>
<a id="enabling-tls-session-cache"></a>
<a id="wi-fi"></a>
<a id="running-application-on-posix-host"></a>
<a id="see-also"></a>

[上一章](P050_HTTP客户端示例.md) · [返回大纲](大纲.md) · [下一章](P052_HTTP大文件下载示例.md)
