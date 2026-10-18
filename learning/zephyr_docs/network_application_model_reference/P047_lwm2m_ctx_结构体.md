---
id: learning.zephyr-docs.network-application-model-reference.page-47
title: lwm2m_ctx_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__ctx.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第47章\_lwm2m\_ctx\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structlwm2m__ctx.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

用于维护单个轻量级M2M（LwM2M）连接信息的上下文结构。

```c
#include <zephyr/net/lwm2m.h>
```

<a id="details"></a>

用于维护单个轻量级M2M（LwM2M）连接信息的上下文结构。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 47.1\_数据成员（Data Fields）

```c
union {
```

<a id="r_a37eed28eb9d71e2eb14edeacea4f88fe"></a>

```c
struct net_sockaddr_storage remote_addr_storage
```

相关声明：[remote_addr_storage](#ae8d889dafd8df676e76542d5a65a8dfc)。

目的地址（Destination Address）。

<a id="r_afba53f6a0fd5a11cb3ecd4eee744233e"></a>

```c
};
```

目的地址存储（Destination Address Storage）。

<a id="r_a9b56ad9b3f2202d25b8c48f34a898dd3"></a>

```c
void * processed_req
```

相关声明：[processed_req](#a9b56ad9b3f2202d25b8c48f34a898dd3)。

指向当前处理请求的指针，供LwM2M引擎（Engine）内部使用。

<a id="r_a8714a3ee6870515631fd75e74644d39c"></a>

```c
lwm2m_set_sockopt_cb_t set_socketoptions
```

相关声明：[lwm2m_set_sockopt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga92d2227f37e7d382bc4f1a7bae21b872)、[set_socketoptions](#a8714a3ee6870515631fd75e74644d39c)。

自定义套接字选项（Socket Options）。

<a id="r_aeb1e3ffc83853f74f2201f582917c2ce"></a>

```c
bool use_dtls
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[use_dtls](#aeb1e3ffc83853f74f2201f582917c2ce)。

表示上下文是否应使用数据报TLS（DTLS）的标志。

<a id="r_aff523bc7473073c917ff1c888da7bece"></a>

```c
bool connection_suspended
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[connection_suspended](#aff523bc7473073c917ff1c888da7bece)。

表示套接字连接（Socket Connection）已挂起的标志。

<a id="r_ac6709d32a87ece72c7cdf283c4ff60c0"></a>

```c
bool buffer_client_messages
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[buffer_client_messages](#ac6709d32a87ece72c7cdf283c4ff60c0)。

表示客户端正在缓冲通知（Notifications）和发送消息（Send Messages）的标志。

<a id="r_ab5fe85963a265f9c059a25138a637e02"></a>

```c
int sec_obj_inst
```

相关声明：[sec_obj_inst](#ab5fe85963a265f9c059a25138a637e02)。

用于服务器凭据的安全对象（Security Object）的当前索引。

<a id="r_a76d92a14bf1729d7b0fee174c51ed4bf"></a>

```c
int srv_obj_inst
```

相关声明：[srv_obj_inst](#a76d92a14bf1729d7b0fee174c51ed4bf)。

此上下文所用服务器对象（Server Object）的当前索引。

<a id="r_aafa787c2b7ea7599c51d9247ea9f1090"></a>

```c
bool bootstrap_mode
```

相关声明：[bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)、[bootstrap_mode](#aafa787c2b7ea7599c51d9247ea9f1090)。

用于启用引导接口（BOOTSTRAP Interface）的标志。

<a id="r_afed1a599a72f131e4f196848c3e6fe85"></a>

```c
int sock_fd
```

相关声明：[sock_fd](#afed1a599a72f131e4f196848c3e6fe85)。

套接字文件描述符（Socket File Descriptor）。

<a id="r_a1b90780926f3cda2d48dfa8f94b1efd8"></a>

```c
lwm2m_socket_fault_cb_t fault_cb
```

相关声明：[lwm2m_socket_fault_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae7bf50f9abf1b82b76ac3e9175e685ac)、[fault_cb](#a1b90780926f3cda2d48dfa8f94b1efd8)。

套接字故障回调（Socket Fault Callback）。

<a id="r_a412bd706adcd17ec8c00f1779012a845"></a>

```c
lwm2m_observe_cb_t observe_cb
```

相关声明：[lwm2m_observe_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad7bea67e16e1e831e0f949dbf83d5afe)、[observe_cb](#a412bd706adcd17ec8c00f1779012a845)。

新建或取消观察（Observations），以及通知得到确认或超时时使用的回调。

<a id="r_ab01ec6be0effa24dde31363a476eccbb"></a>

```c
lwm2m_ctx_event_cb_t event_cb
```

相关声明：[lwm2m_ctx_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga38dbaf038426efc75d889c4a0666dac9)、[event_cb](#ab01ec6be0effa24dde31363a476eccbb)。

客户端事件（Client Events）的回调。

<a id="r_a574b50b9ec4cdfb5fac53a9b6d8c31d5"></a>

```c
uint8_t validate_buf [CONFIG_LWM2M_ENGINE_VALIDATION_BUFFER_SIZE]
```

相关声明：[uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[validate_buf](#a574b50b9ec4cdfb5fac53a9b6d8c31d5)。

验证缓冲区（Validation Buffer）。

<a id="r_ad3d66164415325e7009d1a4c1111f4b3"></a>

```c
void(* set_socket_state )(int fd, enum lwm2m_socket_states state)
```

相关声明：[set_socket_state](#ad3d66164415325e7009d1a4c1111f4b3)、[lwm2m_socket_states](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7611c1aebb0309ee8340e06dd8ee234d)、[state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)。

用于指示传输状态（Transmission States）的回调。

<a id="pub-attribs-0"></a>

### 数据报TLS相关信息（DTLS Related Information）

仅在启用CONFIG_LWM2M_DTLS_SUPPORT且lwm2m_ctx::use_dtls设为true时可用。

<a id="r_a6c4c9025a17a3dc3451651cb1f83d575"></a>

```c
int tls_tag
```

相关声明：[tls_tag](#a6c4c9025a17a3dc3451651cb1f83d575)。

TLS标签（Tag）由客户端设置，作为LwM2M引擎调用tls_credential_(add|delete)时的引用。

<a id="r_a342cb5a0aaf9e5bc53228d3b0cc0fd43"></a>

```c
char * desthostname
```

相关声明：[desthostname](#a342cb5a0aaf9e5bc53228d3b0cc0fd43)。

目的主机名（Destination Hostname）。

<a id="r_aff084b28e547a81bd71215125c28f705"></a>

```c
uint16_t desthostnamelen
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[desthostnamelen](#aff084b28e547a81bd71215125c28f705)。

目的主机名（Destination Hostname）的长度。

<a id="r_a5f17296cd4600b25515e0952dc61ea97"></a>

```c
int(* load_credentials )(struct lwm2m_ctx *client_ctx)
```

相关声明：[load_credentials](#a5f17296cd4600b25515e0952dc61ea97)、[lwm2m_ctx](P047_lwm2m_ctx_结构体.md)。

自定义load_credentials函数。

## 47.2\_详细说明（Detailed Documentation）

<a id="afba53f6a0fd5a11cb3ecd4eee744233e"></a>

### `[union]`

```c
union { ... } lwm2m_ctx
```

目的地址存储（Destination Address Storage）。

<a id="aafa787c2b7ea7599c51d9247ea9f1090"></a>

### `bootstrap_mode`

```c
bool lwm2m_ctx::bootstrap_mode
```

用于启用引导接口（BOOTSTRAP Interface）的标志。

更多信息见LwM2M技术规范的“引导接口（Bootstrap Interface）”一节。

<a id="ac6709d32a87ece72c7cdf283c4ff60c0"></a>

### `buffer_client_messages`

```c
bool lwm2m_ctx::buffer_client_messages
```

表示客户端正在缓冲通知（Notifications）和发送消息（Send Messages）的标志。

为true时缓冲通知（Notifications）和发送消息（Send Messages）。

<a id="aff523bc7473073c917ff1c888da7bece"></a>

### `connection_suspended`

```c
bool lwm2m_ctx::connection_suspended
```

表示套接字连接（Socket Connection）已挂起的标志。

在队列模式（Queue Mode）下，此值说明是否需要重新连接。

<a id="a342cb5a0aaf9e5bc53228d3b0cc0fd43"></a>

### `desthostname`

```c
char* lwm2m_ctx::desthostname
```

目的主机名（Destination Hostname）。

启用MBEDTLS服务器名称指示（SNI）时，必须为套接字设置目的服务器的主机名。

<a id="aff084b28e547a81bd71215125c28f705"></a>

### `desthostnamelen`

```c
uint16_t lwm2m_ctx::desthostnamelen
```

目的主机名（Destination Hostname）的长度。

<a id="ab01ec6be0effa24dde31363a476eccbb"></a>

### `event_cb`

```c
lwm2m_ctx_event_cb_t lwm2m_ctx::event_cb
```

客户端事件（Client Events）的回调。

<a id="a1b90780926f3cda2d48dfa8f94b1efd8"></a>

### `fault_cb`

```c
lwm2m_socket_fault_cb_t lwm2m_ctx::fault_cb
```

套接字故障回调（Socket Fault Callback）。

接收过程中发生套接字错误（Socket Errors）时，LwM2M处理线程将调用此回调。

<a id="a5f17296cd4600b25515e0952dc61ea97"></a>

### `load_credentials`

```c
int(* lwm2m_ctx::load_credentials) (struct lwm2m_ctx *client_ctx)
```

自定义load_credentials函数。

客户端可设置load_credentials函数，以覆盖lwm2m_engine.c中load_tls_credential()的默认行为。

<a id="a412bd706adcd17ec8c00f1779012a845"></a>

### `observe_cb`

```c
lwm2m_observe_cb_t lwm2m_ctx::observe_cb
```

新建或取消观察（Observations），以及通知得到确认或超时时使用的回调。

<a id="a9b56ad9b3f2202d25b8c48f34a898dd3"></a>

### `processed_req`

```c
void* lwm2m_ctx::processed_req
```

指向当前处理请求的指针，供LwM2M引擎（Engine）内部使用。

底层类型为struct lwm2m_message；由于该类型在私有头文件中声明且不向应用公开，因此这里用void指针存储。

<a id="ae8d889dafd8df676e76542d5a65a8dfc"></a>

### `remote_addr_storage`

```c
struct net_sockaddr_storage lwm2m_ctx::remote_addr_storage
```

目的地址（Destination Address）。

<a id="ab5fe85963a265f9c059a25138a637e02"></a>

### `sec_obj_inst`

```c
int lwm2m_ctx::sec_obj_inst
```

用于服务器凭据的安全对象（Security Object）的当前索引。

<a id="ad3d66164415325e7009d1a4c1111f4b3"></a>

### `set_socket_state`

```c
void(* lwm2m_ctx::set_socket_state) (int fd, enum lwm2m_socket_states state)
```

用于指示传输状态（Transmission States）的回调。

客户端应用可以请求LwM2M引擎提供传输状态提示（Transmission State Hints），并利用这些信息控制各种省电模式。

<a id="a8714a3ee6870515631fd75e74644d39c"></a>

### `set_socketoptions`

```c
lwm2m_set_sockopt_cb_t lwm2m_ctx::set_socketoptions
```

自定义套接字选项（Socket Options）。

客户端可提供回调，以覆盖默认套接字选项（Socket Options）；该回调在套接字创建之后、connect之前调用。

<a id="afed1a599a72f131e4f196848c3e6fe85"></a>

### `sock_fd`

```c
int lwm2m_ctx::sock_fd
```

套接字文件描述符（Socket File Descriptor）。

<a id="a76d92a14bf1729d7b0fee174c51ed4bf"></a>

### `srv_obj_inst`

```c
int lwm2m_ctx::srv_obj_inst
```

此上下文所用服务器对象（Server Object）的当前索引。

<a id="a6c4c9025a17a3dc3451651cb1f83d575"></a>

### `tls_tag`

```c
int lwm2m_ctx::tls_tag
```

TLS标签（Tag）由客户端设置，作为LwM2M引擎调用tls_credential_(add|delete)时的引用。

<a id="aeb1e3ffc83853f74f2201f582917c2ce"></a>

### `use_dtls`

```c
bool lwm2m_ctx::use_dtls
```

表示上下文是否应使用数据报TLS（DTLS）的标志。

在连接信息中使用coaps://协议前缀来启用。注意（NOTE）：需要CONFIG_LWM2M_DTLS_SUPPORT。

<a id="a574b50b9ec4cdfb5fac53a9b6d8c31d5"></a>

### `validate_buf`

```c
uint8_t lwm2m_ctx::validate_buf[CONFIG_LWM2M_ENGINE_VALIDATION_BUFFER_SIZE]
```

验证缓冲区（Validation Buffer）。

在验证（Validation）之前，用作解码资源值的临时缓冲区；验证成功后，将其内容复制到实际资源缓冲区。

本数据类型文档由以下文件生成：

- `zephyr/net/lwm2m.h`

## 47.3\_原页交叉引用（Cross References）

- [zephyr/net/lwm2m.h](https://docs.zephyrproject.org/latest/doxygen/html/lwm2m_8h_source.html)
- [lwm2m_set_sockopt_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga92d2227f37e7d382bc4f1a7bae21b872)
- [bool](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html#abb452686968e48b67397da5f97445f5b)
- [lwm2m_socket_fault_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gae7bf50f9abf1b82b76ac3e9175e685ac)
- [lwm2m_observe_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#gad7bea67e16e1e831e0f949dbf83d5afe)
- [lwm2m_ctx_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga38dbaf038426efc75d889c4a0666dac9)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [lwm2m_socket_states](https://docs.zephyrproject.org/latest/doxygen/html/group__lwm2m__api.html#ga7611c1aebb0309ee8340e06dd8ee234d)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [CONFIG_LWM2M_DTLS_SUPPORT](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_LWM2M_DTLS_SUPPORT)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [lwm2m_ctx](P047_lwm2m_ctx_结构体.md)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P046_http_service_h3_config_结构体.md) · [返回大纲](大纲.md) · [下一章](P048_lwm2m_obj_path_结构体.md)
