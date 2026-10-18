---
id: learning.zephyr-docs.api-memory-network-topic-reference.page-12
title: HTTP服务（Service）API。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第12章\_HTTP服务（Service）API。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

<a id="details"></a>

自Zephyr 3.4起提供（Since）；API版本（Version）为0.1.0。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 12.1\_数据结构（Data Structures）

<a id="r_http_5Fresource_5Fdesc"></a>

```c
struct http_resource_desc
```

相关声明：[http_resource_desc](../network_application_model_reference/P037_http_resource_desc_结构体.md)。

HTTP资源描述（Resource Description）。

<a id="r_http_5Fservice_5Fh3_5Fconfig"></a>

```c
struct http_service_h3_config
```

相关声明：[http_service_h3_config](../network_application_model_reference/P046_http_service_h3_config_结构体.md)。

服务的HTTP/3配置。

<a id="r_http_5Fservice_5Fconfig"></a>

```c
struct http_service_config
```

相关声明：[http_service_config](../network_application_model_reference/P045_http_service_config_结构体.md)。

HTTP服务配置（Service Configuration）。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 12.2\_宏定义（Macros）

<a id="r_gab177436ac7a8d6589dcfbd416ffd9200"></a>

```c
#define HTTP_RESOURCE_DEFINE(_name, _service, _resource, _detail)
```

