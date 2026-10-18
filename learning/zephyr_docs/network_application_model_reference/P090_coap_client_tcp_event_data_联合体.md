---
id: learning.zephyr-docs.network-application-model-reference.page-90
title: coap_client_tcp_event_data_联合体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/unioncoap__client__tcp__event__data.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第90章\_coap\_client\_tcp\_event\_data\_联合体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/unioncoap__client__tcp__event__data.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP TCP信令事件（Signaling Events）的事件数据。

```c
#include <zephyr/net/coap_client_tcp.h>
```

<a id="details"></a>

CoAP TCP信令事件（Signaling Events）的事件数据。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 90.1\_数据成员（Data Fields）

```c
struct {
```

<a id="r_a15a73cf6e1168485e1fe794ed3ac6ffd"></a>

```c
const char * alt_addr
```

相关声明：[alt_addr](#acfe56555936d032169ab875ec61aa385)。

重新连接的备用地址（Alternative Address）；未提供时为NULL。

<a id="r_a2db283abea7cd97112a1e48dc87e28ed"></a>

```c
uint32_t hold_off_sec
```

相关声明：[uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)、[hold_off_sec](#a71afec4e9cff19d0d5f140f0683f7018)。

重新连接前的等待时间（Hold-Off Time），单位为秒。

<a id="r_aabf0c77c120433b0ac1d8ff71d938717"></a>

```c
} release
```

相关声明：[release](#aabf0c77c120433b0ac1d8ff71d938717)。

释放事件（RELEASE）的数据。

```c
struct {
```

<a id="r_ad1fc0c68a84e053eece9f5dc3880c464"></a>

```c
uint16_t bad_csm_option
```

相关声明：[uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)、[bad_csm_option](#acc9999996b787c1b58205a72aa6e3aef)。

导致中止的错误能力与设置消息（CSM）选项代码；未提供时为0。

<a id="r_a9aa489304b706749b9271d2500867f5c"></a>

```c
} abort
```

相关声明：[abort](#a9aa489304b706749b9271d2500867f5c)。

中止事件（ABORT）的数据。

## 90.2\_详细说明（Detailed Documentation）

<a id="a9aa489304b706749b9271d2500867f5c"></a>

### `[struct]`

```c
struct { ... } coap_client_tcp_event_data::abort
```

中止事件（ABORT）的数据。

<a id="acfe56555936d032169ab875ec61aa385"></a>

### `alt_addr`

```c
const char* coap_client_tcp_event_data::alt_addr
```

重新连接的备用地址（Alternative Address）；未提供时为NULL。

<a id="acc9999996b787c1b58205a72aa6e3aef"></a>

### `bad_csm_option`

```c
uint16_t coap_client_tcp_event_data::bad_csm_option
```

导致中止的错误能力与设置消息（CSM）选项代码；未提供时为0。

<a id="a71afec4e9cff19d0d5f140f0683f7018"></a>

### `hold_off_sec`

```c
uint32_t coap_client_tcp_event_data::hold_off_sec
```

重新连接前的等待时间（Hold-Off Time），单位为秒。

<a id="aabf0c77c120433b0ac1d8ff71d938717"></a>

### `[struct]`

```c
struct { ... } coap_client_tcp_event_data::release
```

释放事件（RELEASE）的数据。

本数据类型文档由以下文件生成：

- `zephyr/net/coap_client_tcp.h`

## 90.3\_原页交叉引用（Cross References）

- [zephyr/net/coap_client_tcp.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__client__tcp_8h_source.html)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P089_websocket_request_结构体.md) · [返回大纲](大纲.md) · [下一章](P091_mqtt_evt_param_联合体.md)
