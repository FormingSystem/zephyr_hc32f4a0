---
id: learning.zephyr-docs.api-file-host-video-reference.page-2
title: zephyr__net__coap_service.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap__service_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_zephyr\_\_net\_\_coap\_service.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/coap__service_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP服务（Service）的API。

<a id="details"></a>

```c
#include <zephyr/net/coap.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/tls_credentials.h>
```

查看此文件的源码。

受限应用协议服务（CoAP Service）API。供应用响应 CoAP 请求的 API。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 2.1\_宏定义（Macros）

<a id="r_gaef40d300170926ad131d06ce62c63d6a"></a>

```c
#define COAP_RESOURCE_DEFINE(_name, _service, ...)
```

相关声明：[COAP_RESOURCE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gaef40d300170926ad131d06ce62c63d6a)。

定义由名为 `_service` 的服务拥有的静态 CoAP 资源（Static CoAP Resource）。

<a id="r_ga8dc5473755efd48548ec4cb6ac2584ec"></a>

```c
#define COAP_SERVICE_DEFINE(_name, _host, _port, _flags)
```

相关声明：[COAP_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga8dc5473755efd48548ec4cb6ac2584ec)。

定义具有静态资源（Static Resources）的 CoAP 服务。

<a id="r_ga1ec49f2bc2c378431c4721080a13d11d"></a>

```c
#define COAPS_SERVICE_DEFINE(_name, _host, _port, _flags, _sec_tag_list, _sec_tag_list_size)
```

相关声明：[COAPS_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga1ec49f2bc2c378431c4721080a13d11d)。

定义具有静态资源的安全 CoAP 服务（Secure Service）。

<a id="r_ga306c2f205e9008a2bd3f1862f33460d8"></a>

```c
#define COAP_SERVICE_DEFINE_OSCORE(_name, _host, _port, _flags, _oscore_required)
```

相关声明：[COAP_SERVICE_DEFINE_OSCORE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga306c2f205e9008a2bd3f1862f33460d8)。

定义启用受限 RESTful 环境对象安全（OSCORE）、且具有静态资源的 CoAP 服务。

<a id="r_gafbc0c4c98d1cefe0a77b4ffb28cefe88"></a>

```c
#define COAPS_SERVICE_DEFINE_OSCORE(_name, _host, _port, _flags, _sec_tag_list, _sec_tag_list_size, _oscore_required)
```

相关声明：[COAPS_SERVICE_DEFINE_OSCORE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gafbc0c4c98d1cefe0a77b4ffb28cefe88)。

定义启用 OSCORE、且具有静态资源的安全 CoAP 服务，采用数据报传输层安全（DTLS）。

<a id="r_ga1f0c3bf81baa9da11197a74415d3a9ae"></a>

```c
#define COAP_SERVICE_COUNT(_dst)
```

相关声明：[COAP_SERVICE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga1f0c3bf81baa9da11197a74415d3a9ae)。

统计 CoAP 服务数量（Number of Services）。

<a id="r_gade9e9a55968a5ad6b3addbb08f2ccb6f"></a>

```c
#define COAP_SERVICE_RESOURCE_COUNT(_service)
```

相关声明：[COAP_SERVICE_RESOURCE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gade9e9a55968a5ad6b3addbb08f2ccb6f)。

统计 CoAP 服务的静态资源（Static Resources）数量。

<a id="r_gaf01cb4d11b18272eb27be93cb1a7197b"></a>

```c
#define COAP_SERVICE_HAS_RESOURCE(_service, _resource)
```

相关声明：[COAP_SERVICE_HAS_RESOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gaf01cb4d11b18272eb27be93cb1a7197b)。

检查服务是否具有指定资源（Resource）。

<a id="r_gab4d154d5b02235a83c7a2c681b1e22e7"></a>

```c
#define COAP_SERVICE_FOREACH(_it)
```

相关声明：[COAP_SERVICE_FOREACH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gab4d154d5b02235a83c7a2c681b1e22e7)。

遍历全部 CoAP 服务（Services）。

<a id="r_gac3e92107fa12b111771d56987a242b1a"></a>

```c
#define COAP_RESOURCE_FOREACH(_service, _it)
```

相关声明：[COAP_RESOURCE_FOREACH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gac3e92107fa12b111771d56987a242b1a)。

遍历与所给 `_service` 关联的静态 CoAP 资源（Static CoAP Resources）。

<a id="r_gaaca92287c495f4afb79e584c47316037"></a>

```c
#define COAP_SERVICE_FOREACH_RESOURCE(_service, _it)
```

相关声明：[COAP_SERVICE_FOREACH_RESOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gaaca92287c495f4afb79e584c47316037)。

遍历与 `_service` 关联的全部静态资源（Static Resources）。

<a id="define-members-0"></a>

### CoAP 服务配置标志（Service Configuration Flags）



<a id="r_gaf5799a7fbf309f8963d22039a6fe2fbb"></a>

```c
#define COAP_SERVICE_AUTOSTART BIT(0)
```

