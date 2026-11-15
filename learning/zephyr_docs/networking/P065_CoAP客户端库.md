---
id: learning.zephyr-docs.networking.page-65
title: CoAP客户端库
kind: reference
status: maintained
domains: [zephyr, networking, development]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/networking/api/coap_client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第65章\_CoAP客户端库

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/networking/api/coap_client.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

## 65.1 概览（Overview）

CoAP 客户端库（CoAP Client Library）允许应用发送请求并解析响应，通过 [`CONFIG_COAP_CLIENT`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_CLIENT) 启用。请求中提供响应回调（Response Callback），由库通知应用结果。

UDP 分支支持普通用户数据报协议（User Datagram Protocol，UDP）或数据报传输层安全（Datagram Transport Layer Security，DTLS）套接字。应用负责创建套接字，客户端库负责通过它通信。

### 基于 TCP 的 CoAP（CoAP over TCP）

库还支持[RFC 8323](https://datatracker.ietf.org/doc/html/rfc8323.html)定义的可靠传输（Reliable Transport），包括 TCP／TLS。通过 [`CONFIG_COAP_CLIENT_TCP`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_CLIENT_TCP) 启用后，TCP 客户端内部管理连接建立、能力与设置消息（Capabilities and Settings Message，CSM）交换，以及 Ping/Pong、Release、Abort 信令。

这条路径由应用调用 [`coap_client_tcp_connect()`](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gabc8c1782e586f61a4ba196576279baad) 并传入服务器地址，套接字由库创建。示例见[CoAP TCP 客户端](P069_CoAP_TCP客户端示例.md#coap-client-tcp)。

## 65.2 初始化并发送请求（Sample Usage）

先初始化客户端，再准备请求：

```c
static struct coap_client client;
struct coap_client_request req = { 0 };

coap_client_init(&client, NULL);

req.method = COAP_METHOD_GET;
req.confirmable = true;
strcpy(req.path, "test");
req.fmt = COAP_CONTENT_FORMAT_TEXT_PLAIN;
req.cb = response_cb;
req.payload = NULL;
req.len = 0;

/* Sock is a file descriptor referencing a socket, address is the net_sockaddr struct for the
 * destination address of the request or NULL if the socket is already connected.
 */
ret = coap_client_req(&client, sock, &address, &req, -1);
```

`sock` 是应用已打开的套接字描述符；`address` 是目标地址。如果套接字已经连接目标，可将地址参数设为 `NULL`。

原文说明，一个 CoAP 客户端同一时刻只能发送一个请求，可以创建多个客户端实例。

> 源码核对译注：当前官方 [`coap_client.h`](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/net/coap_client.h) 的 `coap_client_req()` 最后一个参数是 `struct coap_transmission_parameters *`，使用默认传输参数应传 `NULL`，不能照抄原例的 `-1`。当前 [Kconfig](https://github.com/zephyrproject-rtos/zephyr/blob/main/subsys/net/lib/coap/Kconfig) 通过 `CONFIG_COAP_CLIENT_MAX_REQUESTS` 控制每个客户端的并发请求槽，默认值为 2；因此“只能一个”是原页尚未同步的描述。槽已满返回 `-EAGAIN`，已有请求使用另一个套接字时返回 `-EALREADY`，不能据此认为一个实例可任意混用多个套接字。

请求有响应或因某种原因失败时，调用注册的回调。回调中的 `last_block` 表示是否已收到最后一块；为 `true` 时，本次响应结束，回调返回后客户端可以接续请求。

响应可能采用分块传输（Blockwise Transfer），库每收到一块就调用一次回调。应用必须处理所有块，才能得到完整响应。

## 65.3 分块响应与资源一致性

按照[RFC 7959](https://datatracker.ietf.org/doc/html/rfc7959.html)，客户端在分块传输期间比较实体标签（Entity Tag，ETag）。资源表示在传输过程中变化时，中止传输，并以 `result_code=-EBADMSG` 调用回调。

实现比 RFC 最低要求更严格：规范最低要求比较服务器提供的 ETag；Zephyr 在后续块突然出现或不再携带 ETag 时也会中止，因为无法验证有标签与无标签混合的数据。应用应丢弃已收到的部分数据，必要时重新请求。

简单的响应处理函数如下：

```c
void response_cb(const struct coap_client_response_data *data, void *user_data)
{
    if (data->result_code >= 0) {
            LOG_INF("CoAP response from server %d", data->result_code);
            if (data->last_block) {
                    LOG_INF("Last packet received");
            }
    } else {
            LOG_ERR("Error in sending request %d", data->result_code);
    }
}
```

> 译注：`result_code` 非负表示收到 CoAP 响应，仍须按具体 CoAP 响应码判断业务是否成功；不能把所有非负值都视为成功下载。

应用可以为请求增加 CoAP 选项（Option）。下例在初始请求中添加 `Block2`，向服务器建议最大块尺寸，适用于预期资源较大的场景；参见 RFC 7959 图 3 的提前协商分块 GET（Block-Wise GET with Early Negotiation）：

```c
static struct coap_client client;
struct coap_client_request req = { 0 };

coap_client_init(&client, NULL);

req.method = COAP_METHOD_GET;
req.confirmable = true;
strcpy(req.path, "test");
req.fmt = COAP_CONTENT_FORMAT_TEXT_PLAIN;
req.cb = response_cb;
req.options[0] = coap_client_option_initial_block2();
req.num_options = 1;
req.payload = NULL;
req.len = 0;

ret = coap_client_req(&client, sock, &address, &req, -1);
```

这里同样需要按当前接口调整末尾传输参数，见前面的源码核对译注。

## 65.4 使用负载回调上传

上传时，可以注册负载回调（Payload Callback），代替指向整段连续数据的指针。库准备 PUT／POST 请求时调用它，让应用逐块提供内容。下面以 Lorem Ipsum 字符串为例：

```c
static int lorem_ipsum_cb(size_t offset, const uint8_t **payload, size_t *len,
                          bool *last_block, void *user_data)
{
    size_t data_left;

    if (offset > LOREM_IPSUM_STRLEN) {
        return -EINVAL;
    }

    *payload = LOREM_IPSUM + offset;

    data_left = LOREM_IPSUM_STRLEN - offset;
    if (data_left <= *len) {
        *len = data_left;
        *last_block = true;
    } else {
        *last_block = false;
    }

    return 0;
}
```

`offset` 是当前数据偏移；`len` 输入时表示本次允许的最大块长度，输出时表示实际提供长度；`last_block` 表示是否结束。官方头文件要求分块上传时，中间块填满请求长度，只有最后一块可以较短。回调返回负错误码会中止上传。

把回调注册到 PUT／POST 请求：

```c
struct coap_client_request req = { 0 };

req.method = COAP_METHOD_PUT;
req.confirmable = true;
strcpy(req.path, "lorem-ipsum");
req.fmt = COAP_CONTENT_FORMAT_TEXT_PLAIN;
req.cb = response_cb;
req.payload_cb = lorem_ipsum_cb,

ret = coap_client_req(&client, sock, &address, &req, -1);
```

> 译注：原例 `req.payload_cb = lorem_ipsum_cb,` 使用逗号连接了后面的表达式；独立赋值写成分号更清楚。末尾 `-1` 仍是前述旧接口参数。若选择直接提供 `payload` 指针的方式，官方头文件要求其在整个分块事务期间有效，直到收到最后一块或错误通知。

## 65.5 API 参考（API Reference）

参见[CoAP 客户端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html)、[CoAP TCP 客户端 API](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html)与[TCP 客户端示例](P069_CoAP_TCP客户端示例.md#coap-client-tcp)。本章原代码保留用于对照，本轮未构建或执行请求、重试与分块传输。


<a id="coap-client"></a>
<a id="coap-client-interface"></a>
<a id="contents"></a>
<a id="id1"></a>
<a id="id2"></a>
<a id="id3"></a>
<a id="id4"></a>
<a id="overview"></a>
<a id="coap-over-tcp"></a>
<a id="index-0"></a>
<a id="sample-usage"></a>
<a id="index-1"></a>
<a id="index-2"></a>
<a id="api-reference"></a>

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：CoAP协议库](P064_CoAP协议库.md) · [本模块主线目录](../reading/networking.md) · [全部主线](../reading/README.md) · [下一篇：CoAP服务器库](P066_CoAP服务器库.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P064_CoAP协议库.md) · [返回大纲](大纲.md) · [下一章](P066_CoAP服务器库.md)

</details>

<!-- reading-navigation:end -->
