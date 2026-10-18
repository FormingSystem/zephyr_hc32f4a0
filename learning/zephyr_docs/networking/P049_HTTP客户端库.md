---
id: learning.zephyr-docs.networking.page-49
title: HTTP客户端库
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/http_client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第49章\_HTTP客户端库

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/http_client.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 49.1 概览（Overview）

HTTP 客户端库（HTTP Client Library）用于发送超文本传输协议（Hypertext Transfer Protocol，HTTP）请求并解析响应。它通过套接字 API（Sockets API）通信，但不会自行创建套接字。通过 Kconfig 选项 [`CONFIG_HTTP_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_HTTP_CLIENT) 启用该库。

应用负责创建套接字并将其交给库。因此，可以根据应用需求，使用普通传输控制协议（Transmission Control Protocol，TCP）套接字进行 HTTP 通信，也可以使用传输层安全（Transport Layer Security，TLS）套接字进行 HTTPS 通信。

## 49.2 使用示例（Sample Usage）

HTTP 客户端库的请求接口是一个函数。下面展示正确初始化请求结构体的方式：

```c
struct http_request req = { 0 };
static uint8_t recv_buf[512];

req.method = HTTP_GET;
req.url = "/";
req.host = "localhost";
req.protocol = "HTTP/1.1";
req.response = response_cb;
req.recv_buf = recv_buf;
req.recv_buf_len = sizeof(recv_buf);

/* sock is a file descriptor referencing a socket that has been connected
 * to the HTTP server.
 */
ret = http_client_req(sock, &req, 5000, NULL);
```

这里 `sock` 是已经连接到 HTTP 服务器的套接字描述符（Socket Descriptor）。请求使用 `HTTP_GET` 方法、根资源路径 `/`、主机名 `localhost` 和 `HTTP/1.1`，并指定响应回调（Response Callback）与接收缓冲区（Receive Buffer）。

> 源码核对译注：官方 [`client.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/http/client.h) 要求在 `http_client_req()` 之前成功调用 `connect()`。第三个参数以毫秒为单位，示例的 `5000` 表示 5 秒，不能传零。函数成功时返回发送到服务器的数据量，失败时返回负错误值；它的返回值不是收到的 HTTP 状态码。

服务器响应后，库通过请求结构体中注册的回调向应用提供响应。响应可能分多次交付，应用必须能够处理这些数据片段，而不能假定一次回调就得到完整响应。

回调除了收到包含响应数据的结构体，还会得到标记，指出库是否预计继续接收更多数据。一个最简单的响应处理函数如下：

```c
static int response_cb(struct http_response *rsp,
                       enum http_final_call final_data,
                       void *user_data)
{
    if (final_data == HTTP_DATA_MORE) {
        LOG_INF("Partial data received (%zd bytes)", rsp->data_len);
    } else if (final_data == HTTP_DATA_FINAL) {
        LOG_INF("All the data received (%zd bytes)", rsp->data_len);
    }

    LOG_INF("Response status %s", rsp->http_status);

    return 0;
}
```

`HTTP_DATA_MORE` 表示当前收到部分数据，后面还有数据；`HTTP_DATA_FINAL` 表示本次响应的数据接收已结束。原示例分别打印收到的数据长度及响应状态字符串。

> 源码核对译注：响应体片段（Body Fragment）由 `body_frag_start` 和 `body_frag_len` 描述。官方头文件说明，同一接收缓冲区也可能触发多次回调，例如处理分块传输编码（Chunked Transfer Encoding）的响应体时。回调“分批交付”不等于所有响应都使用 HTTP 分块传输编码。当前 `http_response_cb_t` 返回 `0` 表示继续下载，返回负值表示中止；原例返回 `0`。

更多用法见[HTTP 客户端示例](P050_HTTP客户端示例.md#sockets-http-client)。

## 49.3 API 参考与相关示例（API Reference）

完整参考见[HTTP 客户端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html)；本指南与详细参考页分别跟踪翻译状态。

| 示例 | 用途 |
| --- | --- |
| [HTTP 客户端（HTTP Client）](P050_HTTP客户端示例.md#sockets-http-client) | 实现发出多种 HTTP 请求的 HTTP(S) 客户端 |
| [TagoIO HTTP POST](P218_TagoIO的HTTP上报示例.md#tagoio-http-post) | 使用 HTTP 向 TagoIO 物联网（Internet of Things，IoT）云平台发送随机温度值 |

本轮未建立 HTTP／HTTPS 连接或运行示例，源码核对不作为网络测试结果。


<a id="http-client"></a>
<a id="http-client-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="overview"></a>
<a id="sample-usage"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：TLS凭据Shell](P042_TLS凭据Shell.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：WebSocket客户端](P053_WebSocket客户端.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P048_高级回显客户端示例.md) · [返回大纲](大纲.md) · [下一章](P050_HTTP客户端示例.md)

</details>

<!-- reading-navigation:end -->