相关声明：[COAP_SERVICE_AUTOSTART](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gaf5799a7fbf309f8963d22039a6fe2fbb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启动时自动启动服务（Start on Boot）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 2.2\_函数（Functions）

<a id="r_gad1e64f8fe2c6ae32730a9a61f8351bab"></a>

```c
int coap_service_start (const struct coap_service *service)
```

相关声明：[coap_service_start](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gad1e64f8fe2c6ae32730a9a61f8351bab)。

启动所给服务（Service）。

<a id="r_ga58bc31fc4d53ebce9c18ccbc5aab72ce"></a>

```c
int coap_service_stop (const struct coap_service *service)
```

相关声明：[coap_service_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga58bc31fc4d53ebce9c18ccbc5aab72ce)。

停止所给服务（Service）。

<a id="r_ga08638f2001ca2f807489c12ff426784c"></a>

```c
int coap_service_is_running (const struct coap_service *service)
```

相关声明：[coap_service_is_running](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga08638f2001ca2f807489c12ff426784c)。

查询所给服务的运行状态（Running State）。

<a id="r_ga19a7a0e3aa5b56ef5cd6c0ce8f142147"></a>

```c
int coap_service_send (const struct coap_service *service, const struct coap_packet *cpkt, const struct net_sockaddr *addr, net_socklen_t addr_len, const struct coap_transmission_parameters *params)
```

相关声明：[coap_service_send](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga19a7a0e3aa5b56ef5cd6c0ce8f142147)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)。

从所给服务（Service）发送 CoAP 消息。

<a id="r_ga40a0a599471f7f283b455809d4cf7587"></a>

```c
int coap_resource_send (const struct coap_resource *resource, const struct coap_packet *cpkt, const struct net_sockaddr *addr, net_socklen_t addr_len, const struct coap_transmission_parameters *params)
```

相关声明：[coap_resource_send](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga40a0a599471f7f283b455809d4cf7587)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)。

从所给资源（Resource）发送 CoAP 消息。

<a id="r_gaa25bfeb07a50674f054b5b56005ac021"></a>

```c
int coap_resource_parse_observe (struct coap_resource *resource, const struct coap_packet *request, const struct net_sockaddr *addr)
```

相关声明：[coap_resource_parse_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gaa25bfeb07a50674f054b5b56005ac021)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

为所给资源解析 CoAP 观察请求（Observe Request）。

<a id="r_ga7329c8a02caa7a0d9becb669932895ca"></a>

```c
int coap_resource_remove_observer_by_addr (struct coap_resource *resource, const struct net_sockaddr *addr)
```

相关声明：[coap_resource_remove_observer_by_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga7329c8a02caa7a0d9becb669932895ca)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

按地址查找观察者（Observer），并将其从资源中移除。

<a id="r_gad575a7209a56874002c540eb3f8c0733"></a>

```c
int coap_resource_remove_observer_by_token (struct coap_resource *resource, const uint8_t *token, uint8_t token_len)
```

相关声明：[coap_resource_remove_observer_by_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gad575a7209a56874002c540eb3f8c0733)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

按令牌（Token）查找观察者（Observer），并将其从资源中移除。


## 2.3\_原页交叉引用（Cross References）

- [zephyr/net/coap.h](../api_source_transport_clock_reference/P006_coap.h_源码浏览.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/tls_credentials.h](../api_source_reference/P870_tls_credentials.h_源码浏览.md)
- [查看此文件的源码。](../api_source_device_reference/P004_coap_service.h_源码浏览.md)
- [COAP_RESOURCE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gaef40d300170926ad131d06ce62c63d6a)
- [COAP_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga8dc5473755efd48548ec4cb6ac2584ec)
- [COAPS_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga1ec49f2bc2c378431c4721080a13d11d)
- [COAP_SERVICE_DEFINE_OSCORE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga306c2f205e9008a2bd3f1862f33460d8)
- [COAPS_SERVICE_DEFINE_OSCORE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gafbc0c4c98d1cefe0a77b4ffb28cefe88)
- [COAP_SERVICE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga1f0c3bf81baa9da11197a74415d3a9ae)
- [COAP_SERVICE_RESOURCE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gade9e9a55968a5ad6b3addbb08f2ccb6f)
- [COAP_SERVICE_HAS_RESOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gaf01cb4d11b18272eb27be93cb1a7197b)
- [COAP_SERVICE_FOREACH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gab4d154d5b02235a83c7a2c681b1e22e7)
- [COAP_RESOURCE_FOREACH](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gac3e92107fa12b111771d56987a242b1a)
- [COAP_SERVICE_FOREACH_RESOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gaaca92287c495f4afb79e584c47316037)
- [COAP_SERVICE_AUTOSTART](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gaf5799a7fbf309f8963d22039a6fe2fbb)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [coap_service_start](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gad1e64f8fe2c6ae32730a9a61f8351bab)
- [coap_service_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga58bc31fc4d53ebce9c18ccbc5aab72ce)
- [coap_service_is_running](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga08638f2001ca2f807489c12ff426784c)
- [coap_service_send](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga19a7a0e3aa5b56ef5cd6c0ce8f142147)
- [coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)
- [coap_resource_send](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga40a0a599471f7f283b455809d4cf7587)
- [coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)
- [coap_resource_parse_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gaa25bfeb07a50674f054b5b56005ac021)
- [coap_resource_remove_observer_by_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#ga7329c8a02caa7a0d9becb669932895ca)
- [coap_resource_remove_observer_by_token](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html#gad575a7209a56874002c540eb3f8c0733)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)

<a id="COAP_SERVICE_FLAGS"></a>
<a id="header-details"></a>

---

[上一章](P001_zephyr__arch__arch_interface.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P003_zephyr__drivers__mipi_dbi.h_文件参考.md)
