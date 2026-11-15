---
id: learning.zephyr-docs.api-coap-trusted-topic-reference.page-6
title: CoAP客户端（Client）的API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_CoAP客户端（Client）的API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP客户端（Client）的API。

<a id="details"></a>

CoAP 客户端 API（Client API）。自 3.4 起提供（Since 3.4），版本（Version）0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 6.1\_数据结构（Data Structures）

<a id="r_coap_5Fclient_5Fresponse_5Fdata"></a>

```c
struct coap_client_response_data
```

相关声明：[coap_client_response_data](../network_application_model_reference/P005_coap_client_response_data_结构体.md)。

CoAP客户端响应数据（Client Response Data）的表示。

<a id="r_coap_5Fclient_5Foption"></a>

```c
struct coap_client_option
```

相关声明：[coap_client_option](../network_application_model_reference/P003_coap_client_option_结构体.md)。

CoAP客户端请求的附加选项（Extra Options）的表示。

<a id="r_coap_5Fclient_5Frequest"></a>

```c
struct coap_client_request
```

相关声明：[coap_client_request](../network_application_model_reference/P004_coap_client_request_结构体.md)。

CoAP客户端请求（Client Request）的表示。

<a id="r_coap_5Fclient"></a>

```c
struct coap_client
```

相关声明：[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)。

CoAP客户端（Client）的表示。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 6.2\_宏定义（Macros）

<a id="r_ga53c57dcb241786b6e0213a7198667bd0"></a>

```c
#define MAX_COAP_MSG_LEN
```

