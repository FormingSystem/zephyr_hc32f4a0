---
id: learning.zephyr-docs.api-file-coap-phy-reference.page-3
title: zephyr__net__coap.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_net\_\_coap.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Zephyr的受限应用协议（CoAP）实现。

<a id="details"></a>

```c
#include <zephyr/types.h>
#include <stddef.h>
#include <stdbool.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/sys/math_extras.h>
#include <zephyr/sys/slist.h>
```

查看此文件的源码。

Zephyr的受限应用协议（CoAP）实现。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_coap_5Fresource"></a>

```c
struct coap_resource
```

相关声明：[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)。

CoAP资源（Resource）的描述。

<a id="r_coap_5Fobserver"></a>

```c
struct coap_observer
```

相关声明：[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)。

表示正在观察（Observe）本地资源的远端设备。

<a id="r_coap_5Fpacket"></a>

```c
struct coap_packet
```

相关声明：[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

CoAP数据包（Packet）的表示。

<a id="r_coap_5Foption"></a>

```c
struct coap_option
```

相关声明：[coap_option](../network_application_model_reference/P010_coap_option_结构体.md)。

CoAP选项（Option）的表示。

<a id="r_coap_5Ftransmission_5Fparameters"></a>

```c
struct coap_transmission_parameters
```

相关声明：[coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)。

CoAP传输参数（Transmission Parameters）。

<a id="r_coap_5Fpending"></a>

```c
struct coap_pending
```

相关声明：[coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)。

表示正在等待确认（ACK）的请求。

<a id="r_coap_5Freply"></a>

```c
struct coap_reply
```

相关声明：[coap_reply](../network_application_model_reference/P015_coap_reply_结构体.md)。

表示请求应答的处理程序（Reply Handler）；观察资源时也会使用它。

<a id="r_coap_5Fblock_5Fcontext"></a>

```c
struct coap_block_context
```

相关声明：[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)。

表示分块事务（Block-Wise Transaction）的当前状态。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 3.2\_宏定义（Macros）

<a id="r_gabdcc1f443e89bd035522cbab7dfee879"></a>

```c
#define COAP_MAKE_RESPONSE_CODE(class, det)
```

相关声明：[COAP_MAKE_RESPONSE_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gabdcc1f443e89bd035522cbab7dfee879)。

用于创建受限应用协议响应码（CoAP Response Code）的实用宏。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 3.3\_类型定义（Typedefs）

<a id="r_ga03129c8f853862f8395cc567edbf4642"></a>

```c
typedef int(* coap_method_t) (struct coap_resource *resource, struct coap_packet *request, struct net_sockaddr *addr, net_socklen_t addr_len)
```

相关声明：[coap_method_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03129c8f853862f8395cc567edbf4642)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

远端实体调用资源方法（Resource Method）时执行的回调类型。

<a id="r_ga4180b2476430fbe4a5e0418fb628ea91"></a>

```c
typedef void(* coap_notify_t) (struct coap_resource *resource, struct coap_observer *observer)
```

相关声明：[coap_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga4180b2476430fbe4a5e0418fb628ea91)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)。

资源有观察者（Observers），并需要在更新时通知观察者所调用的回调类型。

<a id="r_ga84eda10c4bf3e62241e686fdfa828868"></a>

```c
typedef int(* coap_reply_t) (const struct coap_packet *response, struct coap_reply *reply, const struct net_sockaddr *from)
```

