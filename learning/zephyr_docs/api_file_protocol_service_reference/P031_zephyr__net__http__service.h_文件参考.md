---
id: learning.zephyr-docs.api-file-protocol-service-reference.page-31
title: zephyr__net__http__service.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/service_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第31章\_zephyr\_\_net\_\_http\_\_service.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/service_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP服务（Service）API。

<a id="details"></a>

```c
#include <zephyr/net/http/server.h>
#include <stdint.h>
#include <stddef.h>
#include <zephyr/sys/util_macro.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/tls_credentials.h>
```

查看此文件的源码。

HTTP服务（Service）API。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 31.1\_数据结构（Data Structures）

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

## 31.2\_宏定义（Macros）

<a id="r_gab177436ac7a8d6589dcfbd416ffd9200"></a>

```c
#define HTTP_RESOURCE_DEFINE(_name, _service, _resource, _detail)
```

相关声明：[HTTP_RESOURCE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gab177436ac7a8d6589dcfbd416ffd9200)。

定义静态 HTTP 资源（Static HTTP Resource）。

<a id="r_ga8fdbc5b9c3342c7b8fd258e2184cf0ae"></a>

```c
#define HTTP_SERVICE_DEFINE_EMPTY(_name, _host, _port, _concurrent, _backlog, _detail, _res_fallback, _config)
```

相关声明：[HTTP_SERVICE_DEFINE_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8fdbc5b9c3342c7b8fd258e2184cf0ae)。

定义不含静态资源（Static Resources）的 HTTP 服务。

<a id="r_gac8cf3b383a4482c511165eaad3c1d05f"></a>

```c
#define HTTPS_SERVICE_DEFINE_EMPTY(_name, _host, _port, _concurrent, _backlog, _detail, _res_fallback, _config, _sec_tag_list, _sec_tag_list_size)
```

相关声明：[HTTPS_SERVICE_DEFINE_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gac8cf3b383a4482c511165eaad3c1d05f)。

定义不含静态资源（Static Resources）的 HTTPS 服务。

<a id="r_ga24ace8d5ad9ffb68e9a746c7b483b720"></a>

```c
#define HTTP_SERVICE_DEFINE(_name, _host, _port, _concurrent, _backlog, _detail, _res_fallback, _config)
```

相关声明：[HTTP_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga24ace8d5ad9ffb68e9a746c7b483b720)。

定义包含静态资源（Static Resources）的 HTTP 服务。

<a id="r_ga8b6eabec04ca31871581c382c7246765"></a>

```c
#define HTTPS_SERVICE_DEFINE(_name, _host, _port, _concurrent, _backlog, _detail, _res_fallback, _config, _sec_tag_list, _sec_tag_list_size)
```

相关声明：[HTTPS_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8b6eabec04ca31871581c382c7246765)。

定义包含静态资源（Static Resources）的 HTTPS 服务。

<a id="r_ga09fa08b24156d4a9540dbb525986d8cb"></a>

```c
#define HTTP_SERVICE_COUNT(_dst)
```

相关声明：[HTTP_SERVICE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga09fa08b24156d4a9540dbb525986d8cb)。

统计 HTTP 服务（Services）数量。

<a id="r_gacadf010a47812c29313c914492774921"></a>

```c
#define HTTP_SERVICE_RESOURCE_COUNT(_service)
```

相关声明：[HTTP_SERVICE_RESOURCE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gacadf010a47812c29313c914492774921)。

统计 HTTP 服务的静态资源（Static Resources）数量。

<a id="r_ga6144750de0b60baa3ae9c195a06622e7"></a>

```c
#define HTTP_SERVICE_FOREACH(_it)
```

相关声明：[HTTP_SERVICE_FOREACH](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga6144750de0b60baa3ae9c195a06622e7)。

遍历全部 HTTP 服务（Services）。

<a id="r_ga450271e3a0a7098d5942539e1482605f"></a>

```c
#define HTTP_RESOURCE_FOREACH(_service, _it)
```

相关声明：[HTTP_RESOURCE_FOREACH](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga450271e3a0a7098d5942539e1482605f)。

遍历与给定 `_service` 关联的静态 HTTP 资源（Static HTTP Resources）。

<a id="r_ga97f21c80270bb79f32cf4d891e6c3eba"></a>

```c
#define HTTP_SERVICE_FOREACH_RESOURCE(_service, _it)
```

相关声明：[HTTP_SERVICE_FOREACH_RESOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga97f21c80270bb79f32cf4d891e6c3eba)。

遍历与 `_service` 关联的全部静态资源（Static Resources）。

<a id="header-typedef-members"></a>
<a id="typedef-members"></a>

## 31.3\_类型定义（Typedefs）

<a id="r_ga8b3eccd068dab84f64be2a267f7ed72c"></a>

```c
typedef int(* http_socket_create_fn) (const struct http_service_desc *svc, int af, int proto)
```

相关声明：[http_socket_create_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8b3eccd068dab84f64be2a267f7ed72c)。

自定义套接字创建函数类型（Custom Socket Creation Function Type）。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 31.4\_枚举（Enumerations）

<a id="r_gac26366c7dab24a62bd68e9e115d56db6"></a>

```c
enum http_version { HTTP_VERSION_ANY = 0 , HTTP_VERSION_1 = 0x01 , HTTP_VERSION_2 = 0x02 , HTTP_VERSION_3 = 0x04 }
```

