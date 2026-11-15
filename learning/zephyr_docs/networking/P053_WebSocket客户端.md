---
id: learning.zephyr-docs.networking.page-53
title: WebSocket客户端
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/websocket.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第53章\_WebSocket客户端

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/websocket.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 53.1 概览（Overview）

WebSocket 客户端库（WebSocket Client Library）使 Zephyr 可以连接 WebSocket 服务器。应用可以直接调用客户端 API 建立连接，也可以把 WebSocket 作为其他网络协议的传输通道（Transport），例如消息队列遥测传输（Message Queuing Telemetry Transport，MQTT）。

工作原理概览见原文引用的[WebSocket 百科文章](https://en.wikipedia.org/wiki/WebSocket)；协议本身的正式定义见[RFC 6455](https://datatracker.ietf.org/doc/html/rfc6455.html)。

## 53.2 WebSocket 传输（WebSocket Transport）

Zephyr MQTT 客户端库可通过启用 [`CONFIG_MQTT_LIB_WEBSOCKET`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_MQTT_LIB_WEBSOCKET) 和 [`CONFIG_WEBSOCKET_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_WEBSOCKET_CLIENT)，使用 WebSocket 承载 MQTT 等高层协议。

首先创建传输控制协议（Transmission Control Protocol，TCP）套接字并连接 WebSocket 服务器：

```c
sock = socket(family, SOCK_STREAM, IPPROTO_TCP);
...
ret = connect(sock, addr, addr_len);
...
```

然后创建 WebSocket 传输套接字：

```c
ws_sock = websocket_connect(sock, &config, timeout, user_data);
```

之后可以通过该套接字收发应用数据。WebSocket 客户端 API 将发送的数据封装进 WebSocket 帧载荷（Payload），并从收到的帧中提取载荷。可以使用 `websocket_xxx()` 系列 API，也可以使用普通 BSD 套接字 API：

```c
ret = websocket_send_msg(ws_sock, buf_to_send, buf_len,
                         WEBSOCKET_OPCODE_DATA_BINARY, true, true,
                         K_FOREVER);
...
ret = send(ws_sock, buf_to_send, buf_len, 0);
```

原文说明，普通 BSD 套接字函数目前只支持文本（TEXT）数据；发送二进制（BINARY）数据必须使用 [`websocket_send_msg()`](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html#gac23c351e5020d0fc9e936933d399b187)。

> 源码核对译注：官方 [`websocket.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/websocket.h) 将发送超时参数定义为毫秒整数 `int32_t`，无限等待使用 `SYS_FOREVER_MS`。原文代码中的 `K_FOREVER` 不是该接口当前要求的毫秒参数约定，应替换为 `SYS_FOREVER_MS`。示例的两个 `true` 分别表示对帧载荷使用掩码（Mask），以及这是消息的最后一帧（Final）。省略号仅表示未展示的应用逻辑。
>
> 原文“普通接口只支持文本”的实际发送行为可在 [`websocket.c`](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/websocket/websocket.c) 中核对：普通发送路径使用 `WEBSOCKET_OPCODE_DATA_TEXT`。若应用需要明确操作码或接收消息类型，应使用 WebSocket 专用 API；不要把文本发送示例当作二进制发送用法。

完成后必须关闭 WebSocket 传输套接字。调用 `websocket_disconnect` 后，用户还要管理底层 TCP 套接字的生命周期（Lifecycle），决定关闭还是复用：

```text
ret = close(ws_sock);
or
ret = websocket_disconnect(ws_sock);
```

> 译注：原文中的 `or` 表示两种方式任选一种，不是 C 代码。官方实现中 `websocket_disconnect()` 调用关闭 WebSocket 描述符的路径；该路径释放 WebSocket 上下文，底层 TCP 套接字仍由应用负责。不要对同一个 WebSocket 描述符把两种关闭方法依次执行。

## 53.3 API 参考与相关示例（API Reference）

完整参考见[WebSocket API](https://docs.zephyrproject.org/latest/doxygen/html/group__websocket.html)。[WebSocket 客户端示例](P054_WebSocket客户端示例.md#sockets-websocket-client)展示如何连接 WebSocket 服务器；本指南与详细 API 参考分别跟踪翻译状态。

本轮未建立 WebSocket 连接、收发帧或验证 MQTT 传输。


<a id="websocket-client-api"></a>
<a id="websocket-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="overview"></a>
<a id="index-0"></a>
<a id="websocket-transport"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：HTTP客户端库](P049_HTTP客户端库.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：HTTP服务器库](P055_HTTP服务器库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P052_HTTP大文件下载示例.md) · [返回大纲](大纲.md) · [下一章](P054_WebSocket客户端示例.md)

</details>

<!-- reading-navigation:end -->
