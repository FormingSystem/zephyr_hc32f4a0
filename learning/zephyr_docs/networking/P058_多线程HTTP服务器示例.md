---
id: learning.zephyr-docs.networking.page-58
title: 多线程HTTP服务器示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/dumb_http_server_mt/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第58章\_多线程HTTP服务器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/dumb_http_server_mt/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 58.1 概览（Overview）

Zephyr 的 `sockets/dumb_http_server_mt` 示例通过 BSD 套接字兼容 API（BSD Sockets Compatible API）实现多线程（Multi-threaded）HTTP 服务器骨架。HTTP 是超文本传输协议（Hypertext Transfer Protocol）。

其基本功能与[简易 HTTP 服务器](P057_简易HTTP服务器示例.md#socket-dumb-http-server)相似，但支持多个同时连接、传输层安全（Transport Layer Security，TLS）以及 IPv6。本示例不兼容 POSIX 主机运行方式。

它仍是极简服务器：不真正解析收到的 HTTP 请求，而是读入后丢弃，始终提供同一份静态页面。

源码位于[samples/net/sockets/dumb_http_server_mt](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/dumb_http_server_mt)，也可[在 GitHub 浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/dumb_http_server_mt/README.rst/..)。

## 58.2 运行要求（Requirements）

需要[与主机系统联网](P007_与主机系统联网.md#networking-with-host)的环境，或具有硬件联网能力的开发板。

## 58.3 构建与运行（Building and Running）

构建 Zephyr 应用：

```shell
west build -b <board_to_use> samples/net/sockets/dumb_http_server_mt
```

`<board_to_use>` 为实际开发板目标占位符；源码路径相对于 Zephyr 根目录。

启动后，服务器在 `192.0.2.1` 或 `2001:db8::1` 的 `8080` 端口等待连接。浏览器打开 `http://192.0.2.1:8080/` 或 `http://[2001:db8::1]:8080/`，应看到关于 Zephyr 的示例内容。该页面截取自某个时间点的 Zephyr 网站，可能与当前在线网站不同。

也可通过 curl 请求：

```shell
$ curl http://192.0.2.1:8080/
```

最后，可以使用 Apache Bench（`ab`）等 HTTP 分析／负载工具：

```shell
$ ab -n10 http://192.0.2.1:8080/
```

`-n` 参数指定请求次数，此例为 10。译注：这条命令只指定总请求数，没有指定并发级别；不能把运行它等同于验证了多客户端并发能力。`$` 是原文 Shell 提示符，本轮没有构建或进行性能、TLS、IPv6 或并发测试。

## 58.4 相关参考（See Also）

参见[BSD 套接字兼容 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)、[网络分组库（Network Packet Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html)、[线程 API（Thread APIs）](../thread_core_reference/P001_线程公共接口.md)和[TLS 凭据管理](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html)。


<a id="socket-dumb-http-server-mt"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="see-also"></a>

[上一章](P057_简易HTTP服务器示例.md) · [返回大纲](大纲.md) · [下一章](P059_MQTT客户端库.md)
