---
id: learning.zephyr-docs.api-coap-trusted-topic-reference.page-8
title: CoAP 服务 API
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第8章\_CoAP 服务 API

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__service.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

CoAP服务（Service）的API。

<a id="details"></a>

CoAP 服务 API（Service API）。自 3.6 起提供（Since 3.6），版本（Version）0.1.0。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 8.1\_宏定义（Macros）

<a id="r_gaef40d300170926ad131d06ce62c63d6a"></a>

```c
#define COAP_RESOURCE_DEFINE(_name, _service, ...)
```

相关声明：[COAP_RESOURCE_DEFINE](#gaef40d300170926ad131d06ce62c63d6a)。

定义由名为 `_service` 的服务拥有的静态 CoAP 资源（Static CoAP Resource）。

<a id="r_ga8dc5473755efd48548ec4cb6ac2584ec"></a>

```c
#define COAP_SERVICE_DEFINE(_name, _host, _port, _flags)
```

相关声明：[COAP_SERVICE_DEFINE](#ga8dc5473755efd48548ec4cb6ac2584ec)。

定义具有静态资源（Static Resources）的 CoAP 服务。

<a id="r_ga1ec49f2bc2c378431c4721080a13d11d"></a>

```c
#define COAPS_SERVICE_DEFINE(_name, _host, _port, _flags, _sec_tag_list, _sec_tag_list_size)
```

相关声明：[COAPS_SERVICE_DEFINE](#ga1ec49f2bc2c378431c4721080a13d11d)。

定义具有静态资源的安全 CoAP 服务（Secure Service）。

<a id="r_ga306c2f205e9008a2bd3f1862f33460d8"></a>

```c
#define COAP_SERVICE_DEFINE_OSCORE(_name, _host, _port, _flags, _oscore_required)
```

相关声明：[COAP_SERVICE_DEFINE_OSCORE](#ga306c2f205e9008a2bd3f1862f33460d8)。

定义启用受限 RESTful 环境对象安全（OSCORE）、且具有静态资源的 CoAP 服务。

<a id="r_gafbc0c4c98d1cefe0a77b4ffb28cefe88"></a>

```c
#define COAPS_SERVICE_DEFINE_OSCORE(_name, _host, _port, _flags, _sec_tag_list, _sec_tag_list_size, _oscore_required)
```

相关声明：[COAPS_SERVICE_DEFINE_OSCORE](#gafbc0c4c98d1cefe0a77b4ffb28cefe88)。

定义启用 OSCORE、且具有静态资源的安全 CoAP 服务，采用数据报传输层安全（DTLS）。

<a id="r_ga1f0c3bf81baa9da11197a74415d3a9ae"></a>

```c
#define COAP_SERVICE_COUNT(_dst)
```

相关声明：[COAP_SERVICE_COUNT](#ga1f0c3bf81baa9da11197a74415d3a9ae)。

统计 CoAP 服务数量（Number of Services）。

<a id="r_gade9e9a55968a5ad6b3addbb08f2ccb6f"></a>

```c
#define COAP_SERVICE_RESOURCE_COUNT(_service)
```

相关声明：[COAP_SERVICE_RESOURCE_COUNT](#gade9e9a55968a5ad6b3addbb08f2ccb6f)。

统计 CoAP 服务的静态资源（Static Resources）数量。

<a id="r_gaf01cb4d11b18272eb27be93cb1a7197b"></a>

```c
#define COAP_SERVICE_HAS_RESOURCE(_service, _resource)
```

相关声明：[COAP_SERVICE_HAS_RESOURCE](#gaf01cb4d11b18272eb27be93cb1a7197b)。

检查服务是否具有指定资源（Resource）。

<a id="r_gab4d154d5b02235a83c7a2c681b1e22e7"></a>

```c
#define COAP_SERVICE_FOREACH(_it)
```

相关声明：[COAP_SERVICE_FOREACH](#gab4d154d5b02235a83c7a2c681b1e22e7)。

遍历全部 CoAP 服务（Services）。

<a id="r_gac3e92107fa12b111771d56987a242b1a"></a>

```c
#define COAP_RESOURCE_FOREACH(_service, _it)
```

相关声明：[COAP_RESOURCE_FOREACH](#gac3e92107fa12b111771d56987a242b1a)。

遍历与所给 `_service` 关联的静态 CoAP 资源（Static CoAP Resources）。

<a id="r_gaaca92287c495f4afb79e584c47316037"></a>

```c
#define COAP_SERVICE_FOREACH_RESOURCE(_service, _it)
```

相关声明：[COAP_SERVICE_FOREACH_RESOURCE](#gaaca92287c495f4afb79e584c47316037)。

遍历与 `_service` 关联的全部静态资源（Static Resources）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 8.2\_函数（Functions）

<a id="r_gad1e64f8fe2c6ae32730a9a61f8351bab"></a>

```c
int coap_service_start (const struct coap_service *service)
```

相关声明：[coap_service_start](#gad1e64f8fe2c6ae32730a9a61f8351bab)。

启动所给服务（Service）。

<a id="r_ga58bc31fc4d53ebce9c18ccbc5aab72ce"></a>

```c
int coap_service_stop (const struct coap_service *service)
```

相关声明：[coap_service_stop](#ga58bc31fc4d53ebce9c18ccbc5aab72ce)。

停止所给服务（Service）。

<a id="r_ga08638f2001ca2f807489c12ff426784c"></a>

```c
int coap_service_is_running (const struct coap_service *service)
```

相关声明：[coap_service_is_running](#ga08638f2001ca2f807489c12ff426784c)。

查询所给服务的运行状态（Running State）。

<a id="r_ga19a7a0e3aa5b56ef5cd6c0ce8f142147"></a>

```c
int coap_service_send (const struct coap_service *service, const struct coap_packet *cpkt, const struct net_sockaddr *addr, net_socklen_t addr_len, const struct coap_transmission_parameters *params)
```

相关声明：[coap_service_send](#ga19a7a0e3aa5b56ef5cd6c0ce8f142147)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)。

从所给服务（Service）发送 CoAP 消息。

<a id="r_ga40a0a599471f7f283b455809d4cf7587"></a>

```c
int coap_resource_send (const struct coap_resource *resource, const struct coap_packet *cpkt, const struct net_sockaddr *addr, net_socklen_t addr_len, const struct coap_transmission_parameters *params)
```

相关声明：[coap_resource_send](#ga40a0a599471f7f283b455809d4cf7587)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)、[net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)、[coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)。

从所给资源（Resource）发送 CoAP 消息。

<a id="r_gaa25bfeb07a50674f054b5b56005ac021"></a>

```c
int coap_resource_parse_observe (struct coap_resource *resource, const struct coap_packet *request, const struct net_sockaddr *addr)
```

相关声明：[coap_resource_parse_observe](#gaa25bfeb07a50674f054b5b56005ac021)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

为所给资源解析 CoAP 观察请求（Observe Request）。

<a id="r_ga7329c8a02caa7a0d9becb669932895ca"></a>

```c
int coap_resource_remove_observer_by_addr (struct coap_resource *resource, const struct net_sockaddr *addr)
```

相关声明：[coap_resource_remove_observer_by_addr](#ga7329c8a02caa7a0d9becb669932895ca)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)。

按地址查找观察者（Observer），并将其从资源中移除。

<a id="r_gad575a7209a56874002c540eb3f8c0733"></a>

```c
int coap_resource_remove_observer_by_token (struct coap_resource *resource, const uint8_t *token, uint8_t token_len)
```

相关声明：[coap_resource_remove_observer_by_token](#gad575a7209a56874002c540eb3f8c0733)、[coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)、[uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)。

按令牌（Token）查找观察者（Observer），并将其从资源中移除。

<a id="header-member-group"></a>
<a id="member-group"></a>

## 8.3\_CoAP 服务配置标志（Service Configuration Flags）



<a id="r_gaf5799a7fbf309f8963d22039a6fe2fbb"></a>

```c
#define COAP_SERVICE_AUTOSTART BIT(0)
```

相关声明：[COAP_SERVICE_AUTOSTART](#gaf5799a7fbf309f8963d22039a6fe2fbb)、[BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)。

启动时自动启动服务（Start on Boot）。

## 8.4\_详细说明（Detailed Documentation）

<a id="gaef40d300170926ad131d06ce62c63d6a"></a>

### `COAP_RESOURCE_DEFINE`

```c
#define COAP_RESOURCE_DEFINE ( _name, _service, ... )
```

```c
#include <zephyr/net/coap_service.h>
```

展开值（Value）：

```c
STRUCT_SECTION_ITERABLE_ALTERNATE(_CONCAT(coap_resource_, _service), coap_resource,     \
                                  _name) = __VA_ARGS__
```

定义由名为 `_service` 的服务拥有的静态 CoAP 资源（Static CoAP Resource）。

原始示例（Example）：

```c
static const struct gpio_dt_spec led = GPIO_DT_SPEC_GET(DT_ALIAS(led0), gpios);

static int led_put(struct coap_resource *resource, struct coap_packet *request,
                   struct net_sockaddr *addr, net_socklen_t addr_len)
{
        const uint8_t *payload;
        uint16_t payload_len;

        payload = coap_packet_get_payload(request, &payload_len);
        if (payload_len != 1) {
                return COAP_RESPONSE_CODE_BAD_REQUEST;
        }

        if (gpio_pin_set_dt(&led, payload[0]) < 0) {
                return COAP_RESPONSE_CODE_INTERNAL_ERROR;
        }

        return COAP_RESPONSE_CODE_CHANGED;
}

COAP_RESOURCE_DEFINE(my_resource, my_service, {
        .put = led_put,
});
```

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 资源名称（Resource Name）。 |
| `_service` | 关联服务名称（Associated Service Name）。 |

**说明（Note）**：注意（Note）：为资源注册的处理函数（Handlers）可以返回 CoAP 响应码，回复不含负载的确认消息（Acknowledge）；返回值为 0 或负值时，不发送任何内容。示例展示了这一行为。

<a id="gac3e92107fa12b111771d56987a242b1a"></a>

### `COAP_RESOURCE_FOREACH`

```c
#define COAP_RESOURCE_FOREACH ( _service, _it )
```

```c
#include <zephyr/net/coap_service.h>
```

展开值（Value）：

```c
STRUCT_SECTION_FOREACH_ALTERNATE(_CONCAT(coap_resource_, _service), coap_resource, _it)
```

遍历与所给 `_service` 关联的静态 CoAP 资源（Static CoAP Resources）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_service` | CoAP 服务名称（Service Name）。 |
| `_it` | 迭代器名称（Iterator Name），类型为 coap_resource。 |

**说明（Note）**：注意（Note）：此宏要求 _service 使用 COAP_SERVICE_DEFINE 定义。

<a id="gaf5799a7fbf309f8963d22039a6fe2fbb"></a>

### `COAP_SERVICE_AUTOSTART`

```c
#define COAP_SERVICE_AUTOSTART BIT(0)
```

```c
#include <zephyr/net/coap_service.h>
```

启动时自动启动服务（Start on Boot）。

<a id="ga1f0c3bf81baa9da11197a74415d3a9ae"></a>

### `COAP_SERVICE_COUNT`

```c
#define COAP_SERVICE_COUNT ( _dst)
```

```c
#include <zephyr/net/coap_service.h>
```

展开值（Value）：

```c
STRUCT_SECTION_COUNT(coap_service, _dst)
```

统计 CoAP 服务数量（Number of Services）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] _dst` | 指向用于写入结果的位置。 |

<a id="ga8dc5473755efd48548ec4cb6ac2584ec"></a>

### `COAP_SERVICE_DEFINE`

```c
#define COAP_SERVICE_DEFINE ( _name, _host, _port, _flags )
```

```c
#include <zephyr/net/coap_service.h>
```

展开值（Value）：

```c
extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[];       \
extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[];         \
__z_coap_service_define(_name, _host, _port, _flags,                                       \
                        &_CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[0],         \
                        &_CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[0], NULL, 0,  \
                        false, NULL)
```

定义具有静态资源（Static Resources）的 CoAP 服务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` _name` | 服务名称（Service Name）。 |
| ` _host` | 与服务关联的 IP 地址或主机名（Hostname）。 |
| `[in,out] _port` | 指向与服务关联的端口的指针。 |
| ` _flags` | 配置标志（Configuration Flags）。 |

**说明（Note）**：注意（Note）：_host 参数可以为 NULL。非 NULL 时，它用于指定 IPv4 或 IPv6 格式的 IP 地址、完全限定主机名（Fully-qualified Hostname）或虚拟主机（Virtual Host）；为 NULL 时使用任意地址（Any Address）。_port 参数必须非 NULL，指向存放服务所用端口号的位置。如果指定端口号为 0，将使用临时端口号（Ephemeral Port Number），并将实际分配的端口号写回该内存。使用临时端口号时，_port 指向的内存必须可写。

**参阅（See Also）**：另请参见（See Also）：COAP_SERVICE_FLAGS。

<a id="ga306c2f205e9008a2bd3f1862f33460d8"></a>

### `COAP_SERVICE_DEFINE_OSCORE`

```c
#define COAP_SERVICE_DEFINE_OSCORE ( _name, _host, _port, _flags, _oscore_required )
```

```c
#include <zephyr/net/coap_service.h>
```

展开值（Value）：

```c
extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[];       \
extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[];         \
__z_coap_oscore_cache_define(_name) __z_coap_service_define(                               \
        _name, _host, _port, _flags,                                                       \
        &_CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[0],                         \
        &_CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[0], NULL, 0,                  \
        (_oscore_required), __z_coap_oscore_cache_ptr(_name))
```

定义启用受限 RESTful 环境对象安全（OSCORE）、且具有静态资源的 CoAP 服务。

行为与 COAP_SERVICE_DEFINE 相同，但额外为服务接入对象安全（OSCORE）支持，参见 RFC 8613。为每项服务静态分配 OSCORE 交换缓存（Exchange Cache）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` _name` | 服务名称（Service Name）。 |
| ` _host` | 与服务关联的 IP 地址或主机名（Hostname）。 |
| `[in,out] _port` | 指向与服务关联的端口的指针。 |
| ` _flags` | 配置标志（Configuration Flags）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_oscore_required` | 为 true 时，不使用 OSCORE 的请求会被拒绝，返回 4.01 Unauthorized（未授权）。 |

**说明（Note）**：注意（Note）：需要 CONFIG_COAP_OSCORE。禁用此选项时，服务退化为普通的 COAP_SERVICE_DEFINE。

**参阅（See Also）**：另请参见（See Also）：COAP_SERVICE_FLAGS。

<a id="gab4d154d5b02235a83c7a2c681b1e22e7"></a>

### `COAP_SERVICE_FOREACH`

```c
#define COAP_SERVICE_FOREACH ( _it)
```

```c
#include <zephyr/net/coap_service.h>
```

展开值（Value）：

```c
STRUCT_SECTION_FOREACH(coap_service, _it)
```

遍历全部 CoAP 服务（Services）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_it` | 迭代器名称（Iterator Name），类型为 CoAP 服务 API（CoAP Service API）。 |

<a id="gaaca92287c495f4afb79e584c47316037"></a>

### `COAP_SERVICE_FOREACH_RESOURCE`

```c
#define COAP_SERVICE_FOREACH_RESOURCE ( _service, _it )
```

```c
#include <zephyr/net/coap_service.h>
```

展开值（Value）：

```c
for (struct coap_resource *_it = (_service)->res_begin; ({                              \
        __ASSERT(_it <= (_service)->res_end, "unexpected list end location");           \
        _it < (_service)->res_end;                                                      \
}); _it++)
```

遍历与 `_service` 关联的全部静态资源（Static Resources）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_service` | 指向 COAP 服务（Service）的指针。 |
| `_it` | 迭代器名称（Iterator Name），类型为 coap_resource。 |

**说明（Note）**：注意（Note）：此宏适用于使用 COAP_SERVICE_DEFINE 定义的 _service。

<a id="gaf01cb4d11b18272eb27be93cb1a7197b"></a>

### `COAP_SERVICE_HAS_RESOURCE`

```c
#define COAP_SERVICE_HAS_RESOURCE ( _service, _resource )
```

```c
#include <zephyr/net/coap_service.h>
```

展开值（Value）：

```c
((_service)->res_begin <= _resource && _resource < (_service)->res_end)
```

检查服务是否具有指定资源（Resource）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_service` | 指向服务（Service）的指针。 |
| `_resource` | 指向资源（Resource）的指针。 |

<a id="gade9e9a55968a5ad6b3addbb08f2ccb6f"></a>

### `COAP_SERVICE_RESOURCE_COUNT`

```c
#define COAP_SERVICE_RESOURCE_COUNT ( _service)
```

```c
#include <zephyr/net/coap_service.h>
```

展开值（Value）：

```c
((_service)->res_end - (_service)->res_begin)
```

统计 CoAP 服务的静态资源（Static Resources）数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_service` | 指向服务（Service）的指针。 |

<a id="ga1ec49f2bc2c378431c4721080a13d11d"></a>

### `COAPS_SERVICE_DEFINE`

```c
#define COAPS_SERVICE_DEFINE ( _name, _host, _port, _flags, _sec_tag_list, _sec_tag_list_size )
```

```c
#include <zephyr/net/coap_service.h>
```

展开值（Value）：

```c
BUILD_ASSERT(IS_ENABLED(CONFIG_NET_SOCKETS_ENABLE_DTLS),                                   \
             "DTLS is required for CoAP secure (CONFIG_NET_SOCKETS_ENABLE_DTLS)");         \
extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[];       \
extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[];         \
__z_coap_service_define(_name, _host, _port, _flags,                                       \
                        &_CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[0],         \
                        &_CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[0],           \
                        _sec_tag_list, _sec_tag_list_size, false, NULL)
```

定义具有静态资源的安全 CoAP 服务（Secure Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` _name` | 服务名称（Service Name）。 |
| ` _host` | 与服务关联的 IP 地址或主机名（Hostname）。 |
| `[in,out] _port` | 指向与服务关联的端口的指针。 |
| ` _flags` | 配置标志（Configuration Flags）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_sec_tag_list` | 用于建立 COAPS 套接字的 DTLS 安全标签列表（Security Tag List）。 |
| `_sec_tag_list_size` | 用于建立 COAPS 套接字的 DTLS 安全标签列表大小（Security Tag List Size）。 |

**说明（Note）**：注意（Note）：_host 参数可以为 NULL。非 NULL 时，它用于指定 IPv4 或 IPv6 格式的 IP 地址、完全限定主机名（Fully-qualified Hostname）或虚拟主机（Virtual Host）；为 NULL 时使用任意地址（Any Address）。_port 参数必须非 NULL，指向存放服务所用端口号的位置。如果指定端口号为 0，将使用临时端口号（Ephemeral Port Number），并将实际分配的端口号写回该内存。使用临时端口号时，_port 指向的内存必须可写。必须启用 CONFIG_NET_SOCKETS_ENABLE_DTLS 才能支持安全 CoAP。

**参阅（See Also）**：另请参见（See Also）：COAP_SERVICE_FLAGS。

<a id="gafbc0c4c98d1cefe0a77b4ffb28cefe88"></a>

### `COAPS_SERVICE_DEFINE_OSCORE`

```c
#define COAPS_SERVICE_DEFINE_OSCORE ( _name, _host, _port, _flags, _sec_tag_list, _sec_tag_list_size, _oscore_required )
```

```c
#include <zephyr/net/coap_service.h>
```

展开值（Value）：

```c
BUILD_ASSERT(IS_ENABLED(CONFIG_NET_SOCKETS_ENABLE_DTLS),                                   \
             "DTLS is required for CoAP secure (CONFIG_NET_SOCKETS_ENABLE_DTLS)");         \
extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[];       \
extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[];         \
__z_coap_oscore_cache_define(_name)                                                        \
        __z_coap_service_define(_name, _host, _port, _flags,                               \
                                &_CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[0], \
                                &_CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[0],   \
                                _sec_tag_list, _sec_tag_list_size,                         \
                                (_oscore_required), __z_coap_oscore_cache_ptr(_name))
```

定义启用 OSCORE、且具有静态资源的安全 CoAP 服务，采用数据报传输层安全（DTLS）。

将 COAPS_SERVICE_DEFINE 与 COAP_SERVICE_DEFINE_OSCORE 中描述的 OSCORE 支持结合。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` _name` | 服务名称（Service Name）。 |
| ` _host` | 与服务关联的 IP 地址或主机名（Hostname）。 |
| `[in,out] _port` | 指向与服务关联的端口的指针。 |
| ` _flags` | 配置标志（Configuration Flags）。 |

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_sec_tag_list` | 用于建立 COAPS 套接字的 DTLS 安全标签列表（Security Tag List）。 |
| `_sec_tag_list_size` | 用于建立 COAPS 套接字的 DTLS 安全标签列表大小（Security Tag List Size）。 |
| `_oscore_required` | 为 true 时，不使用 OSCORE 的请求会被拒绝，返回 4.01 Unauthorized（未授权）。 |

**参阅（See Also）**：另请参见（See Also）：COAP_SERVICE_FLAGS。

<a id="gaa25bfeb07a50674f054b5b56005ac021"></a>

### `coap_resource_parse_observe()`

```c
int coap_resource_parse_observe ( struct coap_resource * resource, const struct coap_packet * request, const struct net_sockaddr * addr )
```

```c
#include <zephyr/net/coap_service.h>
```

为所给资源解析 CoAP 观察请求（Observe Request）。

observe 选项值为 0 时，添加观察者（Observer）；值为 1 时，移除已有观察者。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `resource` | 指向 CoAP 资源（Resource）的指针。 |
| `request` | 要解析的 CoAP 请求（Request）。 |
| `addr` | 对端地址（Peer Address）。 |

**说明（Note）**：注意（Note）：此函数适用于使用 COAP_RESOURCE_DEFINE 定义的资源。

返回（Returns）：成功时为 observe 选项值，出错时为负值。

<a id="ga7329c8a02caa7a0d9becb669932895ca"></a>

### `coap_resource_remove_observer_by_addr()`

```c
int coap_resource_remove_observer_by_addr ( struct coap_resource * resource, const struct net_sockaddr * addr )
```

```c
#include <zephyr/net/coap_service.h>
```

按地址查找观察者（Observer），并将其从资源中移除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `resource` | 指向 CoAP 资源（Resource）的指针。 |
| `addr` | 对端地址（Peer Address）。 |

**说明（Note）**：注意（Note）：此函数适用于使用 COAP_RESOURCE_DEFINE 定义的资源。

返回（Returns）：成功时为 0，出错时为负值。

<a id="gad575a7209a56874002c540eb3f8c0733"></a>

### `coap_resource_remove_observer_by_token()`

```c
int coap_resource_remove_observer_by_token ( struct coap_resource * resource, const uint8_t * token, uint8_t token_len )
```

```c
#include <zephyr/net/coap_service.h>
```

按令牌（Token）查找观察者（Observer），并将其从资源中移除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `resource` | 指向 CoAP 资源（Resource）的指针。 |
| `token` | 指向令牌（Token）的指针。 |
| `token_len` | 令牌（Token）中有效字节的长度。 |

**说明（Note）**：注意（Note）：此函数适用于使用 COAP_RESOURCE_DEFINE 定义的资源。

返回（Returns）：成功时为 0，出错时为负值。

<a id="ga40a0a599471f7f283b455809d4cf7587"></a>

### `coap_resource_send()`

```c
int coap_resource_send ( const struct coap_resource * resource, const struct coap_packet * cpkt, const struct net_sockaddr * addr, net_socklen_t addr_len, const struct coap_transmission_parameters * params )
```

```c
#include <zephyr/net/coap_service.h>
```

从所给资源（Resource）发送 CoAP 消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `resource` | 指向 CoAP 资源（Resource）的指针。 |
| `cpkt` | 要发送的 CoAP 数据包（Packet）。 |
| `addr` | 对端地址（Peer Address）。 |
| `addr_len` | 对端地址长度（Peer Address Length）。 |
| `params` | 指向传输参数结构体（Transmission Parameters Structure）的指针；使用默认值时传入 NULL。 |

**说明（Note）**：注意（Note）：此函数适用于使用 COAP_RESOURCE_DEFINE 定义的资源。

返回（Returns）：成功时为 0，出错时为负值。

<a id="ga08638f2001ca2f807489c12ff426784c"></a>

### `coap_service_is_running()`

```c
int coap_service_is_running ( const struct coap_service * service)
```

```c
#include <zephyr/net/coap_service.h>
```

查询所给服务的运行状态（Running State）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `service` | 指向 CoAP 服务（Service）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `1` | 服务正在运行（Running）时。 |
| `0` | 服务已停止（Stopped）时。 |
| `<0` | 发生错误时为负值。 |

**说明（Note）**：注意（Note）：此函数适用于使用 COAP_SERVICE_DEFINE 定义的服务。

<a id="ga19a7a0e3aa5b56ef5cd6c0ce8f142147"></a>

### `coap_service_send()`

```c
int coap_service_send ( const struct coap_service * service, const struct coap_packet * cpkt, const struct net_sockaddr * addr, net_socklen_t addr_len, const struct coap_transmission_parameters * params )
```

```c
#include <zephyr/net/coap_service.h>
```

从所给服务（Service）发送 CoAP 消息。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `service` | 指向 CoAP 服务（Service）的指针。 |
| `cpkt` | 要发送的 CoAP 数据包（Packet）。 |
| `addr` | 对端地址（Peer Address）。 |
| `addr_len` | 对端地址长度（Peer Address Length）。 |
| `params` | 指向传输参数结构体（Transmission Parameters Structure）的指针；使用默认值时传入 NULL。 |

**说明（Note）**：注意（Note）：此函数适用于使用 COAP_SERVICE_DEFINE 定义的服务。

返回（Returns）：成功时为 0，出错时为负值。

<a id="gad1e64f8fe2c6ae32730a9a61f8351bab"></a>

### `coap_service_start()`

```c
int coap_service_start ( const struct coap_service * service)
```

```c
#include <zephyr/net/coap_service.h>
```

启动所给服务（Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `service` | 指向 CoAP 服务（Service）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EALREADY` | 服务已经在运行（Already Running）时。 |
| `-ENOTSUP` | 服务器没有有效的主机和端口配置（Host and Port Configuration）时。 |

**说明（Note）**：注意（Note）：此函数适用于使用 COAP_SERVICE_DEFINE 定义的服务。

<a id="ga58bc31fc4d53ebce9c18ccbc5aab72ce"></a>

### `coap_service_stop()`

```c
int coap_service_stop ( const struct coap_service * service)
```

```c
#include <zephyr/net/coap_service.h>
```

停止所给服务（Service）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `service` | 指向 CoAP 服务（Service）的指针。 |

**返回值（Return Values）**

| 名称／方向 | 说明 |
| --- | --- |
| `0` | 成功时。 |
| `-EALREADY` | 服务未运行（Not Running）时。 |

**说明（Note）**：注意（Note）：此函数适用于使用 COAP_SERVICE_DEFINE 定义的服务。


## 8.5\_原页交叉引用（Cross References）

- [coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)
- [coap_resource](../network_application_model_reference/P016_coap_resource_结构体.md)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [BIT](../util_reference/P001_通用工具公共接口.md#ga3a8ea58898cb58fc96013383d39f482c)
- [zephyr/net/coap_service.h](../api_file_host_video_reference/P002_zephyr__net__coap_service.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE_ALTERNATE](../iterable_reference/P001_可遍历段公共接口.md#gae08ef16db3e04967fdca69a19ca4c70b)
- [gpio_dt_spec](../hardware/P267_GPIO设备树描述.md)
- [GPIO_DT_SPEC_GET](../hardware/P266_GPIO公共接口.md#ga2fa6bb5880f46984f9fc29c70f7d503e)
- [DT_ALIAS](../dt_identity_reference/P001_设备树节点标识宏.md#gaa49e19bbc39dc0d6f16b78a5d02482c9)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [coap_packet_get_payload](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga28ccf00fb1f5f13f747e61c2e3008b5c)
- [COAP_RESPONSE_CODE_BAD_REQUEST](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5)
- [gpio_pin_set_dt](../hardware/P266_GPIO公共接口.md#ga541064fb9e575c0c559c101754466fa8)
- [COAP_RESPONSE_CODE_INTERNAL_ERROR](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499)
- [COAP_RESPONSE_CODE_CHANGED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3)
- [STRUCT_SECTION_FOREACH_ALTERNATE](../iterable_reference/P001_可遍历段公共接口.md#ga06fb73cfb2dd5036a6e0f7098105ccd4)
- [STRUCT_SECTION_COUNT](../iterable_reference/P001_可遍历段公共接口.md#ga5f3ecbd953df825cadb2d08f55bc505c)
- [RFC 8613](https://datatracker.ietf.org/doc/html/rfc8613)
- [CONFIG_COAP_OSCORE](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_COAP_OSCORE)
- [STRUCT_SECTION_FOREACH](../iterable_reference/P001_可遍历段公共接口.md#gad723296f2650c25dd278e8586bfaf0ab)
- [CoAP 服务 API](P008_CoAP 服务 API.md)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)
- [CONFIG_NET_SOCKETS_ENABLE_DTLS](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_NET_SOCKETS_ENABLE_DTLS)

<a id="COAP_SERVICE_FLAGS"></a>
<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_gae08ef16db3e04967fdca69a19ca4c70b"></a>
<a id="astructcoap__resource_html"></a>
<a id="agroup__coap__service_html_gaef40d300170926ad131d06ce62c63d6a"></a>
<a id="agroup__coap_html_ga28ccf00fb1f5f13f747e61c2e3008b5c"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a07b00dba944e55c4dcde798da667b499"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a3ffb3632c37c22cee901760753c8d0d3"></a>
<a id="agroup__coap_html_gga1ea81a365834e96f43ab7be573069d26a603e60d2314bde36adf505f446c907c5"></a>
<a id="agroup__devicetree-generic-id_html_gaa49e19bbc39dc0d6f16b78a5d02482c9"></a>
<a id="agroup__gpio__interface_html_ga2fa6bb5880f46984f9fc29c70f7d503e"></a>
<a id="agroup__gpio__interface_html_ga541064fb9e575c0c559c101754466fa8"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructcoap__packet_html"></a>
<a id="astructgpio__dt__spec_html"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="agroup__iterable__section__apis_html_ga06fb73cfb2dd5036a6e0f7098105ccd4"></a>
<a id="agroup__iterable__section__apis_html_ga5f3ecbd953df825cadb2d08f55bc505c"></a>
<a id="agroup__iterable__section__apis_html_gad723296f2650c25dd278e8586bfaf0ab"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P007_CoAP TCP客户端（Client）的API。.md) · [返回大纲](大纲.md) · [下一章](P009_NXP i.MX952 时钟源（Clock Sources）.md)