相关声明：[coap_reply_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga84eda10c4bf3e62241e686fdfa828868)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_reply](../network_application_model_reference/P015_coap_reply_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

响应与某个待处理请求（Pending Request）匹配时调用的辅助函数。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 3.4\_枚举（Enumerations）

<a id="r_ga7b8b3041e2f4ae26e663ff7431a6e6e3"></a>

```c
enum coap_option_num { COAP_OPTION_IF_MATCH = 1 , COAP_OPTION_URI_HOST = 3 , COAP_OPTION_ETAG = 4 , COAP_OPTION_IF_NONE_MATCH = 5 , COAP_OPTION_OBSERVE = 6 , COAP_OPTION_URI_PORT = 7 , COAP_OPTION_LOCATION_PATH = 8 , COAP_OPTION_OSCORE = 9 , COAP_OPTION_URI_PATH = 11 , COAP_OPTION_CONTENT_FORMAT = 12 , COAP_OPTION_MAX_AGE = 14 , COAP_OPTION_URI_QUERY = 15 , COAP_OPTION_ACCEPT = 17 , COAP_OPTION_LOCATION_QUERY = 20 , COAP_OPTION_BLOCK2 = 23 , COAP_OPTION_BLOCK1 = 27 , COAP_OPTION_SIZE2 = 28 , COAP_OPTION_PROXY_URI = 35 , COAP_OPTION_PROXY_SCHEME = 39 , COAP_OPTION_SIZE1 = 60 , COAP_OPTION_ECHO = 252 , COAP_OPTION_NO_RESPONSE = 258 , COAP_OPTION_REQUEST_TAG = 292 , COAP_OPTION_SIGNAL_701_MMS = 2 , COAP_OPTION_SIGNAL_701_BWT = 4 , COAP_OPTION_SIGNAL_704_ALT_ADDR = 2 , COAP_OPTION_SIGNAL_704_HOLD_OFF = 4 , COAP_OPTION_SIGNAL_705_BAD_CSM = 2 }
```

相关声明：[coap_option_num](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga7b8b3041e2f4ae26e663ff7431a6e6e3)、[COAP_OPTION_IF_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4c61e26d11841c76debe2f99de5e9756)、[COAP_OPTION_URI_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a402bb0a642a07d951c35d69736fd3f33)、[COAP_OPTION_ETAG](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a0efdc30ce5551daffd093b2a8466978a)、[COAP_OPTION_IF_NONE_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a07ea6f395818a7019bb9e6a6e34d2d74)、[COAP_OPTION_OBSERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a06e91bbb4fa2144543d4148d3245ad25)、[COAP_OPTION_URI_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a344707b9f4cb71310f2ccf5e8050d17a)、[COAP_OPTION_LOCATION_PATH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae82be3591d43f0d1c7e89ab764d969bd)、[COAP_OPTION_OSCORE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3aaa6222533e1a6f1284fc5857884ad24d)、[COAP_OPTION_URI_PATH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a96b5a15937e875b3087307cc5faab1af)、[COAP_OPTION_CONTENT_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac3166e67b5f5bf3cefee58c8ff58e5b8)、[COAP_OPTION_MAX_AGE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ab4cda4d3732fd12b9f203a2475c20981)、[COAP_OPTION_URI_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3adb4d27052247b9a79ad7fcc0cc30c71c)、[COAP_OPTION_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3afd0725f0ceb5ce22a6c7b390ca7efc9d)、[COAP_OPTION_LOCATION_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac728800fc8f0d80e37dcf322e75eb27d)、[COAP_OPTION_BLOCK2](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4aa7cdfa66bd89f21f592eaf3ebe0972)、[COAP_OPTION_BLOCK1](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a8aaa54af114fd1db631566afa69f162d)、[COAP_OPTION_SIZE2](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a26c1bcd7af4fccd949e3de35fc2d88e6)、[COAP_OPTION_PROXY_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae4d2c93b545708926813217cd36a96ac)、[COAP_OPTION_PROXY_SCHEME](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a30da986503e1e15243b74a16b161901c)、[COAP_OPTION_SIZE1](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a53169a1c7b07c9e97f79dfc06af3eb51)、[COAP_OPTION_ECHO](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a620e8b59f67f89de8a38dc76c8fcc594)、[COAP_OPTION_NO_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a7984f2c4845610491bda964111a1c8e7)、[COAP_OPTION_REQUEST_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a2a47428ec35972d256da05104ea6396f)、[COAP_OPTION_SIGNAL_701_MMS](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a2b6f7575ff75fbc51ac5800a693b19af)、[COAP_OPTION_SIGNAL_701_BWT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3aeed15ed39751b1533f4a1f825c73d0a2)、[COAP_OPTION_SIGNAL_704_ALT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a9aa645f3c03f818848d5b728432998e3)、[COAP_OPTION_SIGNAL_704_HOLD_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3af71df6b0647047115c20790eebb3ce30)、[COAP_OPTION_SIGNAL_705_BAD_CSM](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a649cb25887a08fc21eb0cac51f58d3e5)。

已知的 CoAP 分组选项（Packet Options）集合。

<a id="r_ga6a6547e3c755cf7a5033302c8294e0b7"></a>

```c
enum coap_method { COAP_METHOD_GET = 1 , COAP_METHOD_POST = 2 , COAP_METHOD_PUT = 3 , COAP_METHOD_DELETE = 4 , COAP_METHOD_FETCH = 5 , COAP_METHOD_PATCH = 6 , COAP_METHOD_IPATCH = 7 }
```

相关声明：[coap_method](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6a6547e3c755cf7a5033302c8294e0b7)、[COAP_METHOD_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7a025300cb0dc4c4de8eb0b0e0b4eb5317)、[COAP_METHOD_POST](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7aba51bcab79bf75080ccf75c1ec38a3d6)、[COAP_METHOD_PUT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7a91637ef7c9f57cdcc65d0118008251db)、[COAP_METHOD_DELETE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7adccbea1fe9a43433cf8471e32208a5ac)、[COAP_METHOD_FETCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7afa4070fed5c01b28bb1a59e3f0c021f4)、[COAP_METHOD_PATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7adca55e3d2b4b41b249f6b2f67074d708)、[COAP_METHOD_IPATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7a78f97b895f29819bf3f8b0314967f20e)。

可用的请求方法（Request Methods）。

<a id="r_ga3b375b7580246d1266293d09902f3d9f"></a>

```c
enum coap_msgtype { COAP_TYPE_CON = 0 , COAP_TYPE_NON_CON = 1 , COAP_TYPE_ACK = 2 , COAP_TYPE_RESET = 3 }
```

相关声明：[coap_msgtype](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3b375b7580246d1266293d09902f3d9f)、[COAP_TYPE_CON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga3b375b7580246d1266293d09902f3d9fa65c04ee4847d0c595238079ac9564e8d)、[COAP_TYPE_NON_CON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga3b375b7580246d1266293d09902f3d9fa629a304bea0c85c7b2bf746b26216a4f)、[COAP_TYPE_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga3b375b7580246d1266293d09902f3d9fa7b2fe2187018bce9132af2763b57307d)、[COAP_TYPE_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga3b375b7580246d1266293d09902f3d9fa287b951159fd51b84a2e0491b012f84c)。

CoAP 分组可采用的类型（Packet Types）。

<a id="r_ga1ea81a365834e96f43ab7be573069d26"></a>

```c
enum coap_response_code { COAP_RESPONSE_CODE_CREATED = ((2 << 5) | (1)) , COAP_RESPONSE_CODE_DELETED = ((2 << 5) | (2)) , COAP_RESPONSE_CODE_VALID = ((2 << 5) | (3)) , COAP_RESPONSE_CODE_CHANGED = ((2 << 5) | (4)) , COAP_RESPONSE_CODE_CONTENT = ((2 << 5) | (5)) , COAP_RESPONSE_CODE_CONTINUE = ((2 << 5) | (31)) , COAP_RESPONSE_CODE_BAD_REQUEST = ((4 << 5) | (0)) , COAP_RESPONSE_CODE_UNAUTHORIZED = ((4 << 5) | (1)) , COAP_RESPONSE_CODE_BAD_OPTION = ((4 << 5) | (2)) , COAP_RESPONSE_CODE_FORBIDDEN = ((4 << 5) | (3)) , COAP_RESPONSE_CODE_NOT_FOUND = ((4 << 5) | (4)) , COAP_RESPONSE_CODE_NOT_ALLOWED = ((4 << 5) | (5)) , COAP_RESPONSE_CODE_NOT_ACCEPTABLE = ((4 << 5) | (6)) , COAP_RESPONSE_CODE_INCOMPLETE = ((4 << 5) | (8)) , COAP_RESPONSE_CODE_CONFLICT = ((4 << 5) | (9)) , COAP_RESPONSE_CODE_PRECONDITION_FAILED = ((4 << 5) | (12)) , COAP_RESPONSE_CODE_REQUEST_TOO_LARGE = ((4 << 5) | (13)) , COAP_RESPONSE_CODE_UNSUPPORTED_CONTENT_FORMAT , COAP_RESPONSE_CODE_UNPROCESSABLE_ENTITY = ((4 << 5) | (22)) , COAP_RESPONSE_CODE_TOO_MANY_REQUESTS = ((4 << 5) | (29)) , COAP_RESPONSE_CODE_INTERNAL_ERROR = ((5 << 5) | (0)) , COAP_RESPONSE_CODE_NOT_IMPLEMENTED = ((5 << 5) | (1)) , COAP_RESPONSE_CODE_BAD_GATEWAY = ((5 << 5) | (2)) , COAP_RESPONSE_CODE_SERVICE_UNAVAILABLE = ((5 << 5) | (3)) , COAP_RESPONSE_CODE_GATEWAY_TIMEOUT = ((5 << 5) | (4)) , COAP_RESPONSE_CODE_PROXYING_NOT_SUPPORTED , COAP_SIGNAL_CODE_CSM = ((7 << 5) | (1)) , COAP_SIGNAL_CODE_PING = ((7 << 5) | (2)) , COAP_SIGNAL_CODE_PONG = ((7 << 5) | (3)) , COAP_SIGNAL_CODE_RELEASE = ((7 << 5) | (4)) , COAP_SIGNAL_CODE_ABORT = ((7 << 5) | (5)) }
```

相关声明：[coap_response_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1ea81a365834e96f43ab7be573069d26)、[COAP_RESPONSE_CODE_CREATED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26ad2d9fe8dd5beda74b522377c0b76275b)、[COAP_RESPONSE_CODE_DELETED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26abf324915aa498c64a733a0098de4a082)、[COAP_RESPONSE_CODE_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26aecaac4a0e9c821dfc20536951409dd48)、[COAP_RESPONSE_CODE_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3)、[COAP_RESPONSE_CODE_CONTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26adfd3e5e3c6ad5715127bb444c205fbce)、[COAP_RESPONSE_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26ae4e3ff451c626421b9b329790f019dd8)、[COAP_RESPONSE_CODE_BAD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5)、[COAP_RESPONSE_CODE_UNAUTHORIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26acb76dbf11b47477144cc4ece3357283c)、[COAP_RESPONSE_CODE_BAD_OPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a989a6528edc653c0b693ed875481e82d)、[COAP_RESPONSE_CODE_FORBIDDEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26afeee555ef54f138db58b14ad2c328d04)、[COAP_RESPONSE_CODE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a86c2bff8add69428d164431b3091a8e9)、[COAP_RESPONSE_CODE_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a301eb722445472dba93d5accd6e0dd31)、[COAP_RESPONSE_CODE_NOT_ACCEPTABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a4d77322514521e8dfea01f4a1a6e5886)、[COAP_RESPONSE_CODE_INCOMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a671730c6d2f1a339fcd557c5452150af)、[COAP_RESPONSE_CODE_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26ab447505d233aed9fd8ad28070d317544)、[COAP_RESPONSE_CODE_PRECONDITION_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a289ade02833b57bffd915e648e050e52)、[COAP_RESPONSE_CODE_REQUEST_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26aaa43062a8146c1e2e09183228a540d2e)、[COAP_RESPONSE_CODE_UNSUPPORTED_CONTENT_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26aef6b165b9d3f8f4b477431058815c16b)、[COAP_RESPONSE_CODE_UNPROCESSABLE_ENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a5e5e31cc4647d5e0fdd1c8fe6cfa2661)、[COAP_RESPONSE_CODE_TOO_MANY_REQUESTS](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26aabd72cff6669d382aa04c53e764d0b49)、[COAP_RESPONSE_CODE_INTERNAL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499)、[COAP_RESPONSE_CODE_NOT_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a85c04541bc8580c2ae915946fd677c15)、[COAP_RESPONSE_CODE_BAD_GATEWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a8de29a7ee6bb960a97d6b415217b4640)、[COAP_RESPONSE_CODE_SERVICE_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26afebd274586351951ffe9c8f26b270dec)、[COAP_RESPONSE_CODE_GATEWAY_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26af6d379fef704c269406b782c60772ecd)、[COAP_RESPONSE_CODE_PROXYING_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a5f49a566d37b2cda0c624d76aee08bd1)、[COAP_SIGNAL_CODE_CSM](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26ac528f38c3e8553d83e0455097f4fbdf9)、[COAP_SIGNAL_CODE_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a7390f381b1aa8a4aa21d98527950a152)、[COAP_SIGNAL_CODE_PONG](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26abc76b74967e491c10f320bf19c9026d4)、[COAP_SIGNAL_CODE_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a026916ae7964a98edeadd3f09e9d18ad)、[COAP_SIGNAL_CODE_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a95a8d4bee68a3829dfb4f3a024c8bf68)。

响应分组可用的响应码（Response Codes）集合。

<a id="r_ga94a8f9956742d3928fc3c63b8d01ae73"></a>

```c
enum coap_content_format { COAP_CONTENT_FORMAT_TEXT_PLAIN = 0 , COAP_CONTENT_FORMAT_APP_LINK_FORMAT = 40 , COAP_CONTENT_FORMAT_APP_XML = 41 , COAP_CONTENT_FORMAT_APP_OCTET_STREAM = 42 , COAP_CONTENT_FORMAT_APP_EXI = 47 , COAP_CONTENT_FORMAT_APP_JSON = 50 , COAP_CONTENT_FORMAT_APP_JSON_PATCH_JSON = 51 , COAP_CONTENT_FORMAT_APP_MERGE_PATCH_JSON = 52 , COAP_CONTENT_FORMAT_APP_CBOR = 60 }
```

相关声明：[coap_content_format](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga94a8f9956742d3928fc3c63b8d01ae73)、[COAP_CONTENT_FORMAT_TEXT_PLAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73af068aa8d09032352799bc60868607997)、[COAP_CONTENT_FORMAT_APP_LINK_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a1fbd90fd5cb309e2de6954f46174dc4f)、[COAP_CONTENT_FORMAT_APP_XML](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73adb96bf55e914f4852e92dc65752c372a)、[COAP_CONTENT_FORMAT_APP_OCTET_STREAM](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a88d952174bb3e4ffb9ab11a599952760)、[COAP_CONTENT_FORMAT_APP_EXI](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a483a382550b38468cc66bdce9f4743ea)、[COAP_CONTENT_FORMAT_APP_JSON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a975381d286c1e9b998e41ef0a234d17a)、[COAP_CONTENT_FORMAT_APP_JSON_PATCH_JSON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a141f183724ad6da14c3992c0990d6239)、[COAP_CONTENT_FORMAT_APP_MERGE_PATCH_JSON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a2797149fb3811d706dab291e9edc9436)、[COAP_CONTENT_FORMAT_APP_CBOR](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a7ca73ff57a6c7fb1517b44f2ce17d3f9)。

CoAP 内容格式选项（Content-Format Option）的取值集合。

<a id="r_ga2a323287262bbb6a4932e7911ddb652c"></a>

```c
enum coap_no_response { COAP_NO_RESPONSE_SUPPRESS_2_XX = 0x02 , COAP_NO_RESPONSE_SUPPRESS_4_XX = 0x08 , COAP_NO_RESPONSE_SUPPRESS_5_XX = 0x10 , COAP_NO_RESPONSE_SUPPRESS_ALL }
```

相关声明：[coap_no_response](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2a323287262bbb6a4932e7911ddb652c)、[COAP_NO_RESPONSE_SUPPRESS_2_XX](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga2a323287262bbb6a4932e7911ddb652caeeb51bb18780c20df5b25183d52d42de)、[COAP_NO_RESPONSE_SUPPRESS_4_XX](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga2a323287262bbb6a4932e7911ddb652cae8b0b1231d095b3e7a972ca4c86d8dce)、[COAP_NO_RESPONSE_SUPPRESS_5_XX](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga2a323287262bbb6a4932e7911ddb652ca19ebfb46899b440124322bb67c906cb3)、[COAP_NO_RESPONSE_SUPPRESS_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga2a323287262bbb6a4932e7911ddb652ca21758021d7f3a36bf6ede06daa82dbf0)。

CoAP 无响应选项（No-Response Option）的取值集合。

<a id="r_ga712c1468f936a3af7dc39a86a5961922"></a>

```c
enum coap_block_size { COAP_BLOCK_16 , COAP_BLOCK_32 , COAP_BLOCK_64 , COAP_BLOCK_128 , COAP_BLOCK_256 , COAP_BLOCK_512 , COAP_BLOCK_1024 , COAP_BLOCK_BERT }
```

相关声明：[coap_block_size](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga712c1468f936a3af7dc39a86a5961922)、[COAP_BLOCK_16](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a834d479806b513818e2237f3f1c56968)、[COAP_BLOCK_32](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a1aaf8f841c18e281b176793bb331993d)、[COAP_BLOCK_64](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a7266f448a391ea2a2763f1ded5397520)、[COAP_BLOCK_128](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a147ddf4b0e5d1a8c11f0da2c71dee4d8)、[COAP_BLOCK_256](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922acfc37f84eabccdde4bd84b06c6a5e753)、[COAP_BLOCK_512](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922ad2052905aff08c58585dcf6c6caddc19)、[COAP_BLOCK_1024](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a6998c79e63cf65e7f86ddd5713d48dce)、[COAP_BLOCK_BERT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a549135603208a878cdefd6c5ca1a039b)。

表示分块传输（Block-Wise Transfers，RFC 7959）中每个传输块的大小：

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.5\_函数（Functions）

<a id="r_gafd01c39fac8f173edc04337161e92264"></a>

```c
uint8_t coap_header_get_version (const struct coap_packet *cpkt)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[coap_header_get_version](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafd01c39fac8f173edc04337161e92264)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

返回 CoAP 分组中的版本（Version）。

<a id="r_gaed883ea6cec3acc5eb570e152dc52e25"></a>

```c
uint8_t coap_header_get_type (const struct coap_packet *cpkt)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[coap_header_get_type](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaed883ea6cec3acc5eb570e152dc52e25)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

返回 CoAP 分组的类型（Type）。

<a id="r_ga6a5049accfa0cd7106a3a6593c598545"></a>

```c
uint8_t coap_header_get_token (const struct coap_packet *cpkt, uint8_t *token)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[coap_header_get_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6a5049accfa0cd7106a3a6593c598545)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

返回 CoAP 分组中的令牌（Token），若存在。

<a id="r_gae4bf952fdf9e3d03ab0b0df4c3c0d054"></a>

```c
uint8_t coap_header_get_code (const struct coap_packet *cpkt)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[coap_header_get_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gae4bf952fdf9e3d03ab0b0df4c3c0d054)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

返回 CoAP 分组的代码（Code）。

<a id="r_gafdaecca5ad26bab4fb7c9ee3477318f8"></a>

```c
int coap_header_set_code (const struct coap_packet *cpkt, uint8_t code)
```

相关声明：[coap_header_set_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafdaecca5ad26bab4fb7c9ee3477318f8)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

修改 CoAP 分组的代码（Code）。

<a id="r_ga63388c629da5370d2e711cdc9aabd837"></a>

```c
uint16_t coap_header_get_id (const struct coap_packet *cpkt)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[coap_header_get_id](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga63388c629da5370d2e711cdc9aabd837)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

返回 CoAP 分组关联的消息 ID（Message ID）。

<a id="r_ga28ccf00fb1f5f13f747e61c2e3008b5c"></a>

```c
const uint8_t * coap_packet_get_payload (const struct coap_packet *cpkt, uint16_t *len)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[coap_packet_get_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga28ccf00fb1f5f13f747e61c2e3008b5c)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

返回 CoAP 分组的数据指针和长度。

<a id="r_ga8b621232b740d8e8e1771fba24897121"></a>

```c
bool coap_uri_path_match (const char *const *path, struct coap_option *options, uint8_t opt_num)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_uri_path_match](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga8b621232b740d8e8e1771fba24897121)、[coap_option](../network_application_model_reference/P010_coap_option_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

验证 CoAP URI 路径（URI Path）是否与提供的选项匹配。

<a id="r_ga27a58a69f632551aa7a2394ae2badacf"></a>

```c
int coap_packet_parse (struct coap_packet *cpkt, uint8_t *data, uint16_t len, struct coap_option *options, uint8_t opt_num)
```

相关声明：[coap_packet_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga27a58a69f632551aa7a2394ae2badacf)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[coap_option](../network_application_model_reference/P010_coap_option_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

解析 `data` 中的 CoAP 分组，进行验证并初始化 `cpkt`。

<a id="r_gab8f9e9cdfa20920d5d25fb1507a2286d"></a>

```c
int coap_packet_set_path (struct coap_packet *cpkt, const char *path)
```

相关声明：[coap_packet_set_path](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gab8f9e9cdfa20920d5d25fb1507a2286d)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

解析提供的 CoAP 路径（可带或不带查询）或查询（Query），并将其作为选项追加到 `cpkt`。

<a id="r_ga90e6aab174f8977f0a3b5fbe1a20297c"></a>

```c
int coap_packet_init (struct coap_packet *cpkt, uint8_t *data, uint16_t max_len, uint8_t ver, uint8_t type, uint8_t token_len, const uint8_t *token, uint8_t code, uint16_t id)
```

相关声明：[coap_packet_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga90e6aab174f8977f0a3b5fbe1a20297c)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

根据输入数据创建新的 CoAP 分组（Packet）。

<a id="r_gae6d93b1f93734302be75ee417813e5d1"></a>

```c
int coap_ack_init (struct coap_packet *cpkt, const struct coap_packet *req, uint8_t *data, uint16_t max_len, uint8_t code)
```

相关声明：[coap_ack_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gae6d93b1f93734302be75ee417813e5d1)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

为给定请求创建新的 CoAP 确认消息（Acknowledgment Message）。

<a id="r_ga9626781d73d18c1305f654ef4723e5db"></a>

```c
int coap_rst_init (struct coap_packet *cpkt, const struct coap_packet *req, uint8_t *data, uint16_t max_len)
```

相关声明：[coap_rst_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga9626781d73d18c1305f654ef4723e5db)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

为给定请求创建新的 CoAP 复位消息（Reset Message）。

<a id="r_ga66f986f8a1157236bea27133c2a2538b"></a>

```c
uint8_t * coap_next_token (void)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[coap_next_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga66f986f8a1157236bea27133c2a2538b)。

返回随机生成的 8 字节数组，可用作消息令牌（Token）。

<a id="r_gade5f4995c6419db03ce3e7ff7ca1cfcb"></a>

```c
uint16_t coap_next_id (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[coap_next_id](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gade5f4995c6419db03ce3e7ff7ca1cfcb)。

用于生成消息 ID（Message IDs）的辅助函数。

<a id="r_gaf006c8048ed7b863e70dbdd64bc3d608"></a>

```c
int coap_find_options (const struct coap_packet *cpkt, uint16_t code, struct coap_option *options, uint16_t veclen)
```

相关声明：[coap_find_options](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaf006c8048ed7b863e70dbdd64bc3d608)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[coap_option](../network_application_model_reference/P010_coap_option_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

返回选项编号为 `code` 的选项所关联的值。

<a id="r_ga2aa4140ee83ca4090a5604e34d1f1446"></a>

```c
int coap_packet_append_option (struct coap_packet *cpkt, uint16_t code, const uint8_t *value, uint16_t len)
```

相关声明：[coap_packet_append_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2aa4140ee83ca4090a5604e34d1f1446)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向分组追加选项（Option）。

<a id="r_gaca300a216781d360d2cd64e8e9f1ae8f"></a>

```c
int coap_packet_remove_option (struct coap_packet *cpkt, uint16_t code)
```

相关声明：[coap_packet_remove_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaca300a216781d360d2cd64e8e9f1ae8f)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

从分组移除选项（Option）。

<a id="r_ga2fd0613e61274ec4b9b7bab3ab11ccce"></a>

```c
unsigned int coap_option_value_to_int (const struct coap_option *option)
```

相关声明：[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)、[coap_option_value_to_int](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2fd0613e61274ec4b9b7bab3ab11ccce)、[coap_option](../network_application_model_reference/P010_coap_option_结构体.md)。

将选项转换为整数表示（Integer Representation）。

<a id="r_ga6bec94992ac450dca03436a6ad74efb4"></a>

```c
int coap_append_option_int (struct coap_packet *cpkt, uint16_t code, unsigned int val)
```

相关声明：[coap_append_option_int](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6bec94992ac450dca03436a6ad74efb4)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)。

向分组追加整数值选项（Integer Value Option）。

<a id="r_ga24000def8534acdcd2c61836dc690367"></a>

```c
int coap_packet_append_payload_marker (struct coap_packet *cpkt)
```

相关声明：[coap_packet_append_payload_marker](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga24000def8534acdcd2c61836dc690367)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

向 CoAP 分组追加载荷标记（Payload Marker）。

<a id="r_gadcd3a93a702a2a0b428f39b71dd67954"></a>

```c
int coap_packet_append_payload (struct coap_packet *cpkt, const uint8_t *payload, uint16_t payload_len)
```

相关声明：[coap_packet_append_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gadcd3a93a702a2a0b428f39b71dd67954)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

向 CoAP 分组追加载荷（Payload）。

<a id="r_ga323644931c927b8988aafd89dacb993c"></a>

```c
bool coap_packet_is_request (const struct coap_packet *cpkt)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_packet_is_request](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga323644931c927b8988aafd89dacb993c)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