相关声明：[MAX_COAP_MSG_LEN](#ga53c57dcb241786b6e0213a7198667bd0)。

CoAP 消息（Message）的最大大小。

<a id="r_ga8d16c1066c555e570a97569973809f68"></a>

```c
#define MAX_COAP_CLIENT_OPTION_LEN (12)
```

相关声明：[MAX_COAP_CLIENT_OPTION_LEN](#ga8d16c1066c555e570a97569973809f68)。

`coap_client_option` 中指定选项（Options）的最大字节长度。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 6.3\_类型定义（Typedefs）

<a id="r_ga37e6c0891c3e8eef3316e34d4b7a0318"></a>

```c
typedef void(* coap_client_response_cb_t) (const struct coap_client_response_data *data, void *user_data)
```

相关声明：[coap_client_response_cb_t](#ga37e6c0891c3e8eef3316e34d4b7a0318)、[coap_client_response_data](../network_application_model_reference/P005_coap_client_response_data_结构体.md)。

CoAP 请求（Request）回调。

<a id="r_ga3c35cc0227385124d0ebe25688e3bc1a"></a>

```c
typedef int(* coap_client_payload_cb_t) (size_t offset, const uint8_t **payload, size_t *len, bool *last_block, void *user_data)
```

相关声明：[coap_client_payload_cb_t](#ga3c35cc0227385124d0ebe25688e3bc1a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为 CoAP 请求提供载荷（Payload）的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 6.4\_函数（Functions）

<a id="r_gac85c4bcbc129b5d2be6a74f9024c84d9"></a>

```c
int coap_client_init (struct coap_client *client, const char *info)
```

相关声明：[coap_client_init](#gac85c4bcbc129b5d2be6a74f9024c84d9)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)。

初始化 CoAP 客户端（Client）。

<a id="r_gab5a2ea7ca1852e14142b579f77bc5bf9"></a>

```c
int coap_client_req (struct coap_client *client, int sock, const struct net_sockaddr *addr, struct coap_client_request *req, struct coap_transmission_parameters *params)
```

相关声明：[coap_client_req](#gab5a2ea7ca1852e14142b579f77bc5bf9)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[coap_client_request](../network_application_model_reference/P004_coap_client_request_结构体.md)、[coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)。

发送 CoAP 请求（Request）。

<a id="r_ga3f511d4df22bece05c1ac97ff4d09a80"></a>

```c
void coap_client_cancel_requests (struct coap_client *client)
```

相关声明：[coap_client_cancel_requests](#ga3f511d4df22bece05c1ac97ff4d09a80)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)。

取消当前全部请求（Requests）。

<a id="r_ga71abc48834df15e7550f7f9c75918117"></a>

```c
void coap_client_cancel_request (struct coap_client *client, struct coap_client_request *req)
```

相关声明：[coap_client_cancel_request](#ga71abc48834df15e7550f7f9c75918117)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)、[coap_client_request](../network_application_model_reference/P004_coap_client_request_结构体.md)。

取消匹配的请求（Matching Requests）。

<a id="r_ga7453fafdd924ae0728694e9fb62682aa"></a>

```c
int coap_client_deregister_observe (struct coap_client *client, struct coap_client_request *req)
```

相关声明：[coap_client_deregister_observe](#ga7453fafdd924ae0728694e9fb62682aa)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)、[coap_client_request](../network_application_model_reference/P004_coap_client_request_结构体.md)。

注销匹配的 CoAP 观察订阅（Observe Subscriptions）。

<a id="r_ga17f5d111a03ca0c02b83f5ad96c1caa8"></a>

```c
int coap_client_reregister_observe (struct coap_client *client, struct coap_client_request *req)
```

相关声明：[coap_client_reregister_observe](#ga17f5d111a03ca0c02b83f5ad96c1caa8)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)、[coap_client_request](../network_application_model_reference/P004_coap_client_request_结构体.md)。

刷新，即重新注册（Re-register）正在进行的 CoAP 观察（Observation）。

<a id="r_ga437ead308ea92f314fd9ebb82a6300b7"></a>

```c
struct coap_client_option coap_client_option_initial_block2 (void)
```

相关声明：[coap_client_option](../network_application_model_reference/P003_coap_client_option_结构体.md)、[coap_client_option_initial_block2](#ga437ead308ea92f314fd9ebb82a6300b7)。

初始化要加入请求的 Block2 选项（Option）。

<a id="r_ga9460711a90567fccb810fb4d93dbe841"></a>

```c
bool coap_client_has_ongoing_exchange (struct coap_client *client)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_client_has_ongoing_exchange](#ga9460711a90567fccb810fb4d93dbe841)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)。

检查客户端是否存在正在进行的交换（Ongoing Exchange）。

## 6.5\_详细说明（Detailed Documentation）

<a id="ga8d16c1066c555e570a97569973809f68"></a>

### `MAX_COAP_CLIENT_OPTION_LEN`

```c
#define MAX_COAP_CLIENT_OPTION_LEN (12)
```

```c
#include <zephyr/net/coap_client.h>
```

`coap_client_option` 中指定选项（Options）的最大字节长度。

<a id="ga53c57dcb241786b6e0213a7198667bd0"></a>

### `MAX_COAP_MSG_LEN`

```c
#define MAX_COAP_MSG_LEN
```

```c
#include <zephyr/net/coap_client.h>
```

展开值（Value）：

```c
(CONFIG_COAP_CLIENT_MESSAGE_HEADER_SIZE + \
CONFIG_COAP_CLIENT_MESSAGE_SIZE)
```

CoAP 消息（Message）的最大大小。

<a id="ga3c35cc0227385124d0ebe25688e3bc1a"></a>

### `coap_client_payload_cb_t`

```c
typedef int(* coap_client_payload_cb_t) (size_t offset, const uint8_t **payload, size_t *len, bool *last_block, void *user_data)
```

```c
#include <zephyr/net/coap_client.h>
```

为 CoAP 请求提供载荷（Payload）的回调。

为 CoAP 客户端请求提供负载（Payload）的可选回调。如果在 coap_client_request 中设置了它，CoAP 客户端库会在准备 PUT/POST 请求时调用此回调。

调用时，库向应用提供本次传输的当前负载偏移量（Payload Offset）和负载块大小（Payload Block Size）；应用则设置负载指针、负载大小以及是否预期还有更多数据块。在首次回调时将 last_block 参数设为 false，会触发分块传输上传（Block Transfer Upload）。库持续调用回调，直到 last_block 参数被设为 true。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `offset` | 载荷相对于分块传输（Blockwise Transfer）起点的偏移量。 |
| `payload` | 指向包含负载块（Payload Block）的缓冲区的指针。 |
| `len` | 输入时为请求的最大块大小（Block Size）；输出时为实际负载长度（Payload Length）。 |
| `last_block` | 指向标志的指针，该标志表示是否预期还有更多负载块（Payload Blocks）。 |
| `user_data` | 用户提供的上下文（Context）。 |

**说明（Note）**：注意（Note）：使用分块传输（Block Transfer）时，应用应提供完整大小的负载块。只有最后一块，即 last_block 设为 true 时，才可以短于所请求的块大小。

返回（Returns）：成功时为 0；返回负错误码可中止上传（Abort Upload）。

<a id="ga37e6c0891c3e8eef3316e34d4b7a0318"></a>

### `coap_client_response_cb_t`

```c
typedef void(* coap_client_response_cb_t) (const struct coap_client_response_data *data, void *user_data)
```

```c
#include <zephyr/net/coap_client.h>
```

CoAP 请求（Request）回调。

收到 CoAP 客户端请求的响应时调用此回调，用于报告错误、服务器响应码或传送负载（Payload）。分块传输（Blockwise Transfers）会依次调用此回调，负载偏移量递增，而 payload 参数指向的缓冲区每次仅包含部分内容。

对于组播请求（Multicast Requests），每个响应服务器都会触发一次回调，source 设置为该服务器的单播源地址（Unicast Source Address）。收集窗口（Collection Window）到期时，最后再调用一次回调，并将 source 设置为 NULL，表示此请求不会再收到后续响应。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `data` | CoAP 响应数据（Response Data）。 |
| `user_data` | 用户提供的上下文（Context）。 |

<a id="ga71abc48834df15e7550f7f9c75918117"></a>

### `coap_client_cancel_request()`

```c
void coap_client_cancel_request ( struct coap_client * client, struct coap_client_request * req )
```

```c
#include <zephyr/net/coap_client.h>
```

取消匹配的请求（Matching Requests）。

此函数取消所有匹配给定请求的 CoAP 客户端请求。匹配依据是 method、path、callback 以及所提供的 user_data；任何设置为 NULL 的字段都视为通配符（Wildcard）。

`(struct coap_client_request){0}` 取消全部请求。`(struct coap_client_request){.method = COAP_METHOD_GET}` 取消全部 GET 请求。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 指向 CoAP 客户端实例（Client Instance）的指针。 |
| `req` | 指向待取消的 CoAP 客户端请求（Client Request）的指针。 |

<a id="ga3f511d4df22bece05c1ac97ff4d09a80"></a>

### `coap_client_cancel_requests()`

```c
void coap_client_cancel_requests ( struct coap_client * client)
```

```c
#include <zephyr/net/coap_client.h>
```

取消当前全部请求（Requests）。

此函数用于取消因某种原因已失效的长时间运行请求（Long-running Requests），例如设置了 OBSERVE 选项的 GET。关闭对应客户端套接字之前也应调用它，避免内部轮询线程（Polling Thread）继续监视该套接字。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 客户端实例（Client Instance）。 |

<a id="ga7453fafdd924ae0728694e9fb62682aa"></a>

### `coap_client_deregister_observe()`

```c
int coap_client_deregister_observe ( struct coap_client * client, struct coap_client_request * req )
```

```c
#include <zephyr/net/coap_client.h>
```

注销匹配的 CoAP 观察订阅（Observe Subscriptions）。

按照 RFC 7641 第 3.6 节，发送 Observe 选项为 1（注销，Deregister）的 GET，使用与原始观察请求（Observe Request）相同的令牌（Token）；CON/NON 类型与原始请求一致。

对于可确认请求（Confirmable Requests），操作是异步的：库负责重传，注销得到确认后，通过响应回调传递服务器的最终响应。

对于不可确认请求（Non-confirmable Requests），注销消息只发送一次，随后立即释放请求；调用响应回调并传入 -ECANCELED。

匹配规则（Matching Rules）与 coap_client_cancel_request 相同。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 指向 CoAP 客户端实例（Client Instance）的指针。 |
| `req` | 指向 CoAP 客户端请求（Client Request）的指针，用于匹配要注销的观察请求。 |

**返回（Returns）**：**返回值（Returns）：**成功返回 0，否则返回负错误码。

<a id="ga9460711a90567fccb810fb4d93dbe841"></a>

### `coap_client_has_ongoing_exchange()`

```c
bool coap_client_has_ongoing_exchange ( struct coap_client * client)
```

```c
#include <zephyr/net/coap_client.h>
```

检查客户端是否存在正在进行的交换（Ongoing Exchange）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 指向 CoAP 客户端实例（Client Instance）的指针。 |

**说明（Note）**：注意（Note）：函数不仅考虑正在进行的请求，还考虑已完成请求的存续时间（Lifetime），以妥善处理重复消息。此函数用于套接字处理，但不考虑在本次调用之前就已启动的套接字 POLL。因此，建议在关闭套接字之前等待 POLL 超时结束，例如调用 coap_client_cancel_requests()，它会施加覆盖该超时的延迟。

返回（Returns）：存在正在进行的交换（Exchange）时为 true，否则为 false。

<a id="gac85c4bcbc129b5d2be6a74f9024c84d9"></a>

### `coap_client_init()`

```c
int coap_client_init ( struct coap_client * client, const char * info )
```

```c
#include <zephyr/net/coap_client.h>
```

初始化 CoAP 客户端（Client）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[in] client` | 客户端实例（Client Instance）。 |
| `[in] info` | 客户端接收线程（Receiving Thread）的名称。设置为 NULL 时，使用默认名称 "coap_client"。 |

返回（Returns）：int，成功时为 0，否则为负错误码。

<a id="ga437ead308ea92f314fd9ebb82a6300b7"></a>

### `coap_client_option_initial_block2()`

```c
struct coap_client_option coap_client_option_initial_block2 ( void )
```

```c
#include <zephyr/net/coap_client.h>
```

初始化要加入请求的 Block2 选项（Option）。

如果应用预计请求需要分块传输（Blockwise Transfer），可以预先向服务器建议最大块大小；参见 RFC 7959 图 3：提前协商的分块 GET（Block-Wise GET with Early Negotiation）。

此辅助函数返回一个 Block2 选项（Option），用于随初始请求发送。

返回（Returns）：CoAP 客户端的初始 Block2 选项结构体（Option Structure）。

<a id="gab5a2ea7ca1852e14142b579f77bc5bf9"></a>

### `coap_client_req()`

```c
int coap_client_req ( struct coap_client * client, int sock, const struct net_sockaddr * addr, struct coap_client_request * req, struct coap_transmission_parameters * params )
```

```c
#include <zephyr/net/coap_client.h>
```

发送 CoAP 请求（Request）。

操作由后台线程（Background Thread）异步处理。套接字尚未连接目标地址时，用户必须提供目标地址；否则应将地址设置为 NULL。回调被调用且最后一块标志为 true 后，可以关闭套接字或将其用于另一项查询。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 客户端实例（Client Instance）。 |
| `sock` | 已打开的套接字文件描述符（Socket File Descriptor）。 |
| `addr` | 请求的目标地址（Destination Address）；套接字已连接时为 NULL。 |
| `req` | CoAP 请求结构体（Request Structure）。 |
| `params` | 指向传输参数结构体（Transmission Parameters Structure）的指针；使用默认值时传入 NULL。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 请求已启动（Request Started）。 |
| `-EINVAL` | 参数或请求无效（Invalid Argument or Request）。 |
| `-EAGAIN` | 没有空闲请求槽位（Request Slot）。 |
| `-EALREADY` | 另一套接字上有正在进行的请求。 |
| `-ENOTSUP` | 不支持的地址族（Address Family）。 |
| `<0` | 构造或发送请求失败时，返回其他负错误码。 |

**说明（Note）**：注意（Note）：使用分块传输（Block Transfer）时，req 参数中提供的负载指针（Payload Pointer）必须在整个事务期间保持有效，直到报告最后一块或错误。发送后续负载块时，库需要访问该指针。应用不得对同一目标资源注册多个观察（Observations），参见 RFC 7641 第 3.1 节；应使用 coap_client_reregister_observe() 刷新正在进行的观察。

<a id="ga17f5d111a03ca0c02b83f5ad96c1caa8"></a>

### `coap_client_reregister_observe()`

```c
int coap_client_reregister_observe ( struct coap_client * client, struct coap_client_request * req )
```

```c
#include <zephyr/net/coap_client.h>
```

刷新，即重新注册（Re-register）正在进行的 CoAP 观察（Observation）。

重新发送观察请求的 GET，Observe 选项设为 0（注册，Register），使用与原始请求相同的令牌及选项，即 RFC 7641 的重新注册（Re-registration）。这会刷新服务器上的观察条目，例如在 Max-Age 或服务器端空闲超时到期前刷新，而不会创建第二个观察。服务器以当前资源状态应答，并通过既有观察回调传递。观察会继续，除非应答不是包含 Observe 选项的 2.xx 响应，此时观察结束，参见 RFC 7641 第 3.2 节和第 4.1 节。

构造或发送刷新请求失败时，保留既有观察（Observation），之后刷新仍可能成功；返回错误，但不调用回调。服务器未确认的可确认刷新请求（Confirmable Refresh）会像其他可确认请求一样重传；重试次数耗尽后，结束观察并向回调报告 -ETIMEDOUT。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `client` | 指向客户端实例（Client Instance）的指针。 |
| `req` | 标识观察（Observation）的指针，依据与注册它的 coap_client_req() 相同的字段匹配，即 method、path、cb 和 user_data。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功。 |
| `-ENOENT` | 没有正在进行的观察（Observation）与 req 匹配，例如它已因超时、服务器发出的 Reset 或导致观察结束的服务器响应而终止。 |
| `-EBUSY` | 该观察（Observation）中仍有请求正在等待响应，例如初始注册、先前的可确认刷新请求或正在获取的分块通知；或者函数是在该观察的响应回调中调用的。请稍后重试。 |
| `<0` | 构造或发送请求失败时，返回其他负错误码。 |


## 6.6\_原页交叉引用（Cross References）

- [coap_client_response_data](../network_application_model_reference/P005_coap_client_response_data_结构体.md)
- [coap_client_option](../network_application_model_reference/P003_coap_client_option_结构体.md)
- [coap_client_request](../network_application_model_reference/P004_coap_client_request_结构体.md)
- [coap_client](../network_application_model_reference/P002_coap_client_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)
- [zephyr/net/coap_client.h](../api_file_protocol_service_reference/P008_zephyr__net__coap_client.h_文件参考.md)
- [RFC 7641, section-3.6](https://datatracker.ietf.org/doc/html/rfc7641#section-3.6)
- [RFC 7959](https://datatracker.ietf.org/doc/html/rfc7959)
- [RFC 7641, section-3.1](https://datatracker.ietf.org/doc/html/rfc7641#section-3.1)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P005_微芯（Microchip）SAM D5x_E5x.md) · [返回大纲](大纲.md) · [下一章](P007_CoAP TCP客户端（Client）的API。.md)