相关声明：[HTTP_RESOURCE_DEFINE](#gab177436ac7a8d6589dcfbd416ffd9200)。

定义静态 HTTP 资源（Static HTTP Resource）。

<a id="r_ga8fdbc5b9c3342c7b8fd258e2184cf0ae"></a>

```c
#define HTTP_SERVICE_DEFINE_EMPTY(_name, _host, _port, _concurrent, _backlog, _detail, _res_fallback, _config)
```

相关声明：[HTTP_SERVICE_DEFINE_EMPTY](#ga8fdbc5b9c3342c7b8fd258e2184cf0ae)。

定义不含静态资源（Static Resources）的 HTTP 服务。

<a id="r_gac8cf3b383a4482c511165eaad3c1d05f"></a>

```c
#define HTTPS_SERVICE_DEFINE_EMPTY(_name, _host, _port, _concurrent, _backlog, _detail, _res_fallback, _config, _sec_tag_list, _sec_tag_list_size)
```

相关声明：[HTTPS_SERVICE_DEFINE_EMPTY](#gac8cf3b383a4482c511165eaad3c1d05f)。

定义不含静态资源（Static Resources）的 HTTPS 服务。

<a id="r_ga24ace8d5ad9ffb68e9a746c7b483b720"></a>

```c
#define HTTP_SERVICE_DEFINE(_name, _host, _port, _concurrent, _backlog, _detail, _res_fallback, _config)
```

相关声明：[HTTP_SERVICE_DEFINE](#ga24ace8d5ad9ffb68e9a746c7b483b720)。

定义包含静态资源（Static Resources）的 HTTP 服务。

<a id="r_ga8b6eabec04ca31871581c382c7246765"></a>

```c
#define HTTPS_SERVICE_DEFINE(_name, _host, _port, _concurrent, _backlog, _detail, _res_fallback, _config, _sec_tag_list, _sec_tag_list_size)
```

相关声明：[HTTPS_SERVICE_DEFINE](#ga8b6eabec04ca31871581c382c7246765)。

定义包含静态资源（Static Resources）的 HTTPS 服务。

<a id="r_ga09fa08b24156d4a9540dbb525986d8cb"></a>

```c
#define HTTP_SERVICE_COUNT(_dst)
```

相关声明：[HTTP_SERVICE_COUNT](#ga09fa08b24156d4a9540dbb525986d8cb)。

统计 HTTP 服务（Services）数量。

<a id="r_gacadf010a47812c29313c914492774921"></a>

```c
#define HTTP_SERVICE_RESOURCE_COUNT(_service)
```

相关声明：[HTTP_SERVICE_RESOURCE_COUNT](#gacadf010a47812c29313c914492774921)。

统计 HTTP 服务的静态资源（Static Resources）数量。

<a id="r_ga6144750de0b60baa3ae9c195a06622e7"></a>

```c
#define HTTP_SERVICE_FOREACH(_it)
```

相关声明：[HTTP_SERVICE_FOREACH](#ga6144750de0b60baa3ae9c195a06622e7)。

遍历全部 HTTP 服务（Services）。

<a id="r_ga450271e3a0a7098d5942539e1482605f"></a>

```c
#define HTTP_RESOURCE_FOREACH(_service, _it)
```

相关声明：[HTTP_RESOURCE_FOREACH](#ga450271e3a0a7098d5942539e1482605f)。

遍历与给定 `_service` 关联的静态 HTTP 资源（Static HTTP Resources）。

<a id="r_ga97f21c80270bb79f32cf4d891e6c3eba"></a>

```c
#define HTTP_SERVICE_FOREACH_RESOURCE(_service, _it)
```

相关声明：[HTTP_SERVICE_FOREACH_RESOURCE](#ga97f21c80270bb79f32cf4d891e6c3eba)。

遍历与 `_service` 关联的全部静态资源（Static Resources）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 12.3\_类型定义（Typedefs）

<a id="r_ga8b3eccd068dab84f64be2a267f7ed72c"></a>

```c
typedef int(* http_socket_create_fn) (const struct http_service_desc *svc, int af, int proto)
```

相关声明：[http_socket_create_fn](#ga8b3eccd068dab84f64be2a267f7ed72c)。

自定义套接字创建函数类型（Custom Socket Creation Function Type）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 12.4\_枚举（Enumerations）

<a id="r_gac26366c7dab24a62bd68e9e115d56db6"></a>

```c
enum http_version { HTTP_VERSION_ANY = 0 , HTTP_VERSION_1 = 0x01 , HTTP_VERSION_2 = 0x02 , HTTP_VERSION_3 = 0x04 }
```

相关声明：[http_version](#gac26366c7dab24a62bd68e9e115d56db6)、[HTTP_VERSION_ANY](#ggac26366c7dab24a62bd68e9e115d56db6aa3f71bed9af8bc825a228573d6592e8b)、[HTTP_VERSION_1](#ggac26366c7dab24a62bd68e9e115d56db6a26c2c997aa2de579b51064882b7f78a6)、[HTTP_VERSION_2](#ggac26366c7dab24a62bd68e9e115d56db6a2240d6f65d5af421be670655fed8b202)、[HTTP_VERSION_3](#ggac26366c7dab24a62bd68e9e115d56db6a907296c738aa0848b48cc07b0b776751)。

此服务支持的 HTTP 版本（Version）。

<a id="r_ga6fa1d08ae3794379a09455530114e3bd"></a>

```c
enum http_h3_alt_svc_policy { HTTP_H3_ALT_SVC_DEFAULT = 0 , HTTP_H3_ALT_SVC_DISABLE , HTTP_H3_ALT_SVC_ENABLE }
```

相关声明：[http_h3_alt_svc_policy](#ga6fa1d08ae3794379a09455530114e3bd)、[HTTP_H3_ALT_SVC_DEFAULT](#gga6fa1d08ae3794379a09455530114e3bdaf2d427f7461f1441acaaade10eede5b2)、[HTTP_H3_ALT_SVC_DISABLE](#gga6fa1d08ae3794379a09455530114e3bda90f916bd5f4d2c746ed68b505b6aca1e)、[HTTP_H3_ALT_SVC_ENABLE](#gga6fa1d08ae3794379a09455530114e3bda3865c947ce80ba6ea065702cdba6a707)。

此服务的 HTTP/3 Alt-Svc 通告策略（Advertisement Policy）。

## 12.5\_详细说明（Detailed Documentation）

<a id="gab177436ac7a8d6589dcfbd416ffd9200"></a>

### `HTTP_RESOURCE_DEFINE`

```c
#define HTTP_RESOURCE_DEFINE ( _name, _service, _resource, _detail )
```

```c
#include <zephyr/net/http/service.h>
```

展开值（Value）：

```c
const STRUCT_SECTION_ITERABLE_ALTERNATE(http_resource_desc_##_service, http_resource_desc, \
                                        _name) = {                                         \
        .resource = _resource,                                                             \
        .detail = (void *)(_detail),                                                       \
}
```

定义静态 HTTP 资源（Static HTTP Resource）。

静态 HTTP 资源（Static HTTP Resource）在系统初始化之前就已知。动态资源（Dynamic Resources）可在系统初始化时发现，也可在运行时由系统内部或外部事件插入或移除。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_name` | 资源名称（Resource Name）。 |
| `_service` | 关联服务名称（Associated Service Name）。 |
| `_resource` | 标识资源的类路径字符串（Pathname-like String）。 |
| `_detail` | 与资源关联的实现专有详情（Implementation-specific Detail）。 |

**说明（Note）**：注意（Note）：_resource 是去掉协议、主机和 URL 参数后的 URL。例如 http://www.foo.com/bar/baz.html#param1=value1 的资源为 /bar/baz.html，通常称为 URL 的路径（Path）。每个 (service, resource) 配对必须唯一，_resource 必须非 NULL。

<a id="ga450271e3a0a7098d5942539e1482605f"></a>

### `HTTP_RESOURCE_FOREACH`

```c
#define HTTP_RESOURCE_FOREACH ( _service, _it )
```

```c
#include <zephyr/net/http/service.h>
```

展开值（Value）：

```c
STRUCT_SECTION_FOREACH_ALTERNATE(http_resource_desc_##_service, http_resource_desc, _it)
```

遍历与给定 `_service` 关联的静态 HTTP 资源（Static HTTP Resources）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_service` | HTTP 服务名称（Service Name） |
| `_it` | 迭代器名称（Iterator Name），类型为 http_resource_desc。 |

**说明（Note）**：注意（Note）：此宏要求使用 HTTP_SERVICE_DEFINE 定义 _service。

<a id="ga09fa08b24156d4a9540dbb525986d8cb"></a>

### `HTTP_SERVICE_COUNT`

```c
#define HTTP_SERVICE_COUNT ( _dst)
```

```c
#include <zephyr/net/http/service.h>
```

展开值（Value）：

```c
STRUCT_SECTION_COUNT(http_service_desc, _dst)
```

统计 HTTP 服务（Services）数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `[out] _dst` | 指向用于写入结果的位置。 |

<a id="ga24ace8d5ad9ffb68e9a746c7b483b720"></a>

### `HTTP_SERVICE_DEFINE`

```c
#define HTTP_SERVICE_DEFINE ( _name, _host, _port, _concurrent, _backlog, _detail, _res_fallback, _config )
```

```c
#include <zephyr/net/http/service.h>
```

展开值（Value）：

```c
extern struct http_resource_desc _CONCAT(_http_resource_desc_##_name, _list_start)[];      \
extern struct http_resource_desc _CONCAT(_http_resource_desc_##_name, _list_end)[];        \
__z_http_service_define(_name, _host, _port, _concurrent, _backlog, _detail,               \
                        _res_fallback,                                                     \
                        &_CONCAT(_http_resource_desc_##_name, _list_start)[0],             \
                        &_CONCAT(_http_resource_desc_##_name, _list_end)[0], _config);
```

定义包含静态资源（Static Resources）的 HTTP 服务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` _name` | 服务名称（Service Name）。 |
| ` _host` | 与服务关联的 IP 地址或主机名（Hostname）。 |
| `[in,out] _port` | 指向与服务关联的端口的指针。 |
| ` _concurrent` | 最大并发客户端数量（Concurrent Clients），最大为 CONFIG_HTTP_SERVER_MAX_CLIENTS。 |
| ` _backlog` | 最大排队连接数量（Queued Connections），最小为 1。 |
| ` _detail` | 与服务关联的用户定义详情（User-defined Detail）。 |
| ` _res_fallback` | 无其他资源匹配路径时提供的回退资源（Fallback Resource）。 |
| ` _config` | 指向 http_service_config 结构体的指针，NULL 表示使用默认行为。 |

**说明（Note）**：注意（Note）：_host 指定 IPv4／IPv6 地址、完全限定主机名（Fully-qualified Hostname）或虚拟主机（Virtual Host）。为 NULL 时，监听端口在所有地址上监听。_port 必须非 NULL，指向存放此服务端口号的位置。端口号为零时使用临时端口（Ephemeral Port），并将实际分配的端口号写回内存。因此使用临时端口时，_port 指向的内存必须可写。

<a id="ga8fdbc5b9c3342c7b8fd258e2184cf0ae"></a>

### `HTTP_SERVICE_DEFINE_EMPTY`

```c
#define HTTP_SERVICE_DEFINE_EMPTY ( _name, _host, _port, _concurrent, _backlog, _detail, _res_fallback, _config )
```

```c
#include <zephyr/net/http/service.h>
```

展开值（Value）：

```c
__z_http_service_define(_name, _host, _port, _concurrent, _backlog, _detail,               \
                        _res_fallback, NULL, NULL, _config)
```

定义不含静态资源（Static Resources）的 HTTP 服务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` _name` | 服务名称（Service Name）。 |
| ` _host` | 与服务关联的 IP 地址或主机名（Hostname）。 |
| `[in,out] _port` | 指向与服务关联的端口的指针。 |
| ` _concurrent` | 最大并发客户端数量（Concurrent Clients），最大为 CONFIG_HTTP_SERVER_MAX_CLIENTS。 |
| ` _backlog` | 最大排队连接数量（Queued Connections），最小为 1。 |
| ` _detail` | 与服务关联的用户定义详情（User-defined Detail）。 |
| ` _res_fallback` | 无其他资源匹配路径时提供的回退资源（Fallback Resource）。 |
| ` _config` | 指向 http_service_config 结构体的指针，NULL 表示使用默认行为。 |

**说明（Note）**：注意（Note）：_host 指定 IPv4／IPv6 地址、完全限定主机名（Fully-qualified Hostname）或虚拟主机（Virtual Host）。为 NULL 时，监听端口在所有地址上监听。_port 必须非 NULL，指向存放此服务端口号的位置。端口号为零时使用临时端口（Ephemeral Port），并将实际分配的端口号写回内存。因此使用临时端口时，_port 指向的内存必须可写。

<a id="ga6144750de0b60baa3ae9c195a06622e7"></a>

### `HTTP_SERVICE_FOREACH`

```c
#define HTTP_SERVICE_FOREACH ( _it)
```

```c
#include <zephyr/net/http/service.h>
```

展开值（Value）：

```c
STRUCT_SECTION_FOREACH(http_service_desc, _it)
```

遍历全部 HTTP 服务（Services）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_it` | http_service_desc 迭代器名称（Iterator Name） |

<a id="ga97f21c80270bb79f32cf4d891e6c3eba"></a>

### `HTTP_SERVICE_FOREACH_RESOURCE`

```c
#define HTTP_SERVICE_FOREACH_RESOURCE ( _service, _it )
```

```c
#include <zephyr/net/http/service.h>
```

展开值（Value）：

```c
for (struct http_resource_desc *_it = (_service)->res_begin; ({                            \
             __ASSERT(_it <= (_service)->res_end, "unexpected list end location");         \
             _it < (_service)->res_end;                                                    \
     });                                                                                   \
     _it++)
```

遍历与 `_service` 关联的全部静态资源（Static Resources）。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_service` | 指向 HTTP 服务（Service）的指针 |
| `_it` | 迭代器名称（Iterator Name），类型为 http_resource_desc。 |

**说明（Note）**：注意（Note）：此宏适用于由 HTTP_SERVICE_DEFINE 或 HTTP_SERVICE_DEFINE_EMPTY 定义的 _service。

<a id="gacadf010a47812c29313c914492774921"></a>

### `HTTP_SERVICE_RESOURCE_COUNT`

```c
#define HTTP_SERVICE_RESOURCE_COUNT ( _service)
```

```c
#include <zephyr/net/http/service.h>
```

展开值（Value）：

```c
((_service)->res_end - (_service)->res_begin)
```

统计 HTTP 服务的静态资源（Static Resources）数量。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `_service` | 指向服务（Service）的指针。 |

<a id="ga8b6eabec04ca31871581c382c7246765"></a>

### `HTTPS_SERVICE_DEFINE`

```c
#define HTTPS_SERVICE_DEFINE ( _name, _host, _port, _concurrent, _backlog, _detail, _res_fallback, _config, _sec_tag_list, _sec_tag_list_size )
```

```c
#include <zephyr/net/http/service.h>
```

展开值（Value）：

```c
extern struct http_resource_desc _CONCAT(_http_resource_desc_##_name, _list_start)[];  \
extern struct http_resource_desc _CONCAT(_http_resource_desc_##_name, _list_end)[];    \
__z_http_service_define(_name, _host, _port, _concurrent, _backlog, _detail,           \
                        _res_fallback,                                                 \
                        &_CONCAT(_http_resource_desc_##_name, _list_start)[0],         \
                        &_CONCAT(_http_resource_desc_##_name, _list_end)[0], _config,  \
                        _sec_tag_list, _sec_tag_list_size);                            \
BUILD_ASSERT(IS_ENABLED(CONFIG_NET_SOCKETS_SOCKOPT_TLS),                               \
             "TLS is required for HTTP secure (CONFIG_NET_SOCKETS_SOCKOPT_TLS)")
```

定义包含静态资源（Static Resources）的 HTTPS 服务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` _name` | 服务名称（Service Name）。 |
| ` _host` | 与服务关联的 IP 地址或主机名（Hostname）。 |
| `[in,out] _port` | 指向与服务关联的端口的指针。 |
| ` _concurrent` | 最大并发客户端数量（Concurrent Clients），最大为 CONFIG_HTTP_SERVER_MAX_CLIENTS。 |
| ` _backlog` | 最大排队连接数量（Queued Connections），最小为 1。 |
| ` _detail` | 与服务关联的用户定义详情（User-defined Detail）。 |
| ` _res_fallback` | 无其他资源匹配路径时提供的回退资源（Fallback Resource）。 |
| ` _config` | 指向 http_service_config 结构体的指针，NULL 表示使用默认行为。 |
| ` _sec_tag_list` | 用于设置 HTTPS 套接字的 TLS 安全标签列表（Security Tag List）。 |
| ` _sec_tag_list_size` | 用于设置 HTTPS 套接字的 TLS 安全标签列表大小（Security Tag List Size）。 |

**说明（Note）**：注意（Note）：_host 指定 IPv4／IPv6 地址、完全限定主机名（Fully-qualified Hostname）或虚拟主机（Virtual Host）。为 NULL 时，监听端口在所有地址上监听。_port 必须非 NULL，指向存放此服务端口号的位置。端口号为零时使用临时端口（Ephemeral Port），并将实际分配的端口号写回内存。因此使用临时端口时，_port 指向的内存必须可写。

<a id="gac8cf3b383a4482c511165eaad3c1d05f"></a>

### `HTTPS_SERVICE_DEFINE_EMPTY`

```c
#define HTTPS_SERVICE_DEFINE_EMPTY ( _name, _host, _port, _concurrent, _backlog, _detail, _res_fallback, _config, _sec_tag_list, _sec_tag_list_size )
```

```c
#include <zephyr/net/http/service.h>
```

展开值（Value）：

```c
__z_http_service_define(_name, _host, _port, _concurrent, _backlog, _detail,             \
                        _res_fallback, NULL, NULL, _config,                              \
                        _sec_tag_list, _sec_tag_list_size);                              \
BUILD_ASSERT(IS_ENABLED(CONFIG_NET_SOCKETS_SOCKOPT_TLS),                                 \
             "TLS is required for HTTP secure (CONFIG_NET_SOCKETS_SOCKOPT_TLS)")
```

定义不含静态资源（Static Resources）的 HTTPS 服务。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| ` _name` | 服务名称（Service Name）。 |
| ` _host` | 与服务关联的 IP 地址或主机名（Hostname）。 |
| `[in,out] _port` | 指向与服务关联的端口的指针。 |
| ` _concurrent` | 最大并发客户端数量（Concurrent Clients），最大为 CONFIG_HTTP_SERVER_MAX_CLIENTS。 |
| ` _backlog` | 最大排队连接数量（Queued Connections），最小为 1。 |
| ` _detail` | 与服务关联的用户定义详情（User-defined Detail）。 |
| ` _res_fallback` | 无其他资源匹配路径时提供的回退资源（Fallback Resource）。 |
| ` _config` | 指向 http_service_config 结构体的指针，NULL 表示使用默认行为。 |
| ` _sec_tag_list` | 用于设置 HTTPS 套接字的 TLS 安全标签列表（Security Tag List）。 |
| ` _sec_tag_list_size` | 用于设置 HTTPS 套接字的 TLS 安全标签列表大小（Security Tag List Size）。 |

**说明（Note）**：注意（Note）：_host 指定 IPv4／IPv6 地址、完全限定主机名（Fully-qualified Hostname）或虚拟主机（Virtual Host）。为 NULL 时，监听端口在所有地址上监听。_port 必须非 NULL，指向存放此服务端口号的位置。端口号为零时使用临时端口（Ephemeral Port），并将实际分配的端口号写回内存。因此使用临时端口时，_port 指向的内存必须可写。

<a id="ga8b3eccd068dab84f64be2a267f7ed72c"></a>

### `http_socket_create_fn`

```c
typedef int(* http_socket_create_fn) (const struct http_service_desc *svc, int af, int proto)
```

```c
#include <zephyr/net/http/service.h>
```

自定义套接字创建函数类型（Custom Socket Creation Function Type）。

允许按用户需求自定义 HTTP 服务。例如，可创建带自定义选项的套接字，或为特定服务创建其他类型的套接字。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `svc` | 正在为其创建套接字的 HTTP 服务描述（Service Description）。 |
| `af` | 待创建套接字的地址族（Address Family），例如 AF_INET 或 AF_INET6。 |
| `proto` | 待创建套接字的协议（Protocol），例如 IPPROTO_TCP。 |

**返回（Returns）**：返回值（Returns）：成功返回有效的套接字文件描述符（Socket File Descriptor），失败返回负错误码。

<a id="ga6fa1d08ae3794379a09455530114e3bd"></a>

### `http_h3_alt_svc_policy`

```c
enum http_h3_alt_svc_policy
```

```c
#include <zephyr/net/http/service.h>
```

此服务的 HTTP/3 Alt-Svc 通告策略（Advertisement Policy）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HTTP_H3_ALT_SVC_DEFAULT` | 使用 Kconfig 中配置的全局默认策略（Global Default Policy）。 |
| `HTTP_H3_ALT_SVC_DISABLE` | 此服务从不通过 Alt-Svc 通告 HTTP/3。 |
| `HTTP_H3_ALT_SVC_ENABLE` | 可用时，此服务始终通过 Alt-Svc 通告 HTTP/3。 |

<a id="gac26366c7dab24a62bd68e9e115d56db6"></a>

### `http_version`

```c
enum http_version
```

```c
#include <zephyr/net/http/service.h>
```

此服务支持的 HTTP 版本（Version）。

未设置时支持所有已配置版本。用户也可指定单一版本，使此服务只支持该版本；多个值可按位或组合，以支持多个指定版本。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HTTP_VERSION_ANY` | 支持系统中配置的任意 HTTP 版本（HTTP Version）。 |
| `HTTP_VERSION_1` | 支持 HTTP/1.0 和 HTTP/1.1。 |
| `HTTP_VERSION_2` | 支持 HTTP/2。 |
| `HTTP_VERSION_3` | 支持 HTTP/3。 |


## 12.6\_原页交叉引用（Cross References）

- [http_resource_desc](../network_application_model_reference/P037_http_resource_desc_结构体.md)
- [http_service_h3_config](../network_application_model_reference/P046_http_service_h3_config_结构体.md)
- [http_service_config](../network_application_model_reference/P045_http_service_config_结构体.md)
- [zephyr/net/http/service.h](../api_file_protocol_service_reference/P031_zephyr__net__http__service.h_文件参考.md)
- [STRUCT_SECTION_ITERABLE_ALTERNATE](../iterable_reference/P001_可遍历段公共接口.md#gae08ef16db3e04967fdca69a19ca4c70b)
- [http://www.foo.com/bar/baz.html](http://www.foo.com/bar/baz.html)
- [STRUCT_SECTION_FOREACH_ALTERNATE](../iterable_reference/P001_可遍历段公共接口.md#ga06fb73cfb2dd5036a6e0f7098105ccd4)
- [STRUCT_SECTION_COUNT](../iterable_reference/P001_可遍历段公共接口.md#ga5f3ecbd953df825cadb2d08f55bc505c)
- [STRUCT_SECTION_FOREACH](../iterable_reference/P001_可遍历段公共接口.md#gad723296f2650c25dd278e8586bfaf0ab)
- [IS_ENABLED](../util_reference/P001_通用工具公共接口.md#ga111fe4e9d63758262fc6810a782cb32a)

<a id="header-details"></a>
<a id="doc-define-members"></a>
<a id="header-doc-define-members"></a>
<a id="agroup__iterable__section__apis_html_gae08ef16db3e04967fdca69a19ca4c70b"></a>
<a id="astructhttp__resource__desc_html"></a>
<a id="agroup__iterable__section__apis_html_ga06fb73cfb2dd5036a6e0f7098105ccd4"></a>
<a id="agroup__iterable__section__apis_html_ga5f3ecbd953df825cadb2d08f55bc505c"></a>
<a id="agroup__iterable__section__apis_html_gad723296f2650c25dd278e8586bfaf0ab"></a>
<a id="agroup__sys-util_html_ga111fe4e9d63758262fc6810a782cb32a"></a>
<a id="doc-typedef-members"></a>
<a id="header-doc-typedef-members"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="gga6fa1d08ae3794379a09455530114e3bdaf2d427f7461f1441acaaade10eede5b2"></a>
<a id="gga6fa1d08ae3794379a09455530114e3bda90f916bd5f4d2c746ed68b505b6aca1e"></a>
<a id="gga6fa1d08ae3794379a09455530114e3bda3865c947ce80ba6ea065702cdba6a707"></a>
<a id="ggac26366c7dab24a62bd68e9e115d56db6aa3f71bed9af8bc825a228573d6592e8b"></a>
<a id="ggac26366c7dab24a62bd68e9e115d56db6a26c2c997aa2de579b51064882b7f78a6"></a>
<a id="ggac26366c7dab24a62bd68e9e115d56db6a2240d6f65d5af421be670655fed8b202"></a>
<a id="ggac26366c7dab24a62bd68e9e115d56db6a907296c738aa0848b48cc07b0b776751"></a>

---

[上一章](P011_以太网物理层接口（Ethernet PHY Interface）.md) · [返回大纲](大纲.md) · [下一章](P013_IEEE 802.15.4 网络管理（Net Management）.md)
