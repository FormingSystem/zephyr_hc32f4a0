---
id: learning.zephyr-docs.api-source-configuration-reference.page-99
title: service.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/service_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第99章\_service.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/service_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/service_8h.html)。

## 99.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="foldopen00059"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00095"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="foldopen00103"></a>
<a id="l00103"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="foldopen00113"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00117"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00129"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00163"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00190"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00197"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00308"></a>
<a id="l00309"></a>
<a id="l00310"></a>
<a id="l00311"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00317"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="foldopen00349"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="foldopen00361"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00375"></a>
<a id="l00376"></a>
<a id="agroup__http__service_html_ga6fa1d08ae3794379a09455530114e3bd"></a>
<a id="agroup__http__service_html_ga8b3eccd068dab84f64be2a267f7ed72c"></a>
<a id="agroup__http__service_html_gac26366c7dab24a62bd68e9e115d56db6"></a>
<a id="agroup__http__service_html_gga6fa1d08ae3794379a09455530114e3bda3865c947ce80ba6ea065702cdba6a707"></a>
<a id="agroup__http__service_html_gga6fa1d08ae3794379a09455530114e3bda90f916bd5f4d2c746ed68b505b6aca1e"></a>
<a id="agroup__http__service_html_gga6fa1d08ae3794379a09455530114e3bdaf2d427f7461f1441acaaade10eede5b2"></a>
<a id="agroup__http__service_html_ggac26366c7dab24a62bd68e9e115d56db6a2240d6f65d5af421be670655fed8b202"></a>
<a id="agroup__http__service_html_ggac26366c7dab24a62bd68e9e115d56db6a26c2c997aa2de579b51064882b7f78a6"></a>
<a id="agroup__http__service_html_ggac26366c7dab24a62bd68e9e115d56db6a907296c738aa0848b48cc07b0b776751"></a>
<a id="agroup__http__service_html_ggac26366c7dab24a62bd68e9e115d56db6aa3f71bed9af8bc825a228573d6592e8b"></a>
<a id="agroup__tls__credentials_html_gaadfe9694309e473f7be74ed98dfb36d3"></a>
<a id="ahttp_2server_8h_html"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructhttp__resource__desc_html"></a>
<a id="astructhttp__resource__desc_html_a2882314e271a09d6bc9fae3f58558605"></a>
<a id="astructhttp__resource__desc_html_afdf3332dbc4fb8c10ec8bc525cd8d498"></a>
<a id="astructhttp__resource__detail_html"></a>
<a id="astructhttp__service__config_html"></a>
<a id="astructhttp__service__config_html_a4738a850d59dc1a6db82bd12174506ec"></a>
<a id="astructhttp__service__config_html_a7a3b7aa9e222cb816d7330c2c2be127f"></a>
<a id="astructhttp__service__config_html_aa4c887036b350e7fc92799cefd0b0141"></a>
<a id="astructhttp__service__h3__config_html"></a>
<a id="astructhttp__service__h3__config_html_a0be4af47f80b4734f43fbc04fd86163c"></a>
<a id="astructhttp__service__h3__config_html_a0ffd5ab6f7804fb4dbd8cca2da6fda0a"></a>
<a id="astructhttp__service__h3__config_html_afec0c9db1dd92540d988317a6d491075"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="atls__credentials_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 * Copyright (c) 2022 Meta
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_HTTP_SERVICE_H_
#define ZEPHYR_INCLUDE_NET_HTTP_SERVICE_H_


#include <zephyr/net/http/server.h>
#include <stdint.h>
#include <stddef.h>

#include <zephyr/sys/util_macro.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/tls_credentials.h>