相关声明：[http_version](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gac26366c7dab24a62bd68e9e115d56db6)、[HTTP_VERSION_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ggac26366c7dab24a62bd68e9e115d56db6aa3f71bed9af8bc825a228573d6592e8b)、[HTTP_VERSION_1](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ggac26366c7dab24a62bd68e9e115d56db6a26c2c997aa2de579b51064882b7f78a6)、[HTTP_VERSION_2](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ggac26366c7dab24a62bd68e9e115d56db6a2240d6f65d5af421be670655fed8b202)、[HTTP_VERSION_3](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ggac26366c7dab24a62bd68e9e115d56db6a907296c738aa0848b48cc07b0b776751)。

此服务支持的 HTTP 版本（Version）。

<a id="r_ga6fa1d08ae3794379a09455530114e3bd"></a>

```c
enum http_h3_alt_svc_policy { HTTP_H3_ALT_SVC_DEFAULT = 0 , HTTP_H3_ALT_SVC_DISABLE , HTTP_H3_ALT_SVC_ENABLE }
```

相关声明：[http_h3_alt_svc_policy](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga6fa1d08ae3794379a09455530114e3bd)、[HTTP_H3_ALT_SVC_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gga6fa1d08ae3794379a09455530114e3bdaf2d427f7461f1441acaaade10eede5b2)、[HTTP_H3_ALT_SVC_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gga6fa1d08ae3794379a09455530114e3bda90f916bd5f4d2c746ed68b505b6aca1e)、[HTTP_H3_ALT_SVC_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gga6fa1d08ae3794379a09455530114e3bda3865c947ce80ba6ea065702cdba6a707)。

此服务的 HTTP/3 Alt-Svc 通告策略（Advertisement Policy）。


## 31.5\_原页交叉引用（Cross References）

- [zephyr/net/http/server.h](../api_source_configuration_reference/P030_server.h_源码浏览.md)
- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/sys/util_macro.h](../util_reference/P005_宏工具头文件源码.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P003_可遍历段辅助头文件源码.md)
- [zephyr/net/tls_credentials.h](../api_source_reference/P870_tls_credentials.h_源码浏览.md)
- [查看此文件的源码。](../api_source_configuration_reference/P099_service.h_源码浏览.md)
- [http_resource_desc](../network_application_model_reference/P037_http_resource_desc_结构体.md)
- [http_service_h3_config](../network_application_model_reference/P046_http_service_h3_config_结构体.md)
- [http_service_config](../network_application_model_reference/P045_http_service_config_结构体.md)
- [HTTP_RESOURCE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gab177436ac7a8d6589dcfbd416ffd9200)
- [HTTP_SERVICE_DEFINE_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8fdbc5b9c3342c7b8fd258e2184cf0ae)
- [HTTPS_SERVICE_DEFINE_EMPTY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gac8cf3b383a4482c511165eaad3c1d05f)
- [HTTP_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga24ace8d5ad9ffb68e9a746c7b483b720)
- [HTTPS_SERVICE_DEFINE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8b6eabec04ca31871581c382c7246765)
- [HTTP_SERVICE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga09fa08b24156d4a9540dbb525986d8cb)
- [HTTP_SERVICE_RESOURCE_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gacadf010a47812c29313c914492774921)
- [HTTP_SERVICE_FOREACH](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga6144750de0b60baa3ae9c195a06622e7)
- [HTTP_RESOURCE_FOREACH](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga450271e3a0a7098d5942539e1482605f)
- [HTTP_SERVICE_FOREACH_RESOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga97f21c80270bb79f32cf4d891e6c3eba)
- [http_socket_create_fn](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga8b3eccd068dab84f64be2a267f7ed72c)
- [http_version](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gac26366c7dab24a62bd68e9e115d56db6)
- [HTTP_VERSION_ANY](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ggac26366c7dab24a62bd68e9e115d56db6aa3f71bed9af8bc825a228573d6592e8b)
- [HTTP_VERSION_1](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ggac26366c7dab24a62bd68e9e115d56db6a26c2c997aa2de579b51064882b7f78a6)
- [HTTP_VERSION_2](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ggac26366c7dab24a62bd68e9e115d56db6a2240d6f65d5af421be670655fed8b202)
- [HTTP_VERSION_3](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ggac26366c7dab24a62bd68e9e115d56db6a907296c738aa0848b48cc07b0b776751)
- [http_h3_alt_svc_policy](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#ga6fa1d08ae3794379a09455530114e3bd)
- [HTTP_H3_ALT_SVC_DEFAULT](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gga6fa1d08ae3794379a09455530114e3bdaf2d427f7461f1441acaaade10eede5b2)
- [HTTP_H3_ALT_SVC_DISABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gga6fa1d08ae3794379a09455530114e3bda90f916bd5f4d2c746ed68b505b6aca1e)
- [HTTP_H3_ALT_SVC_ENABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__service.html#gga6fa1d08ae3794379a09455530114e3bda3865c947ce80ba6ea065702cdba6a707)

<a id="header-details"></a>

---

[上一章](P030_zephyr__drivers__interrupt_controller__sam0_eic.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P032_zephyr__dt-bindings__clock__stm32_common_clocks.h_文件参考.md)
