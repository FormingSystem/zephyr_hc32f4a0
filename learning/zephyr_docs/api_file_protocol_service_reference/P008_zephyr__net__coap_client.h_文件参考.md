---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-8
title: zephyr__net__coap_client.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap__client_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_zephyr\_\_net\_\_coap\_client.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/coap__client_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP客户端（Client）的API。

<a id="details"></a>

```c
#include <zephyr/net/coap.h>
#include <zephyr/kernel.h>
```

查看此文件的源码。

受限应用协议（CoAP）客户端 API，供应用发起 CoAP 请求（Requests）。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 8.1\_数据结构（Data Structures）

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

## 8.2\_宏定义（Macros）

<a id="r_ga53c57dcb241786b6e0213a7198667bd0"></a>

```c
#define MAX_COAP_MSG_LEN
```

相关声明：[MAX_COAP_MSG_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga53c57dcb241786b6e0213a7198667bd0)。

CoAP 消息（Message）的最大大小。

<a id="r_ga8d16c1066c555e570a97569973809f68"></a>

```c
#define MAX_COAP_CLIENT_OPTION_LEN (12)
```

相关声明：[MAX_COAP_CLIENT_OPTION_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga8d16c1066c555e570a97569973809f68)。

`coap_client_option` 中指定选项（Options）的最大字节长度。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 8.3\_类型定义（Typedefs）

<a id="r_ga37e6c0891c3e8eef3316e34d4b7a0318"></a>

```c
typedef void(* coap_client_response_cb_t) (const struct coap_client_response_data *data, void *user_data)
```

相关声明：[coap_client_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga37e6c0891c3e8eef3316e34d4b7a0318)、[coap_client_response_data](../network_application_model_reference/P005_coap_client_response_data_结构体.md)。

CoAP 请求（Request）回调。

<a id="r_ga3c35cc0227385124d0ebe25688e3bc1a"></a>

```c
typedef int(* coap_client_payload_cb_t) (size_t offset, const uint8_t **payload, size_t *len, bool *last_block, void *user_data)
```

相关声明：[coap_client_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga3c35cc0227385124d0ebe25688e3bc1a)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

为 CoAP 请求提供载荷（Payload）的回调。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.4\_函数（Functions）

<a id="r_gac85c4bcbc129b5d2be6a74f9024c84d9"></a>

```c
int coap_client_init (struct coap_client *client, const char *info)
```

相关声明：[coap_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#gac85c4bcbc129b5d2be6a74f9024c84d9)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)。

初始化 CoAP 客户端（Client）。

<a id="r_gab5a2ea7ca1852e14142b579f77bc5bf9"></a>

```c
int coap_client_req (struct coap_client *client, int sock, const struct net_sockaddr *addr, struct coap_client_request *req, struct coap_transmission_parameters *params)
```

相关声明：[coap_client_req](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#gab5a2ea7ca1852e14142b579f77bc5bf9)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[coap_client_request](../network_application_model_reference/P004_coap_client_request_结构体.md)、[coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)。

发送 CoAP 请求（Request）。

<a id="r_ga3f511d4df22bece05c1ac97ff4d09a80"></a>

```c
void coap_client_cancel_requests (struct coap_client *client)
```

相关声明：[coap_client_cancel_requests](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga3f511d4df22bece05c1ac97ff4d09a80)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)。

取消当前全部请求（Requests）。

<a id="r_ga71abc48834df15e7550f7f9c75918117"></a>

```c
void coap_client_cancel_request (struct coap_client *client, struct coap_client_request *req)
```

相关声明：[coap_client_cancel_request](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga71abc48834df15e7550f7f9c75918117)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)、[coap_client_request](../network_application_model_reference/P004_coap_client_request_结构体.md)。

取消匹配的请求（Matching Requests）。

<a id="r_ga7453fafdd924ae0728694e9fb62682aa"></a>

```c
int coap_client_deregister_observe (struct coap_client *client, struct coap_client_request *req)
```

相关声明：[coap_client_deregister_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga7453fafdd924ae0728694e9fb62682aa)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)、[coap_client_request](../network_application_model_reference/P004_coap_client_request_结构体.md)。

注销匹配的 CoAP 观察订阅（Observe Subscriptions）。

<a id="r_ga17f5d111a03ca0c02b83f5ad96c1caa8"></a>

```c
int coap_client_reregister_observe (struct coap_client *client, struct coap_client_request *req)
```

相关声明：[coap_client_reregister_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga17f5d111a03ca0c02b83f5ad96c1caa8)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)、[coap_client_request](../network_application_model_reference/P004_coap_client_request_结构体.md)。

刷新，即重新注册（Re-register）正在进行的 CoAP 观察（Observation）。

<a id="r_ga437ead308ea92f314fd9ebb82a6300b7"></a>

```c
struct coap_client_option coap_client_option_initial_block2 (void)
```

相关声明：[coap_client_option](../network_application_model_reference/P003_coap_client_option_结构体.md)、[coap_client_option_initial_block2](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga437ead308ea92f314fd9ebb82a6300b7)。

初始化要加入请求的 Block2 选项（Option）。

<a id="r_ga9460711a90567fccb810fb4d93dbe841"></a>

```c
bool coap_client_has_ongoing_exchange (struct coap_client *client)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_client_has_ongoing_exchange](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga9460711a90567fccb810fb4d93dbe841)、[coap_client](../network_application_model_reference/P002_coap_client_结构体.md)。

检查客户端是否存在正在进行的交换（Ongoing Exchange）。


## 8.5\_原页交叉引用（Cross References）

- [zephyr/net/coap.h](../api_source_transport_clock_reference/P006_coap.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [查看此文件的源码。](../api_source_system_reference/P006_coap_client.h_源码浏览.md)
- [coap_client_response_data](../network_application_model_reference/P005_coap_client_response_data_结构体.md)
- [coap_client_option](../network_application_model_reference/P003_coap_client_option_结构体.md)
- [coap_client_request](../network_application_model_reference/P004_coap_client_request_结构体.md)
- [coap_client](../network_application_model_reference/P002_coap_client_结构体.md)
- [MAX_COAP_MSG_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga53c57dcb241786b6e0213a7198667bd0)
- [MAX_COAP_CLIENT_OPTION_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga8d16c1066c555e570a97569973809f68)
- [coap_client_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga37e6c0891c3e8eef3316e34d4b7a0318)
- [coap_client_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga3c35cc0227385124d0ebe25688e3bc1a)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [coap_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#gac85c4bcbc129b5d2be6a74f9024c84d9)
- [coap_client_req](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#gab5a2ea7ca1852e14142b579f77bc5bf9)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)
- [coap_client_cancel_requests](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga3f511d4df22bece05c1ac97ff4d09a80)
- [coap_client_cancel_request](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga71abc48834df15e7550f7f9c75918117)
- [coap_client_deregister_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga7453fafdd924ae0728694e9fb62682aa)
- [coap_client_reregister_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga17f5d111a03ca0c02b83f5ad96c1caa8)
- [coap_client_option_initial_block2](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga437ead308ea92f314fd9ebb82a6300b7)
- [coap_client_has_ongoing_exchange](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga9460711a90567fccb810fb4d93dbe841)

<a id="header-details"></a>

---

[上一章](P007_zephyr__dt-bindings__pinctrl__ch32h41x-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P009_zephyr__data__cobs.h_文件参考.md)
