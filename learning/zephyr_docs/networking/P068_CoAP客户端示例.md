---
id: learning.zephyr-docs.networking.page-68
title: CoAP客户端示例
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/samples/net/sockets/coap_client/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第68章\_CoAP客户端示例

原文：[官方页面](https://docs.zephyrproject.org/latest/samples/net/sockets/coap_client/README.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 68.1 概览（Overview）

这是一个简单的 CoAP 客户端（CoAP Client），展示如何从资源（Resource）读取信息。所选平台需要支持网络，必要时调整配置。可[浏览官方示例源码](https://github.com/zephyrproject-rtos/zephyr/blob/main//samples/net/sockets/coap_client/README.rst/..)。

通过 [`CONFIG_NET_SAMPLE_COAP_CLIENT_PEER`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/coap_client/Kconfig) 选择服务器。对端（Peer）字符串可以是 IPv4 字面地址、IPv6 字面地址或主机名；省略端口时，使用 CoAP 默认端口 `5683`。

默认配置对应的统一资源标识符（Uniform Resource Identifier，URI）可表示为：

```text
coap://[2001:db8::1]:5683/test
```

其他有效对端字符串包括：

```text
192.0.2.1:5683
192.0.2.42
[2001:db8::1]:5683
[2001:db8::2]
example.com:5683
example.com
```

回复超时和分块重试行为可分别通过 [`CONFIG_NET_SAMPLE_COAP_CLIENT_REPLY_TIMEOUT_MS`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/coap_client/Kconfig)、[`CONFIG_NET_SAMPLE_COAP_CLIENT_BLOCKWISE_MAX_RETRIES`](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/coap_client/Kconfig) 配置。

> 源码核对译注：这三个选项定义在示例自己的 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/net/sockets/coap_client/Kconfig)。回复超时单位为毫秒，默认 0 表示一直等待；分块超时重试次数默认 0，只有回复超时非零时才生效。

例如，在应用配置中设置 IPv4 对端：

```kconfig
CONFIG_NET_SAMPLE_COAP_CLIENT_PEER="192.0.2.1:5683"
```

启用域名系统（Domain Name System，DNS）后，可以使用主机名测试：

```kconfig
CONFIG_NET_SAMPLE_COAP_CLIENT_PEER="example.com:5683"
```

`net-tools\coap-test-server\` 中的 `coap_sample_server.py` 是供手工互操作测试使用的辅助服务器。原页此处遗留未渲染的 `:ref:` 标记；有效说明见官方 [coap-test-server/README.md](https://github.com/zephyrproject-rtos/net-tools/blob/master/coap-test-server/README.md)。

## 68.2 构建与运行（Building and Running）

程序打印收到响应的所有八位字节（Octet）。可结合 `tcpdump` 或 `wireshark` 查看更多上下文，网络环境见[net-tools](https://github.com/zephyrproject-rtos/net-tools)。测试服务器的详细说明位于原文所称的 `net-tools\coap-test-server\README.md`；这些是工具项目内的相对位置。

按[与主机系统联网](P007_与主机系统联网.md#networking-with-host)中的说明，在 QEMU 或 `native_sim` 上构建并运行。本页没有另外给出构建命令。

> 译注：辅助服务器用于开发期手工互操作验证。官方 README 提供 `/test`、`/large`、`/obs` 资源，分别支持基本方法、分块 GET 和观察通知测试；不把它当作生产服务部署结果。

## 68.3 示例输出（Sample Output）

```text
reply: 60 00 00 00 00 24 11 40 fe 80 00 00 00 00 00 00 5c 25 e2 ff fe
15 01 01 fe 80 00 00 00 00 00 00 5c 25 e2 ff fe 15 01 01 16 33 16 33
00 24 3d 86 60 40 00 01 ff 54 79 70 65 3a 20 30 0a 43 6f 64 65 3a 20
31 0a 4d 49 44 3a 20 31 0a (76 bytes)
```

上述 76 字节及十六进制内容来自官方原页，不是本轮实测。实际内容随响应变化。

## 68.4 相关参考（See Also）

参见[CoAP 基础库 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html)。本轮未启动辅助服务器、构建客户端或发送网络请求。


<a id="coap-client"></a>
<a id="overview"></a>
<a id="building-and-running"></a>
<a id="sample-output"></a>
<a id="see-also"></a>

[上一章](P067_CoAP_OSCORE对象安全.md) · [返回大纲](大纲.md) · [下一章](P069_CoAP_TCP客户端示例.md)
