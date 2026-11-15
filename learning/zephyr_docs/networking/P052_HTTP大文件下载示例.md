---
id: learning.zephyr-docs.networking.page-52
title: HTTP大文件下载示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/big_http_download/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_HTTP大文件下载示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/big_http_download/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 52.1 概览（Overview）

Zephyr 的 `sockets/big_http_download` 示例使用 BSD 套接字兼容 API（BSD Sockets Compatible API）实现简单的 HTTP GET 客户端。HTTP 是超文本传输协议（Hypertext Transfer Protocol）。

与[普通套接字 HTTP GET 示例](P051_普通套接字HTTP_GET示例.md#sockets-http-get)不同，本例下载数兆字节的文件，并用哈希（Hash）验证完整性。它会重复下载，累计传输的总字节数，因此可作为 Zephyr IP 协议栈的负载测试（Load Testing）应用。

源码位于[samples/net/sockets/big_http_download](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/big_http_download)，也可[在 GitHub 浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/big_http_download/README.rst/..)。

## 52.2 运行要求（Requirements）

需要[与主机系统联网](P007_与主机系统联网.md#networking-with-host)的环境，或具有硬件联网能力的开发板。需要通过网络地址转换（Network Address Translation，NAT）／路由允许设备访问互联网，并在主机提供可用的域名系统（Domain Name System，DNS）服务以解析域名。

## 52.3 构建与运行（Building and Running）

构建应用的 Zephyr 版本：

```shell
west build -b <board_to_use> samples/net/sockets/big_http_download
```

`<board_to_use>` 需要替换为实际开发板目标；源码路径相对于 Zephyr 根目录。

启动后，示例向原文指定的[Ubuntu Xenial vmlinuz 文件](http://archive.ubuntu.com/ubuntu/dists/xenial/main/installer-amd64/current/images/hd-media/vmlinuz)发出 HTTP GET 请求。原文选择这个站点，是因为它提供多种大小的文件及相应哈希，便于选择和校验。

原文所选文件约 6.7 MB，既能观察 Zephyr 流式传输（Streaming）一定规模数据的可靠性，也能在较合理的时间内完成。下载时计算 SHA-256 哈希，并与源码中的参考值比较；不一致时打印错误。短暂停顿后再次下载，以无限循环方式重复，同时保留累计接收字节数，从而支持更长时间、更大流量的测试。

可以修改源码以访问其他互联网站点，或访问本地网络中的服务器；后者不需要为互联网访问配置 NAT／路由。

> 原文警告：进行大量测试时，请使用本地服务器，或自己在互联网上部署的专用测试服务器。不要用 `archive.ubuntu.com` 的文件进行大规模测试。

> 源码核对译注：当前官方 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/big_http_download/Kconfig) 提供示例私有选项 [`CONFIG_SAMPLE_BIG_HTTP_DL_URL`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/big_http_download/Kconfig) 和 [`CONFIG_SAMPLE_BIG_HTTP_DL_NUM_ITER`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/big_http_download/Kconfig)，后者默认为 `0`，表示不限次数。更换下载文件时，还需同步核对 [`big_http_download.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/big_http_download/src/big_http_download.c) 中的参考哈希，不能只改 URL。6.7 MB 是原页描述，不代表本轮重新测量的文件大小；链接可达也不等于文件仍与旧参考哈希相同。

### 启用 TLS（Enabling TLS Support）

构建时加入 `overlay-tls.conf`，启用传输层安全（Transport Layer Security，TLS）：

```shell
west build -b qemu_x86 samples/net/sockets/big_http_download -- -DCONF_FILE="prj.conf overlay-tls.conf"
```

也可在 `west build` 或 `cmake` 中指定 `-DEXTRA_CONF_FILE=overlay-tls.conf`。

TLS 版本下载原文指定的[Git 2.34.1 源码压缩包](https://launchpad.net/ubuntu/+archive/primary/+sourcefiles/git/1:2.34.1-1ubuntu1/git_2.34.1.orig.tar.xz)，原文大小约 6.6 MB。用于访问默认[Launchpad 站点](https://launchpad.net)及可能重定向（Redirect）目标的证书位于示例 `src` 目录。访问其他 TLS 站点时，需要提供适合验证新服务器的证书。

官方 [`overlay-tls.conf`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/big_http_download/overlay-tls.conf) 中仍指定了上述下载地址。证书、远端内容及服务行为均可能随时间变化，本轮未执行固件下载测试或核验这份压缩包的内容哈希。

本例的 TLS 模式依赖非 POSIX 的 TLS 套接字功能，因此只能在 Zephyr 上运行 TLS 版本。

## 52.4 在 POSIX 主机运行（Running on POSIX Host）

同一份应用源码可以在 Linux 等 POSIX 系统构建。在该示例目录执行：

```shell
$ make -f Makefile.host
```

然后运行：

```shell
$ ./big_http_download
```

应用行为与 Zephyr 版本相同，TLS 限制仍如前述。

> 源码核对译注：官方 [Makefile.host](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/big_http_download/Makefile.host) 会链接 `mbedcrypto`，并说明主机须已安装 Mbed TLS 开发文件，例如 Debian／Ubuntu 的 `libmbedtls-dev`。所以这不是只依赖 C 编译器的单文件构建。`$` 是提示符。本轮未安装依赖、编译主机程序或运行循环负载测试。

## 52.5 相关参考（See Also）

参见[BSD 套接字兼容 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)与[TLS 凭据管理](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html)。


<a id="sockets-big-http-download"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="enabling-tls-support"></a>
<a id="running-application-on-posix-host"></a>
<a id="see-also"></a>

[上一章](P051_普通套接字HTTP_GET示例.md) · [返回大纲](大纲.md) · [下一章](P053_WebSocket客户端.md)
