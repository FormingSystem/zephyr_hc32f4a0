---
id: learning.zephyr-docs.networking.page-57
title: 简易HTTP服务器示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/dumb_http_server/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第57章\_简易HTTP服务器示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/dumb_http_server/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 57.1 概览（Overview）

Zephyr 的 `sockets/dumb_http_server` 示例使用 BSD 套接字兼容 API（BSD Sockets Compatible API）实现一个 HTTP 服务器骨架。HTTP 是超文本传输协议（Hypertext Transfer Protocol）。

它演示如何编写可在 POSIX 与 Zephyr 之间移植的套接字应用，因此保持极简：不真正解析收到的 HTTP 请求，而是读取后丢弃，始终返回同一份静态页面。即使如此，它仍能展示如何编写可由普通浏览器访问的套接字程序，也可使用现成 HTTP 诊断工具进行性能或回归测试（Regression Testing）。

源码位于[samples/net/sockets/dumb_http_server](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/dumb_http_server)，也可[在 GitHub 浏览官方源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/dumb_http_server/README.rst/..)。

## 57.2 运行要求（Requirements）

需要[与主机系统联网](P007_与主机系统联网.md#networking-with-host)的环境，或具有硬件联网能力的开发板。

## 57.3 构建与运行（Building and Running）

构建 Zephyr 版本：

```shell
west build -b <board_to_use> samples/net/sockets/dumb_http_server
```

> 译注：原文引导句误写为 `sockets/echo`，实际命令和本页源码均为 `sockets/dumb_http_server`。`<board_to_use>` 为实际开发板目标占位符；路径相对于 Zephyr 根目录。

启动后，示例在 `192.0.2.1:8080` 等待连接。浏览器打开 `http://192.0.2.1:8080/`，应看到一份关于 Zephyr 的示例页面。它是在某一时刻从 Zephyr 网站截取的内容，可能与当前在线网站不同。

也可以使用 curl：

```shell
$ curl http://192.0.2.1:8080/
```

或者使用 Apache Bench（`ab`）等 HTTP 分析／负载工具：

```shell
$ ab -n10 http://192.0.2.1:8080/
```

`-n` 指定向服务器发出的 HTTP 请求数量，此例为 10。

## 57.4 在 POSIX 主机运行（Running on POSIX Host）

同一源码可在 Linux 等 POSIX 系统构建。原文说明两种环境主要使用不同的头文件。

在示例目录中构建：

```shell
$ make -f Makefile.host
```

运行：

```shell
$ ./socket_dumb_http
```

访问 `http://127.0.0.1:8080/`，再按上一节测试。行为与 Zephyr 版本相同；`127.0.0.1` 是主机回环地址（Loopback Address）。

> 源码核对译注：官方 [Makefile.host](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/dumb_http_server/Makefile.host) 注释要求先运行一次 Zephyr 构建以生成包含文件；并非只取得单个 C 文件即可直接完成主机构建。`$` 是提示符，本轮未编译或执行请求／负载测试。

## 57.5 相关参考（See Also）

参见[BSD 套接字兼容 API](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__sockets.html)与[网络分组库（Network Packet Library）](https://docs.zephyrproject.org/latest/doxygen/html/group__net__pkt.html)。


<a id="socket-dumb-http-server"></a>
<a id="overview"></a>
<a id="requirements"></a>
<a id="building-and-running"></a>
<a id="running-application-on-posix-host"></a>
<a id="see-also"></a>

[上一章](P056_HTTP服务器示例.md) · [返回大纲](大纲.md) · [下一章](P058_多线程HTTP服务器示例.md)