检查 CoAP 分组是否为 CoAP 请求（Request）。

<a id="r_gab8ab58c900a4b0396ca7722c754fb1ec"></a>

```c
int coap_handle_request_len (struct coap_packet *cpkt, struct coap_resource *resources, size_t resources_len, struct coap_option *options, uint8_t opt_num, struct net_sockaddr *addr, net_socklen_t addr_len)
```

相关声明：[coap_handle_request_len](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gab8ab58c900a4b0396ca7722c754fb1ec)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[coap_option](../network_application_model_reference/P010_coap_option_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

收到请求后，调用匹配资源（Resources）的相应方法。

<a id="r_gaa170f8dbe1633e2b02c9c2d8dd27f181"></a>

```c
int coap_handle_request (struct coap_packet *cpkt, struct coap_resource *resources, struct coap_option *options, uint8_t opt_num, struct net_sockaddr *addr, net_socklen_t addr_len)
```

相关声明：[coap_handle_request](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaa170f8dbe1633e2b02c9c2d8dd27f181)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[coap_option](../network_application_model_reference/P010_coap_option_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)。

收到请求后，调用匹配资源（Resources）的相应方法。

<a id="r_gafffadd4a837e48fd72af20468ccd86f2"></a>

```c
static uint16_t coap_block_size_to_bytes (enum coap_block_size block_size)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[coap_block_size_to_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafffadd4a837e48fd72af20468ccd86f2)、[coap_block_size](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga712c1468f936a3af7dc39a86a5961922)。

用于将枚举转换为以字节表示的大小的辅助函数。

<a id="r_ga27e3008b8511333e0c0115ba928017f3"></a>

```c
static enum coap_block_size coap_bytes_to_block_size (uint16_t bytes)
```

相关声明：[coap_block_size](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga712c1468f936a3af7dc39a86a5961922)、[coap_bytes_to_block_size](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga27e3008b8511333e0c0115ba928017f3)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

用于将以字节表示的块大小（Block Size）转换为枚举的辅助函数。

<a id="r_ga57486e764f0feb6544fa3b0d19935afd"></a>

```c
int coap_block_transfer_init (struct coap_block_context *ctx, enum coap_block_size block_size, size_t total_size)
```

相关声明：[coap_block_transfer_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga57486e764f0feb6544fa3b0d19935afd)、[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)、[coap_block_size](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga712c1468f936a3af7dc39a86a5961922)。

初始化分块传输（Block-Wise Transfer）的上下文（Context）。

<a id="r_ga8b5966a29054ace04cae81d4da588e72"></a>

```c
int coap_append_descriptive_block_option (struct coap_packet *cpkt, struct coap_block_context *ctx)
```

相关声明：[coap_append_descriptive_block_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga8b5966a29054ace04cae81d4da588e72)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)。

向分组追加 BLOCK1 或 BLOCK2 选项（Option）。

<a id="r_gaabdfa8cf28cc2c3a14ae0af5fa7e7212"></a>

```c
bool coap_has_descriptive_block_option (struct coap_packet *cpkt)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_has_descriptive_block_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaabdfa8cf28cc2c3a14ae0af5fa7e7212)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