#ifdef __cplusplus
extern "C" {
#endif

struct http_resource_desc {
        const char *resource;
        void *detail;
};

#define HTTP_RESOURCE_DEFINE(_name, _service, _resource, _detail)                                  \
        const STRUCT_SECTION_ITERABLE_ALTERNATE(http_resource_desc_##_service, http_resource_desc, \
                                                _name) = {                                         \
                .resource = _resource,                                                             \
                .detail = (void *)(_detail),                                                       \
        }


struct http_service_runtime_data {
        int num_clients;
};

struct http_service_desc;


typedef int (*http_socket_create_fn)(const struct http_service_desc *svc, int af, int proto);

enum http_version {
        HTTP_VERSION_ANY = 0,
        HTTP_VERSION_1 = 0x01,
        HTTP_VERSION_2 = 0x02,
        HTTP_VERSION_3 = 0x04,
};

enum http_h3_alt_svc_policy {
        HTTP_H3_ALT_SVC_DEFAULT = 0,
        HTTP_H3_ALT_SVC_DISABLE,
        HTTP_H3_ALT_SVC_ENABLE,
};

struct http_service_h3_config {
        enum http_h3_alt_svc_policy alt_svc_policy;
        bool enable_session_tickets;
        uint32_t max_early_data_size;
};

struct http_service_config {
        http_socket_create_fn socket_create;
        enum http_version http_ver;
        struct http_service_h3_config h3;

        /* If any more service-specific configuration is needed, it can be added here. */
};


struct http_service_desc {
        const char *host;
        uint16_t *port;
        int *fd;
        /* QUIC listening connection socket for HTTP/3. It is used to accept
         * new connections for this service.
         * Set to NULL if HTTP/3 is not supported, and set to -1 if HTTP/3 is
         * not yet initialized or enabled for this service. If HTTP/3 is supported then
         * this pointer cannot be null.
         */
        int *fd_h3;
        void *detail;
        size_t concurrent;
        size_t backlog;
        struct http_service_runtime_data *data;
        struct http_resource_desc *res_begin;
        struct http_resource_desc *res_end;
        struct http_resource_detail *res_fallback;
        const struct http_service_config *config;
#if defined(CONFIG_NET_SOCKETS_SOCKOPT_TLS)
        const sec_tag_t *sec_tag_list;
        size_t sec_tag_list_size;
#endif
};

#define __z_http_service_define(_name, _host, _port, _concurrent, _backlog, _detail,               \
                                _res_fallback, _res_begin, _res_end, _config, ...)                 \
        BUILD_ASSERT(_concurrent <= CONFIG_HTTP_SERVER_MAX_CLIENTS,                                \
                     "can't accept more then MAX_CLIENTS");                                        \
        BUILD_ASSERT(_backlog > 0, "backlog can't be 0");                                          \
        static int _name##_fd = -1;                                                                \
        IF_ENABLED(CONFIG_HTTP_SERVER_VERSION_3, (static int _name##_fd_h3 = -1;))                 \
        static struct http_service_runtime_data _name##_data = {0};                                \
        const STRUCT_SECTION_ITERABLE(http_service_desc, _name) = {                                \
                .host = _host,                                                                     \
                .port = (uint16_t *)(_port),                                                       \
                .fd = &_name##_fd,                                                                 \
                IF_ENABLED(CONFIG_HTTP_SERVER_VERSION_3, (.fd_h3 = &_name##_fd_h3,))               \
                .detail = (void *)(_detail),                                                       \
                .concurrent = (_concurrent),                                                       \
                .backlog = (_backlog),                                                             \
                .data = &_name##_data,                                                             \
                .res_begin = (_res_begin),                                                         \
                .res_end = (_res_end),                                                             \
                .res_fallback = (_res_fallback),                                                   \
                .config = (_config),                                                               \
                COND_CODE_1(CONFIG_NET_SOCKETS_SOCKOPT_TLS,                                        \
                            (.sec_tag_list = COND_CODE_0(NUM_VA_ARGS_LESS_1(__VA_ARGS__), (NULL),  \
                                                         (GET_ARG_N(1, __VA_ARGS__))),), ())       \
                COND_CODE_1(CONFIG_NET_SOCKETS_SOCKOPT_TLS,                                        \
                            (.sec_tag_list_size = COND_CODE_0(NUM_VA_ARGS_LESS_1(__VA_ARGS__), (0),\
                                             (GET_ARG_N(1, GET_ARGS_LESS_N(1, __VA_ARGS__))))), ())\
        }


#define HTTP_SERVICE_DEFINE_EMPTY(_name, _host, _port, _concurrent, _backlog, _detail,             \
                                  _res_fallback, _config)                                          \
        __z_http_service_define(_name, _host, _port, _concurrent, _backlog, _detail,               \
                                _res_fallback, NULL, NULL, _config)

#define HTTPS_SERVICE_DEFINE_EMPTY(_name, _host, _port, _concurrent, _backlog, _detail,          \
                                   _res_fallback, _config, _sec_tag_list, _sec_tag_list_size)    \
        __z_http_service_define(_name, _host, _port, _concurrent, _backlog, _detail,             \
                                _res_fallback, NULL, NULL, _config,                              \
                                _sec_tag_list, _sec_tag_list_size);                              \
        BUILD_ASSERT(IS_ENABLED(CONFIG_NET_SOCKETS_SOCKOPT_TLS),                                 \
                     "TLS is required for HTTP secure (CONFIG_NET_SOCKETS_SOCKOPT_TLS)")

#define HTTP_SERVICE_DEFINE(_name, _host, _port, _concurrent, _backlog, _detail, _res_fallback,    \
                            _config)                                                               \
        extern struct http_resource_desc _CONCAT(_http_resource_desc_##_name, _list_start)[];      \
        extern struct http_resource_desc _CONCAT(_http_resource_desc_##_name, _list_end)[];        \
        __z_http_service_define(_name, _host, _port, _concurrent, _backlog, _detail,               \
                                _res_fallback,                                                     \
                                &_CONCAT(_http_resource_desc_##_name, _list_start)[0],             \
                                &_CONCAT(_http_resource_desc_##_name, _list_end)[0], _config);

#define HTTPS_SERVICE_DEFINE(_name, _host, _port, _concurrent, _backlog, _detail,              \
                             _res_fallback, _config, _sec_tag_list, _sec_tag_list_size)        \
        extern struct http_resource_desc _CONCAT(_http_resource_desc_##_name, _list_start)[];  \
        extern struct http_resource_desc _CONCAT(_http_resource_desc_##_name, _list_end)[];    \
        __z_http_service_define(_name, _host, _port, _concurrent, _backlog, _detail,           \
                                _res_fallback,                                                 \
                                &_CONCAT(_http_resource_desc_##_name, _list_start)[0],         \
                                &_CONCAT(_http_resource_desc_##_name, _list_end)[0], _config,  \
                                _sec_tag_list, _sec_tag_list_size);                            \
        BUILD_ASSERT(IS_ENABLED(CONFIG_NET_SOCKETS_SOCKOPT_TLS),                               \
                     "TLS is required for HTTP secure (CONFIG_NET_SOCKETS_SOCKOPT_TLS)")

#define HTTP_SERVICE_COUNT(_dst) STRUCT_SECTION_COUNT(http_service_desc, _dst)

#define HTTP_SERVICE_RESOURCE_COUNT(_service) ((_service)->res_end - (_service)->res_begin)

#define HTTP_SERVICE_FOREACH(_it) STRUCT_SECTION_FOREACH(http_service_desc, _it)

#define HTTP_RESOURCE_FOREACH(_service, _it)                                                       \
        STRUCT_SECTION_FOREACH_ALTERNATE(http_resource_desc_##_service, http_resource_desc, _it)

#define HTTP_SERVICE_FOREACH_RESOURCE(_service, _it)                                               \
        for (struct http_resource_desc *_it = (_service)->res_begin; ({                            \
                     __ASSERT(_it <= (_service)->res_end, "unexpected list end location");         \
                     _it < (_service)->res_end;                                                    \
             });                                                                                   \
             _it++)

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_HTTP_SERVICE_H_ */
```

## 99.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2022 Meta。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 137 行

如果还需要服务专用配置，可以在此添加。

### 注释 3：原第 146 行

用于 HTTP/3 的 QUIC 监听连接套接字（Listening connection socket），负责接受该服务的新连接。

不支持 HTTP/3 时设为 NULL；该服务尚未初始化或启用 HTTP/3 时设为 -1。如果支持 HTTP/3，此指针就不能为 NULL。

译注：原注释同时描述指针及 -1 状态，按原文保留；使用时须结合本字段声明区分指针与其所指向的套接字值。

### 注释 4：原第 376 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_HTTP_SERVICE_H_`。

## 99.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/service_8h.html)
- [zephyr/net/http/server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/net/tls_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)
- [http_resource_desc](../network_application_model_reference/P037_http_resource_desc_结构体.md)
- [resource](../network_application_model_reference/P037_http_resource_desc_结构体.md#a2882314e271a09d6bc9fae3f58558605)
- [detail](../network_application_model_reference/P037_http_resource_desc_结构体.md#afdf3332dbc4fb8c10ec8bc525cd8d498)
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
- [http_service_h3_config](../network_application_model_reference/P046_http_service_h3_config_结构体.md)
- [alt_svc_policy](../network_application_model_reference/P046_http_service_h3_config_结构体.md#a0be4af47f80b4734f43fbc04fd86163c)
- [enable_session_tickets](../network_application_model_reference/P046_http_service_h3_config_结构体.md#a0ffd5ab6f7804fb4dbd8cca2da6fda0a)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [max_early_data_size](../network_application_model_reference/P046_http_service_h3_config_结构体.md#afec0c9db1dd92540d988317a6d491075)
- [http_service_config](../network_application_model_reference/P045_http_service_config_结构体.md)
- [socket_create](../network_application_model_reference/P045_http_service_config_结构体.md#a7a3b7aa9e222cb816d7330c2c2be127f)
- [http_ver](../network_application_model_reference/P045_http_service_config_结构体.md#aa4c887036b350e7fc92799cefd0b0141)
- [h3](../network_application_model_reference/P045_http_service_config_结构体.md#a4738a850d59dc1a6db82bd12174506ec)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [http_resource_detail](../network_application_model_reference/P038_http_resource_detail_结构体.md)
- [sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)
- [server.h](https://docs.zephyrproject.org/latest/doxygen/html/http_2server_8h.html)
- [http_resource_desc::resource](../network_application_model_reference/P037_http_resource_desc_结构体.md#a2882314e271a09d6bc9fae3f58558605)
- [http_resource_desc::detail](../network_application_model_reference/P037_http_resource_desc_结构体.md#afdf3332dbc4fb8c10ec8bc525cd8d498)
- [http_service_config::h3](../network_application_model_reference/P045_http_service_config_结构体.md#a4738a850d59dc1a6db82bd12174506ec)
- [http_service_config::socket_create](../network_application_model_reference/P045_http_service_config_结构体.md#a7a3b7aa9e222cb816d7330c2c2be127f)
- [http_service_config::http_ver](../network_application_model_reference/P045_http_service_config_结构体.md#aa4c887036b350e7fc92799cefd0b0141)
- [http_service_h3_config::alt_svc_policy](../network_application_model_reference/P046_http_service_h3_config_结构体.md#a0be4af47f80b4734f43fbc04fd86163c)
- [http_service_h3_config::enable_session_tickets](../network_application_model_reference/P046_http_service_h3_config_结构体.md#a0ffd5ab6f7804fb4dbd8cca2da6fda0a)
- [http_service_h3_config::max_early_data_size](../network_application_model_reference/P046_http_service_h3_config_结构体.md#afec0c9db1dd92540d988317a6d491075)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [tls_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P098_rpi-pico-rp2350b-pinctrl.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P100_shared_irq.h_源码浏览.md)
