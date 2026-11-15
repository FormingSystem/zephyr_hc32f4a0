---
id: learning.zephyr-docs.network-application-model-reference.page-16
title: coap_resource_结构体
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structcoap__resource.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第16章\_coap\_resource\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structcoap__resource.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP资源（Resource）的描述。

```c
#include <zephyr/net/coap.h>
```

<a id="details"></a>

CoAP资源（Resource）的描述。CoAP服务器通常需要注册资源，使客户端能够获取资源状态或请求更新资源。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 16.1\_数据成员（Data Fields）

<a id="r_aebe880e3ccbd2441854dfa899dc72c13"></a>

```c
coap_method_t get
```

相关声明：[coap_method_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03129c8f853862f8395cc567edbf4642)、[get](#aebe880e3ccbd2441854dfa899dc72c13)。

为各个CoAP方法（Method）指定要调用的函数。

<a id="r_a1efed8197d44aba3b63aaa9d9bb0f5bb"></a>

```c
coap_method_t post
```

相关声明：[coap_method_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03129c8f853862f8395cc567edbf4642)、[post](#a1efed8197d44aba3b63aaa9d9bb0f5bb)。

<a id="r_a3152a778e27e36fad7dd62985621d58b"></a>

```c
coap_method_t put
```

相关声明：[coap_method_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03129c8f853862f8395cc567edbf4642)、[put](#a3152a778e27e36fad7dd62985621d58b)。

<a id="r_a77dfb6d59c25e6e58141226023bf59ea"></a>

```c
coap_method_t del
```

相关声明：[coap_method_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03129c8f853862f8395cc567edbf4642)、[del](#a77dfb6d59c25e6e58141226023bf59ea)。

<a id="r_a6975e84ebc67d6aff2efb755695518f5"></a>

```c
coap_method_t fetch
```

相关声明：[coap_method_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03129c8f853862f8395cc567edbf4642)、[fetch](#a6975e84ebc67d6aff2efb755695518f5)。

<a id="r_aa0a5465fc5b49a566e3803a9f1638724"></a>

```c
coap_method_t patch
```

相关声明：[coap_method_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03129c8f853862f8395cc567edbf4642)、[patch](#aa0a5465fc5b49a566e3803a9f1638724)。

<a id="r_a7657cb2e9bbac7f98e35b4ed33f13163"></a>

```c
coap_method_t ipatch
```

相关声明：[coap_method_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03129c8f853862f8395cc567edbf4642)、[ipatch](#a7657cb2e9bbac7f98e35b4ed33f13163)。

<a id="r_a3199679fd990d757e9a500fbd7c653d7"></a>

```c
coap_notify_t notify
```

相关声明：[coap_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga4180b2476430fbe4a5e0418fb628ea91)、[notify](#a3199679fd990d757e9a500fbd7c653d7)。

要调用的通知函数（Notify Function）。

<a id="r_ada7a41309b6ca11612b17fabf6cd56c5"></a>

```c
const char *const * path
```

相关声明：[path](#ada7a41309b6ca11612b17fabf6cd56c5)。

资源路径（Resource Path）。

<a id="r_a202a83a5aa024a62bd25cc40f42e8d65"></a>

```c
void * user_data
```

相关声明：[user_data](#a202a83a5aa024a62bd25cc40f42e8d65)。

用户专用的不透明数据（Opaque Data）。

<a id="r_a6c1fe25539ecbe4ec2ed7446fff84861"></a>

```c
struct coap_core_metadata * metadata
```

相关声明：[coap_core_metadata](P008_coap_core_metadata_结构体.md)、[metadata](#a6c1fe25539ecbe4ec2ed7446fff84861)。

用于“.well-known/core”响应的资源元数据（Resource Metadata）。

<a id="r_a5035dc9c88c2b0ae557608e34ec14433"></a>

```c
sys_slist_t observers
```

相关声明：[sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)、[observers](#a5035dc9c88c2b0ae557608e34ec14433)。

资源观察者（Resource Observers）的列表。

<a id="r_ae8e1b2b1920689913e0910a82a30e009"></a>

```c
int age
```

相关声明：[age](#ae8e1b2b1920689913e0910a82a30e009)。

资源年龄（Resource Age）。

## 16.2\_详细说明（Detailed Documentation）

<a id="ae8e1b2b1920689913e0910a82a30e009"></a>

### `age`

```c
int coap_resource::age
```

资源年龄（Resource Age）。

<a id="a77dfb6d59c25e6e58141226023bf59ea"></a>

### `del`

```c
coap_method_t coap_resource::del
```

<a id="a6975e84ebc67d6aff2efb755695518f5"></a>

### `fetch`

```c
coap_method_t coap_resource::fetch
```

<a id="aebe880e3ccbd2441854dfa899dc72c13"></a>

### `get`

```c
coap_method_t coap_resource::get
```

为各个CoAP方法（Method）指定要调用的函数。

<a id="a7657cb2e9bbac7f98e35b4ed33f13163"></a>

### `ipatch`

```c
coap_method_t coap_resource::ipatch
```

<a id="a6c1fe25539ecbe4ec2ed7446fff84861"></a>

### `metadata`

```c
struct coap_core_metadata* coap_resource::metadata
```

用于“.well-known/core”响应的资源元数据（Resource Metadata）。

<a id="a3199679fd990d757e9a500fbd7c653d7"></a>

### `notify`

```c
coap_notify_t coap_resource::notify
```

要调用的通知函数（Notify Function）。

<a id="a5035dc9c88c2b0ae557608e34ec14433"></a>

### `observers`

```c
sys_slist_t coap_resource::observers
```

资源观察者（Resource Observers）的列表。

<a id="aa0a5465fc5b49a566e3803a9f1638724"></a>

### `patch`

```c
coap_method_t coap_resource::patch
```

<a id="ada7a41309b6ca11612b17fabf6cd56c5"></a>

### `path`

```c
const char* const* coap_resource::path
```

资源路径（Resource Path）。

<a id="a1efed8197d44aba3b63aaa9d9bb0f5bb"></a>

### `post`

```c
coap_method_t coap_resource::post
```

<a id="a3152a778e27e36fad7dd62985621d58b"></a>

### `put`

```c
coap_method_t coap_resource::put
```

<a id="a202a83a5aa024a62bd25cc40f42e8d65"></a>

### `user_data`

```c
void* coap_resource::user_data
```

用户专用的不透明数据（Opaque Data）。

本数据类型文档由以下文件生成：

- `zephyr/net/coap.h`

## 16.3\_原页交叉引用（Cross References）

- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h_source.html)
- [coap_method_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03129c8f853862f8395cc567edbf4642)
- [coap_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga4180b2476430fbe4a5e0418fb628ea91)
- [coap_core_metadata](P008_coap_core_metadata_结构体.md)
- [sys_slist_t](../slist_reference/P001_单向链表公共接口.md#ga44658c336b634c03938a251cdc8134f8)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P015_coap_reply_结构体.md) · [返回大纲](大纲.md) · [下一章](P017_coap_transmission_parameters_结构体.md)