检查分组是否设置了描述性块选项（Descriptive Block Option）。

<a id="r_ga941ee9d68f1a628755aa79c249cbae58"></a>

```c
int coap_remove_descriptive_block_option (struct coap_packet *cpkt)
```

相关声明：[coap_remove_descriptive_block_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga941ee9d68f1a628755aa79c249cbae58)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

从分组移除 BLOCK1 或 BLOCK2 选项（Option）。

<a id="r_gafc61a6878d82f81565ab752ced0ce2be"></a>

```c
bool coap_block_has_more (struct coap_packet *cpkt)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_block_has_more](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafc61a6878d82f81565ab752ced0ce2be)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

检查 BLOCK1 或 BLOCK2 选项是否设置了“还有后续块”标志（More Flag）。

<a id="r_ga518d5f4422ff45f2b4a296f249da89cd"></a>

```c
int coap_append_block1_option (struct coap_packet *cpkt, struct coap_block_context *ctx)
```

相关声明：[coap_append_block1_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga518d5f4422ff45f2b4a296f249da89cd)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)。

向分组追加 BLOCK1 选项。

<a id="r_ga361c17b698bdaa0fc529b7338efefd8c"></a>

```c
int coap_append_block2_option (struct coap_packet *cpkt, struct coap_block_context *ctx)
```

相关声明：[coap_append_block2_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga361c17b698bdaa0fc529b7338efefd8c)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)。

向分组追加 BLOCK2 选项。

<a id="r_ga3f66d5935dcacfeebcac2b3001d7b57a"></a>

```c
int coap_append_size1_option (struct coap_packet *cpkt, struct coap_block_context *ctx)
```

相关声明：[coap_append_size1_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3f66d5935dcacfeebcac2b3001d7b57a)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)。

向分组追加 SIZE1 选项。

<a id="r_gafbc8c15ef03b762f9411c38b03aa403b"></a>

```c
int coap_append_size2_option (struct coap_packet *cpkt, struct coap_block_context *ctx)
```

相关声明：[coap_append_size2_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafbc8c15ef03b762f9411c38b03aa403b)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)。

向分组追加 SIZE2 选项。

<a id="r_ga21b8f4ffeecc7900f6bf299836d2b5b3"></a>

```c
int coap_get_option_int (const struct coap_packet *cpkt, uint16_t code)
```

相关声明：[coap_get_option_int](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga21b8f4ffeecc7900f6bf299836d2b5b3)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

获取 CoAP 选项的整数表示（Integer Representation）。

<a id="r_ga10c4a0d7e2052f3116fbf3b355fe75db"></a>

```c
int coap_get_block1_option (const struct coap_packet *cpkt, bool *has_more, uint32_t *block_number)
```

相关声明：[coap_get_block1_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga10c4a0d7e2052f3116fbf3b355fe75db)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 CoAP BLOCK1 选项获取块大小（Block Size）、后续块标志（More Flag）和块编号（Block Number）。

<a id="r_ga196390e6f016b72b3ae2ae9e69bed1b7"></a>

```c
int coap_get_block2_option (const struct coap_packet *cpkt, bool *has_more, uint32_t *block_number)
```

相关声明：[coap_get_block2_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga196390e6f016b72b3ae2ae9e69bed1b7)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

从 CoAP BLOCK2 选项获取各值。

<a id="r_ga3b0cc9bfabdddeffd98f36d7f15dd416"></a>

```c
int coap_update_from_block (const struct coap_packet *cpkt, struct coap_block_context *ctx)
```

相关声明：[coap_update_from_block](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3b0cc9bfabdddeffd98f36d7f15dd416)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)。

从 `cpkt` 获取 `BLOCK{1,2}` 和 `SIZE{1,2}`，并相应更新 `ctx`。

<a id="r_ga50f7837da003601479dbc470ba9898ae"></a>

```c
int coap_next_block_for_option (const struct coap_packet *cpkt, struct coap_block_context *ctx, enum coap_option_num option)
```

相关声明：[coap_next_block_for_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga50f7837da003601479dbc470ba9898ae)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)、[coap_option_num](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga7b8b3041e2f4ae26e663ff7431a6e6e3)。

根据 `cpkt` 中设置的选项更新 `ctx`，使调用后当前条目指示正在传输的数据体中的正确偏移（Offset）。

<a id="r_ga1244716ecf06fad1013131c42eab8c5c"></a>

```c
size_t coap_next_block (const struct coap_packet *cpkt, struct coap_block_context *ctx)
```

相关声明：[coap_next_block](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1244716ecf06fad1013131c42eab8c5c)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)。

更新 `ctx`，使调用后当前条目指示正在传输的数据体中的正确偏移（Offset）。

<a id="r_ga998a3b01a3a535614183ac08da101811"></a>

```c
bool coap_age_is_newer (uint32_t v1, uint32_t v2)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_age_is_newer](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga998a3b01a3a535614183ac08da101811)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

比较观察选项（Observe Option）的值，以判断新鲜度（Freshness）。

<a id="r_ga262f21fdad778db96c8bd700ba66ce1b"></a>

```c
void coap_observer_init (struct coap_observer *observer, const struct coap_packet *request, const struct net_sockaddr *addr)
```

相关声明：[coap_observer_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga262f21fdad778db96c8bd700ba66ce1b)、[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

表示由 `addr` 引用并发出 `request` 的远端设备希望观察（Observe）某个资源。

<a id="r_ga34c5eac86081ea46b63c1cbb7c1315e9"></a>

```c
void coap_observer_init_oscore (struct coap_observer *observer, const struct coap_packet *request, const struct net_sockaddr *addr, struct coap_oscore_context *oscore_ctx)
```

相关声明：[coap_observer_init_oscore](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga34c5eac86081ea46b63c1cbb7c1315e9)、[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

表示由 `addr` 引用并发出 `request` 的远端设备希望观察（Observe）某个资源。

<a id="r_ga3c42861f8442e548f560acf3deca6baa"></a>

```c
bool coap_register_observer (struct coap_resource *resource, struct coap_observer *observer)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_register_observer](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3c42861f8442e548f560acf3deca6baa)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)。

观察者（Observer）初始化后，将其关联到资源（Resource）。

<a id="r_ga33c351ac06b5ae9217cd53d8cf330fbd"></a>

```c
bool coap_remove_observer (struct coap_resource *resource, struct coap_observer *observer)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_remove_observer](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga33c351ac06b5ae9217cd53d8cf330fbd)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)。

从该资源已注册的观察者列表（Observer List）中移除此观察者。

<a id="r_gab045e6e61ef8c35f85591b8792d88952"></a>

```c
struct coap_observer * coap_find_observer (struct coap_observer *observers, size_t len, const struct net_sockaddr *addr, const uint8_t *token, uint8_t token_len)
```

相关声明：[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)、[coap_find_observer](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gab045e6e61ef8c35f85591b8792d88952)、[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

返回地址与 `addr` 匹配、且令牌为 `token` 的观察者（Observer）。

<a id="r_ga6542f6350f6e4ed861d6c482617dd5d0"></a>

```c
struct coap_observer * coap_find_observer_by_addr (struct coap_observer *observers, size_t len, const struct net_sockaddr *addr)
```

相关声明：[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)、[coap_find_observer_by_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6542f6350f6e4ed861d6c482617dd5d0)、[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

返回地址与 `addr` 匹配的观察者（Observer）。

<a id="r_gadeaa59fd7b6eab454d5930289b4e08f7"></a>

```c
struct coap_observer * coap_find_observer_by_token (struct coap_observer *observers, size_t len, const uint8_t *token, uint8_t token_len)
```

相关声明：[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)、[coap_find_observer_by_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gadeaa59fd7b6eab454d5930289b4e08f7)、[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

返回令牌为 `token` 的观察者（Observer）。

<a id="r_ga2410e973bf3192244426df346230608b"></a>

```c
struct coap_observer * coap_observer_next_unused (struct coap_observer *observers, size_t len)
```

相关声明：[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)、[coap_observer_next_unused](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2410e973bf3192244426df346230608b)、[coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)。

返回下一个可用的观察者表示（Observer Representation）。

<a id="r_gacfe30c84434dc8adbf3d399ec0e51bec"></a>

```c
void coap_reply_init (struct coap_reply *reply, const struct coap_packet *request)
```

相关声明：[coap_reply_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gacfe30c84434dc8adbf3d399ec0e51bec)、[coap_reply](../network_application_model_reference/P015_coap_reply_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

表示期望收到对 `request` 的回复（Reply）。

<a id="r_ga0b84eee85b854bf087bceb7566e93086"></a>

```c
int coap_pending_init (struct coap_pending *pending, const struct coap_packet *request, const struct net_sockaddr *addr, const struct coap_transmission_parameters *params)
```

相关声明：[coap_pending_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga0b84eee85b854bf087bceb7566e93086)、[coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)。

用一个请求初始化待处理请求（Pending Request）。

<a id="r_ga800831ddfe19b1a5637a5edd9e78c470"></a>

```c
struct coap_pending * coap_pending_next_unused (struct coap_pending *pendings, size_t len)
```

相关声明：[coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)、[coap_pending_next_unused](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga800831ddfe19b1a5637a5edd9e78c470)、[coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)。

返回下一个可用的待处理结构体（Pending Struct），可用于跟踪请求的重传状态（Retransmission Status）。

<a id="r_ga65cb5f7ac01ea5ebe1c6e30a7c70ad4e"></a>

```c
struct coap_reply * coap_reply_next_unused (struct coap_reply *replies, size_t len)
```

相关声明：[coap_reply](../network_application_model_reference/P015_coap_reply_结构体.md)、[coap_reply_next_unused](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga65cb5f7ac01ea5ebe1c6e30a7c70ad4e)、[coap_reply](../network_application_model_reference/P015_coap_reply_结构体.md)。

返回下一个可用的回复结构体（Reply Struct），可用于跟踪收到的回复和通知。

<a id="r_ga94ceba78cbd2440f91d9b30d6b06594d"></a>

```c
struct coap_pending * coap_pending_received (const struct coap_packet *response, struct coap_pending *pendings, size_t len)
```

相关声明：[coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)、[coap_pending_received](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga94ceba78cbd2440f91d9b30d6b06594d)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)。

收到响应后，返回是否存在匹配的待处理请求（Pending Request）。

<a id="r_ga44ca9e8b0fe2544b8da73efda10b187b"></a>

```c
struct coap_reply * coap_response_received (const struct coap_packet *response, const struct net_sockaddr *from, struct coap_reply *replies, size_t len)
```

相关声明：[coap_reply](../network_application_model_reference/P015_coap_reply_结构体.md)、[coap_response_received](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga44ca9e8b0fe2544b8da73efda10b187b)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[coap_reply](../network_application_model_reference/P015_coap_reply_结构体.md)。

收到响应后，调用 `coap_reply` 结构体中注册的 `coap_reply_t` 处理函数。

<a id="r_ga9d63518c701ebdb4c7f65c5368d00d27"></a>

```c
struct coap_pending * coap_pending_next_to_expire (struct coap_pending *pendings, size_t len)
```

相关声明：[coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)、[coap_pending_next_to_expire](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga9d63518c701ebdb4c7f65c5368d00d27)、[coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)。

返回下一个即将到期的待处理项（Pending）；`pending->timeout` 给出距下一次到期还有多少毫秒。

<a id="r_ga2bcfc7340ed2347862b0f003e1b00a4b"></a>

```c
bool coap_pending_cycle (struct coap_pending *pending)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_pending_cycle](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2bcfc7340ed2347862b0f003e1b00a4b)、[coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)。

请求发送后，用户可能需要推进待处理重传（Pending Retransmission）的周期，以更新超时。

<a id="r_ga03287eb3187aa28e0e83e0e0c72e2631"></a>

```c
void coap_pending_clear (struct coap_pending *pending)
```

相关声明：[coap_pending_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03287eb3187aa28e0e83e0e0c72e2631)、[coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)。

取消待处理重传（Pending Retransmission），使该项重新可用。

<a id="r_ga6e0947048052e733a3571fdc8955b2d7"></a>

```c
void coap_pendings_clear (struct coap_pending *pendings, size_t len)
```

相关声明：[coap_pendings_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6e0947048052e733a3571fdc8955b2d7)、[coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)。

取消所有待处理重传（Pending Retransmissions），使这些项重新可用。

<a id="r_gad9db2ced9b882265c16e3039f893ca03"></a>

```c
size_t coap_pendings_count (struct coap_pending *pendings, size_t len)
```

相关声明：[coap_pendings_count](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gad9db2ced9b882265c16e3039f893ca03)、[coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)。

统计待处理请求（Pending Requests）的数量。

<a id="r_ga37b58c38c150751d31207ece416529d8"></a>

```c
void coap_reply_clear (struct coap_reply *reply)
```

相关声明：[coap_reply_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga37b58c38c150751d31207ece416529d8)、[coap_reply](../network_application_model_reference/P015_coap_reply_结构体.md)。

取消等待此回复（Reply），使该项重新可用。

<a id="r_gaddb02509934f5bac20b7c7f83aea4cd8"></a>

```c
void coap_replies_clear (struct coap_reply *replies, size_t len)
```

相关声明：[coap_replies_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaddb02509934f5bac20b7c7f83aea4cd8)、[coap_reply](../network_application_model_reference/P015_coap_reply_结构体.md)。

取消所有回复（Replies），使这些项重新可用。

<a id="r_gad0c738d308f9cca8ea5cdb79449282cb"></a>

```c
int coap_resource_notify (struct coap_resource *resource)
```

相关声明：[coap_resource_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gad0c738d308f9cca8ea5cdb79449282cb)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)。

表示此资源（Resource）已更新，应为每个已注册观察者（Observer）调用通知回调（Notify Callback）。

<a id="r_ga46b315c30b642eec65bcb84e9c937ee7"></a>

```c
bool coap_request_is_observe (const struct coap_packet *request)
```

相关声明：[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[coap_request_is_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga46b315c30b642eec65bcb84e9c937ee7)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

返回此请求是否在启用资源观察（Observing a Resource）。

<a id="r_ga1bd7be0a5390f0599e7bec0cbd79daf8"></a>

```c
struct coap_transmission_parameters coap_get_transmission_parameters (void)
```

相关声明：[coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)、[coap_get_transmission_parameters](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1bd7be0a5390f0599e7bec0cbd79daf8)。

获取当前生效的 CoAP 传输参数（Transmission Parameters）。

<a id="r_gaf361fd233f1aa650650108ae1e205ede"></a>

```c
void coap_set_transmission_parameters (const struct coap_transmission_parameters *params)
```

相关声明：[coap_set_transmission_parameters](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaf361fd233f1aa650650108ae1e205ede)、[coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)。

设置 CoAP 传输参数（Transmission Parameters）。

<a id="r_ga59f6d6ff09861ab3df9cda894f45de40"></a>

```c
int coap_check_unsupported_critical_options (const struct coap_packet *cpkt, uint16_t *opt)
```

相关声明：[coap_check_unsupported_critical_options](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga59f6d6ff09861ab3df9cda894f45de40)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

检查 CoAP 分组是否包含不受支持的关键选项（Critical Options）。

<a id="r_gaa715f58474d6f668f47dc66e478ba6b2"></a>

```c
uint8_t coap_tcp_header_get_token (const struct coap_packet *cpkt, uint8_t *token)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[coap_tcp_header_get_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaa715f58474d6f668f47dc66e478ba6b2)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

返回 CoAP TCP 分组中的令牌（Token），若存在。

<a id="r_gab2dc876158b3248fa35fbc61a1faf19a"></a>

```c
uint8_t coap_tcp_header_get_code (const struct coap_packet *cpkt)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[coap_tcp_header_get_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gab2dc876158b3248fa35fbc61a1faf19a)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

返回 CoAP TCP 分组的代码（Code）。

<a id="r_ga1adc19283d0b41f6af152d41b32b86d7"></a>

```c
const uint8_t * coap_tcp_packet_get_payload (const struct coap_packet *cpkt, uint32_t *len)
```

相关声明：[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[coap_tcp_packet_get_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1adc19283d0b41f6af152d41b32b86d7)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)。

返回 CoAP TCP 分组的数据指针和长度。

<a id="r_gaf2cd52a5976556c2093bc770bb61c192"></a>

```c
int coap_tcp_packet_parse (struct coap_packet *cpkt, uint8_t *data, uint16_t len, struct coap_option *options, uint8_t opt_num)
```

相关声明：[coap_tcp_packet_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaf2cd52a5976556c2093bc770bb61c192)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[coap_option](../network_application_model_reference/P010_coap_option_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

解析 `data` 中的 CoAP TCP 分组，进行验证并初始化 `cpkt`。

<a id="r_ga5d9fd91c714705b56780264823c56fe6"></a>

```c
int coap_tcp_packet_init (struct coap_packet *cpkt, uint8_t *data, uint16_t max_len, uint8_t token_len, const uint8_t *token, uint8_t code)
```

相关声明：[coap_tcp_packet_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga5d9fd91c714705b56780264823c56fe6)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

根据输入数据创建新的 CoAP TCP 分组（Packet）。

<a id="r_gae5829b14002cc4d24cf8501ab960c35a"></a>

```c
int coap_tcp_packet_update_len (struct coap_packet *cpkt)
```

相关声明：[coap_tcp_packet_update_len](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gae5829b14002cc4d24cf8501ab960c35a)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)。

更新 CoAP TCP 分组头部中的长度字段（Length Field）。

<a id="r_gaf3275841a174b4438c20a1e6e364ea8a"></a>

```c
int coap_tcp_append_block2_option (struct coap_packet *cpkt, struct coap_block_context *ctx)
```

相关声明：[coap_tcp_append_block2_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaf3275841a174b4438c20a1e6e364ea8a)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)。

向 TCP 分组追加 BLOCK2 选项。

<a id="r_ga34c1c3b75e0787d8526b7a7a5b5a1633"></a>

```c
int coap_tcp_update_from_block (const struct coap_packet *cpkt, struct coap_block_context *ctx)
```

相关声明：[coap_tcp_update_from_block](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga34c1c3b75e0787d8526b7a7a5b5a1633)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)。

从 `cpkt` 获取 `BLOCK{1,2}` 和 `SIZE{1,2}`，并相应更新 `ctx`。

<a id="r_ga99e8ff6696fb7916932ae32c3e3ec8a2"></a>

```c
size_t coap_tcp_next_block (const struct coap_packet *cpkt, struct coap_block_context *ctx)
```

相关声明：[coap_tcp_next_block](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga99e8ff6696fb7916932ae32c3e3ec8a2)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)。

更新 `ctx`，使调用后当前条目指示正在传输的数据体中的正确偏移（Offset）。


## 3.6\_原页交叉引用（Cross References）

- [zephyr/types.h](../api_source_compiler_device_reference/P014_types.h_源码浏览.md)
- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/net/net_ip.h](../api_source_packet_gnss_reference/P005_net_ip.h_源码浏览.md)
- [zephyr/sys/math_extras.h](../math_reference/P003_数学辅助头文件源码.md)
- [zephyr/sys/slist.h](../slist_reference/P003_单向链表头文件源码.md)
- [查看此文件的源码。](../api_source_transport_clock_reference/P006_coap.h_源码浏览.md)
- [coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)
- [coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)
- [coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)
- [coap_option](../network_application_model_reference/P010_coap_option_结构体.md)
- [coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)
- [coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)
- [coap_reply](../network_application_model_reference/P015_coap_reply_结构体.md)
- [coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)
- [COAP_MAKE_RESPONSE_CODE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gabdcc1f443e89bd035522cbab7dfee879)
- [coap_method_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03129c8f853862f8395cc567edbf4642)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [coap_notify_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga4180b2476430fbe4a5e0418fb628ea91)
- [coap_reply_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga84eda10c4bf3e62241e686fdfa828868)
- [coap_option_num](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga7b8b3041e2f4ae26e663ff7431a6e6e3)
- [COAP_OPTION_IF_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4c61e26d11841c76debe2f99de5e9756)
- [COAP_OPTION_URI_HOST](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a402bb0a642a07d951c35d69736fd3f33)
- [COAP_OPTION_ETAG](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a0efdc30ce5551daffd093b2a8466978a)
- [COAP_OPTION_IF_NONE_MATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a07ea6f395818a7019bb9e6a6e34d2d74)
- [COAP_OPTION_OBSERVE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a06e91bbb4fa2144543d4148d3245ad25)
- [COAP_OPTION_URI_PORT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a344707b9f4cb71310f2ccf5e8050d17a)
- [COAP_OPTION_LOCATION_PATH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae82be3591d43f0d1c7e89ab764d969bd)
- [COAP_OPTION_OSCORE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3aaa6222533e1a6f1284fc5857884ad24d)
- [COAP_OPTION_URI_PATH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a96b5a15937e875b3087307cc5faab1af)
- [COAP_OPTION_CONTENT_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac3166e67b5f5bf3cefee58c8ff58e5b8)
- [COAP_OPTION_MAX_AGE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ab4cda4d3732fd12b9f203a2475c20981)
- [COAP_OPTION_URI_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3adb4d27052247b9a79ad7fcc0cc30c71c)
- [COAP_OPTION_ACCEPT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3afd0725f0ceb5ce22a6c7b390ca7efc9d)
- [COAP_OPTION_LOCATION_QUERY](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ac728800fc8f0d80e37dcf322e75eb27d)
- [COAP_OPTION_BLOCK2](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a4aa7cdfa66bd89f21f592eaf3ebe0972)
- [COAP_OPTION_BLOCK1](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a8aaa54af114fd1db631566afa69f162d)
- [COAP_OPTION_SIZE2](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a26c1bcd7af4fccd949e3de35fc2d88e6)
- [COAP_OPTION_PROXY_URI](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3ae4d2c93b545708926813217cd36a96ac)
- [COAP_OPTION_PROXY_SCHEME](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a30da986503e1e15243b74a16b161901c)
- [COAP_OPTION_SIZE1](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a53169a1c7b07c9e97f79dfc06af3eb51)
- [COAP_OPTION_ECHO](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a620e8b59f67f89de8a38dc76c8fcc594)
- [COAP_OPTION_NO_RESPONSE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a7984f2c4845610491bda964111a1c8e7)
- [COAP_OPTION_REQUEST_TAG](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a2a47428ec35972d256da05104ea6396f)
- [COAP_OPTION_SIGNAL_701_MMS](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a2b6f7575ff75fbc51ac5800a693b19af)
- [COAP_OPTION_SIGNAL_701_BWT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3aeed15ed39751b1533f4a1f825c73d0a2)
- [COAP_OPTION_SIGNAL_704_ALT_ADDR](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a9aa645f3c03f818848d5b728432998e3)
- [COAP_OPTION_SIGNAL_704_HOLD_OFF](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3af71df6b0647047115c20790eebb3ce30)
- [COAP_OPTION_SIGNAL_705_BAD_CSM](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga7b8b3041e2f4ae26e663ff7431a6e6e3a649cb25887a08fc21eb0cac51f58d3e5)
- [coap_method](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6a6547e3c755cf7a5033302c8294e0b7)
- [COAP_METHOD_GET](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7a025300cb0dc4c4de8eb0b0e0b4eb5317)
- [COAP_METHOD_POST](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7aba51bcab79bf75080ccf75c1ec38a3d6)
- [COAP_METHOD_PUT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7a91637ef7c9f57cdcc65d0118008251db)
- [COAP_METHOD_DELETE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7adccbea1fe9a43433cf8471e32208a5ac)
- [COAP_METHOD_FETCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7afa4070fed5c01b28bb1a59e3f0c021f4)
- [COAP_METHOD_PATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7adca55e3d2b4b41b249f6b2f67074d708)
- [COAP_METHOD_IPATCH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga6a6547e3c755cf7a5033302c8294e0b7a78f97b895f29819bf3f8b0314967f20e)
- [coap_msgtype](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3b375b7580246d1266293d09902f3d9f)
- [COAP_TYPE_CON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga3b375b7580246d1266293d09902f3d9fa65c04ee4847d0c595238079ac9564e8d)
- [COAP_TYPE_NON_CON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga3b375b7580246d1266293d09902f3d9fa629a304bea0c85c7b2bf746b26216a4f)
- [COAP_TYPE_ACK](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga3b375b7580246d1266293d09902f3d9fa7b2fe2187018bce9132af2763b57307d)
- [COAP_TYPE_RESET](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga3b375b7580246d1266293d09902f3d9fa287b951159fd51b84a2e0491b012f84c)
- [coap_response_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1ea81a365834e96f43ab7be573069d26)
- [COAP_RESPONSE_CODE_CREATED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26ad2d9fe8dd5beda74b522377c0b76275b)
- [COAP_RESPONSE_CODE_DELETED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26abf324915aa498c64a733a0098de4a082)
- [COAP_RESPONSE_CODE_VALID](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26aecaac4a0e9c821dfc20536951409dd48)
- [COAP_RESPONSE_CODE_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3)
- [COAP_RESPONSE_CODE_CONTENT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26adfd3e5e3c6ad5715127bb444c205fbce)
- [COAP_RESPONSE_CODE_CONTINUE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26ae4e3ff451c626421b9b329790f019dd8)
- [COAP_RESPONSE_CODE_BAD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5)
- [COAP_RESPONSE_CODE_UNAUTHORIZED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26acb76dbf11b47477144cc4ece3357283c)
- [COAP_RESPONSE_CODE_BAD_OPTION](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a989a6528edc653c0b693ed875481e82d)
- [COAP_RESPONSE_CODE_FORBIDDEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26afeee555ef54f138db58b14ad2c328d04)
- [COAP_RESPONSE_CODE_NOT_FOUND](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a86c2bff8add69428d164431b3091a8e9)
- [COAP_RESPONSE_CODE_NOT_ALLOWED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a301eb722445472dba93d5accd6e0dd31)
- [COAP_RESPONSE_CODE_NOT_ACCEPTABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a4d77322514521e8dfea01f4a1a6e5886)
- [COAP_RESPONSE_CODE_INCOMPLETE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a671730c6d2f1a339fcd557c5452150af)
- [COAP_RESPONSE_CODE_CONFLICT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26ab447505d233aed9fd8ad28070d317544)
- [COAP_RESPONSE_CODE_PRECONDITION_FAILED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a289ade02833b57bffd915e648e050e52)
- [COAP_RESPONSE_CODE_REQUEST_TOO_LARGE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26aaa43062a8146c1e2e09183228a540d2e)
- [COAP_RESPONSE_CODE_UNSUPPORTED_CONTENT_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26aef6b165b9d3f8f4b477431058815c16b)
- [COAP_RESPONSE_CODE_UNPROCESSABLE_ENTITY](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a5e5e31cc4647d5e0fdd1c8fe6cfa2661)
- [COAP_RESPONSE_CODE_TOO_MANY_REQUESTS](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26aabd72cff6669d382aa04c53e764d0b49)
- [COAP_RESPONSE_CODE_INTERNAL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499)
- [COAP_RESPONSE_CODE_NOT_IMPLEMENTED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a85c04541bc8580c2ae915946fd677c15)
- [COAP_RESPONSE_CODE_BAD_GATEWAY](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a8de29a7ee6bb960a97d6b415217b4640)
- [COAP_RESPONSE_CODE_SERVICE_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26afebd274586351951ffe9c8f26b270dec)
- [COAP_RESPONSE_CODE_GATEWAY_TIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26af6d379fef704c269406b782c60772ecd)
- [COAP_RESPONSE_CODE_PROXYING_NOT_SUPPORTED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a5f49a566d37b2cda0c624d76aee08bd1)
- [COAP_SIGNAL_CODE_CSM](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26ac528f38c3e8553d83e0455097f4fbdf9)
- [COAP_SIGNAL_CODE_PING](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a7390f381b1aa8a4aa21d98527950a152)
- [COAP_SIGNAL_CODE_PONG](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26abc76b74967e491c10f320bf19c9026d4)
- [COAP_SIGNAL_CODE_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a026916ae7964a98edeadd3f09e9d18ad)
- [COAP_SIGNAL_CODE_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a95a8d4bee68a3829dfb4f3a024c8bf68)
- [coap_content_format](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga94a8f9956742d3928fc3c63b8d01ae73)
- [COAP_CONTENT_FORMAT_TEXT_PLAIN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73af068aa8d09032352799bc60868607997)
- [COAP_CONTENT_FORMAT_APP_LINK_FORMAT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a1fbd90fd5cb309e2de6954f46174dc4f)
- [COAP_CONTENT_FORMAT_APP_XML](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73adb96bf55e914f4852e92dc65752c372a)
- [COAP_CONTENT_FORMAT_APP_OCTET_STREAM](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a88d952174bb3e4ffb9ab11a599952760)
- [COAP_CONTENT_FORMAT_APP_EXI](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a483a382550b38468cc66bdce9f4743ea)
- [COAP_CONTENT_FORMAT_APP_JSON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a975381d286c1e9b998e41ef0a234d17a)
- [COAP_CONTENT_FORMAT_APP_JSON_PATCH_JSON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a141f183724ad6da14c3992c0990d6239)
- [COAP_CONTENT_FORMAT_APP_MERGE_PATCH_JSON](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a2797149fb3811d706dab291e9edc9436)
- [COAP_CONTENT_FORMAT_APP_CBOR](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga94a8f9956742d3928fc3c63b8d01ae73a7ca73ff57a6c7fb1517b44f2ce17d3f9)
- [coap_no_response](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2a323287262bbb6a4932e7911ddb652c)
- [COAP_NO_RESPONSE_SUPPRESS_2_XX](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga2a323287262bbb6a4932e7911ddb652caeeb51bb18780c20df5b25183d52d42de)
- [COAP_NO_RESPONSE_SUPPRESS_4_XX](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga2a323287262bbb6a4932e7911ddb652cae8b0b1231d095b3e7a972ca4c86d8dce)
- [COAP_NO_RESPONSE_SUPPRESS_5_XX](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga2a323287262bbb6a4932e7911ddb652ca19ebfb46899b440124322bb67c906cb3)
- [COAP_NO_RESPONSE_SUPPRESS_ALL](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga2a323287262bbb6a4932e7911ddb652ca21758021d7f3a36bf6ede06daa82dbf0)
- [coap_block_size](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga712c1468f936a3af7dc39a86a5961922)
- [COAP_BLOCK_16](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a834d479806b513818e2237f3f1c56968)
- [COAP_BLOCK_32](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a1aaf8f841c18e281b176793bb331993d)
- [COAP_BLOCK_64](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a7266f448a391ea2a2763f1ded5397520)
- [COAP_BLOCK_128](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a147ddf4b0e5d1a8c11f0da2c71dee4d8)
- [COAP_BLOCK_256](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922acfc37f84eabccdde4bd84b06c6a5e753)
- [COAP_BLOCK_512](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922ad2052905aff08c58585dcf6c6caddc19)
- [COAP_BLOCK_1024](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a6998c79e63cf65e7f86ddd5713d48dce)
- [COAP_BLOCK_BERT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga712c1468f936a3af7dc39a86a5961922a549135603208a878cdefd6c5ca1a039b)
- [RFC 7959](https://datatracker.ietf.org/doc/html/rfc7959)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [coap_header_get_version](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafd01c39fac8f173edc04337161e92264)
- [coap_header_get_type](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaed883ea6cec3acc5eb570e152dc52e25)
- [coap_header_get_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6a5049accfa0cd7106a3a6593c598545)
- [coap_header_get_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gae4bf952fdf9e3d03ab0b0df4c3c0d054)
- [coap_header_set_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafdaecca5ad26bab4fb7c9ee3477318f8)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [coap_header_get_id](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga63388c629da5370d2e711cdc9aabd837)
- [coap_packet_get_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga28ccf00fb1f5f13f747e61c2e3008b5c)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [coap_uri_path_match](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga8b621232b740d8e8e1771fba24897121)
- [coap_packet_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga27a58a69f632551aa7a2394ae2badacf)
- [coap_packet_set_path](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gab8f9e9cdfa20920d5d25fb1507a2286d)
- [coap_packet_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga90e6aab174f8977f0a3b5fbe1a20297c)
- [coap_ack_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gae6d93b1f93734302be75ee417813e5d1)
- [coap_rst_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga9626781d73d18c1305f654ef4723e5db)
- [coap_next_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga66f986f8a1157236bea27133c2a2538b)
- [coap_next_id](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gade5f4995c6419db03ce3e7ff7ca1cfcb)
- [coap_find_options](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaf006c8048ed7b863e70dbdd64bc3d608)
- [coap_packet_append_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2aa4140ee83ca4090a5604e34d1f1446)
- [coap_packet_remove_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaca300a216781d360d2cd64e8e9f1ae8f)
- [unsigned](../api_file_reference/P186_____w__zephyr__zephyr__lib__libc__minimal__include__sys__types.h_文件参考.md#a4089fb16419d359081465355db05f846)
- [coap_option_value_to_int](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2fd0613e61274ec4b9b7bab3ab11ccce)
- [coap_append_option_int](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6bec94992ac450dca03436a6ad74efb4)
- [coap_packet_append_payload_marker](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga24000def8534acdcd2c61836dc690367)
- [coap_packet_append_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gadcd3a93a702a2a0b428f39b71dd67954)
- [coap_packet_is_request](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga323644931c927b8988aafd89dacb993c)
- [coap_handle_request_len](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gab8ab58c900a4b0396ca7722c754fb1ec)
- [coap_handle_request](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaa170f8dbe1633e2b02c9c2d8dd27f181)
- [coap_block_size_to_bytes](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafffadd4a837e48fd72af20468ccd86f2)
- [coap_bytes_to_block_size](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga27e3008b8511333e0c0115ba928017f3)
- [coap_block_transfer_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga57486e764f0feb6544fa3b0d19935afd)
- [coap_append_descriptive_block_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga8b5966a29054ace04cae81d4da588e72)
- [coap_has_descriptive_block_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaabdfa8cf28cc2c3a14ae0af5fa7e7212)
- [coap_remove_descriptive_block_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga941ee9d68f1a628755aa79c249cbae58)
- [coap_block_has_more](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafc61a6878d82f81565ab752ced0ce2be)
- [coap_append_block1_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga518d5f4422ff45f2b4a296f249da89cd)
- [coap_append_block2_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga361c17b698bdaa0fc529b7338efefd8c)
- [coap_append_size1_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3f66d5935dcacfeebcac2b3001d7b57a)
- [coap_append_size2_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gafbc8c15ef03b762f9411c38b03aa403b)
- [coap_get_option_int](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga21b8f4ffeecc7900f6bf299836d2b5b3)
- [coap_get_block1_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga10c4a0d7e2052f3116fbf3b355fe75db)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [coap_get_block2_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga196390e6f016b72b3ae2ae9e69bed1b7)
- [coap_update_from_block](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3b0cc9bfabdddeffd98f36d7f15dd416)
- [coap_next_block_for_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga50f7837da003601479dbc470ba9898ae)
- [coap_next_block](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1244716ecf06fad1013131c42eab8c5c)
- [coap_age_is_newer](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga998a3b01a3a535614183ac08da101811)
- [coap_observer_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga262f21fdad778db96c8bd700ba66ce1b)
- [coap_observer_init_oscore](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga34c5eac86081ea46b63c1cbb7c1315e9)
- [coap_register_observer](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga3c42861f8442e548f560acf3deca6baa)
- [coap_remove_observer](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga33c351ac06b5ae9217cd53d8cf330fbd)
- [coap_find_observer](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gab045e6e61ef8c35f85591b8792d88952)
- [coap_find_observer_by_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6542f6350f6e4ed861d6c482617dd5d0)
- [coap_find_observer_by_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gadeaa59fd7b6eab454d5930289b4e08f7)
- [coap_observer_next_unused](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2410e973bf3192244426df346230608b)
- [coap_reply_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gacfe30c84434dc8adbf3d399ec0e51bec)
- [coap_pending_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga0b84eee85b854bf087bceb7566e93086)
- [coap_pending_next_unused](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga800831ddfe19b1a5637a5edd9e78c470)
- [coap_reply_next_unused](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga65cb5f7ac01ea5ebe1c6e30a7c70ad4e)
- [coap_pending_received](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga94ceba78cbd2440f91d9b30d6b06594d)
- [coap_response_received](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga44ca9e8b0fe2544b8da73efda10b187b)
- [coap_pending_next_to_expire](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga9d63518c701ebdb4c7f65c5368d00d27)
- [coap_pending_cycle](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga2bcfc7340ed2347862b0f003e1b00a4b)
- [coap_pending_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga03287eb3187aa28e0e83e0e0c72e2631)
- [coap_pendings_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6e0947048052e733a3571fdc8955b2d7)
- [coap_pendings_count](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gad9db2ced9b882265c16e3039f893ca03)
- [coap_reply_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga37b58c38c150751d31207ece416529d8)
- [coap_replies_clear](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaddb02509934f5bac20b7c7f83aea4cd8)
- [coap_resource_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gad0c738d308f9cca8ea5cdb79449282cb)
- [coap_request_is_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga46b315c30b642eec65bcb84e9c937ee7)
- [coap_get_transmission_parameters](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1bd7be0a5390f0599e7bec0cbd79daf8)
- [coap_set_transmission_parameters](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaf361fd233f1aa650650108ae1e205ede)
- [coap_check_unsupported_critical_options](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga59f6d6ff09861ab3df9cda894f45de40)
- [coap_tcp_header_get_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaa715f58474d6f668f47dc66e478ba6b2)
- [coap_tcp_header_get_code](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gab2dc876158b3248fa35fbc61a1faf19a)
- [coap_tcp_packet_get_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga1adc19283d0b41f6af152d41b32b86d7)
- [coap_tcp_packet_parse](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaf2cd52a5976556c2093bc770bb61c192)
- [coap_tcp_packet_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga5d9fd91c714705b56780264823c56fe6)
- [coap_tcp_packet_update_len](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gae5829b14002cc4d24cf8501ab960c35a)
- [coap_tcp_append_block2_option](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gaf3275841a174b4438c20a1e6e364ea8a)
- [coap_tcp_update_from_block](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga34c1c3b75e0787d8526b7a7a5b5a1633)
- [coap_tcp_next_block](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga99e8ff6696fb7916932ae32c3e3ec8a2)

<a id="header-details"></a>

---

[上一章](P002_zephyr__dt-bindings__pinctrl__ch570-pinctrl.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__dt-bindings__mfd__infineon-autanalog.h_文件参考.md)
