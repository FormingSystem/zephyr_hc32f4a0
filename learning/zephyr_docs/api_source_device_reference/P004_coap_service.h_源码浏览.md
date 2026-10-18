---
id: learning.zephyr-docs.api-source-device-reference.page-4
title: coap_service.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap__service_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_coap\_service.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/coap__service_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/coap__service_8h.html)。

## 4.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00036"></a>
<a id="l00042"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00141"></a>
<a id="foldopen00178"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="foldopen00199"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="foldopen00228"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00236"></a>
<a id="l00237"></a>
<a id="foldopen00255"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00279"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00286"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="foldopen00312"></a>
<a id="l00312"></a>
<a id="l00313"></a>
<a id="l00314"></a>
<a id="l00320"></a>
<a id="l00321"></a>
<a id="foldopen00330"></a>
<a id="l00330"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="foldopen00341"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00397"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00452"></a>
<a id="l00453"></a>
<a id="l00454"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="l00460"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="acoap_8h_html"></a>
<a id="acoap__oscore_8h_html"></a>
<a id="agroup__coap__service_html_ga08638f2001ca2f807489c12ff426784c"></a>
<a id="agroup__coap__service_html_ga19a7a0e3aa5b56ef5cd6c0ce8f142147"></a>
<a id="agroup__coap__service_html_ga40a0a599471f7f283b455809d4cf7587"></a>
<a id="agroup__coap__service_html_ga58bc31fc4d53ebce9c18ccbc5aab72ce"></a>
<a id="agroup__coap__service_html_ga7329c8a02caa7a0d9becb669932895ca"></a>
<a id="agroup__coap__service_html_gaa25bfeb07a50674f054b5b56005ac021"></a>
<a id="agroup__coap__service_html_gad1e64f8fe2c6ae32730a9a61f8351bab"></a>
<a id="agroup__coap__service_html_gad575a7209a56874002c540eb3f8c0733"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="agroup__tls__credentials_html_gaadfe9694309e473f7be74ed98dfb36d3"></a>
<a id="aparser_8h_html_ab6b306ef981f5e21bb41ea2c2dbe8cd9"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructcoap__observer_html"></a>
<a id="astructcoap__oscore__exchange_html"></a>
<a id="astructcoap__packet_html"></a>
<a id="astructcoap__pending_html"></a>
<a id="astructcoap__resource_html"></a>
<a id="astructcoap__transmission__parameters_html"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="asys_2iterable__sections_8h_html"></a>
<a id="atls__credentials_8h_html"></a>

```c
/*
 * Copyright (c) 2023 Basalte bv
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_COAP_SERVICE_H_
#define ZEPHYR_INCLUDE_NET_COAP_SERVICE_H_

#include <zephyr/net/coap.h>
#include <zephyr/sys/iterable_sections.h>
#include <zephyr/net/tls_credentials.h>

#if defined(CONFIG_COAP_OSCORE)
#include <zephyr/net/coap_oscore.h>
#endif

#ifdef __cplusplus
extern "C" {
#endif



#define COAP_SERVICE_AUTOSTART          BIT(0)



struct coap_service_data {
        int sock_fd;
        bool close_requested;
        struct coap_observer observers[CONFIG_COAP_SERVICE_OBSERVERS];
        struct coap_pending pending[CONFIG_COAP_SERVICE_PENDING_MESSAGES];
#if defined(CONFIG_COAP_OSCORE) || defined(__DOXYGEN__)
        struct coap_oscore_exchange *oscore_exchange_cache;
#endif /* CONFIG_COAP_OSCORE */
        /* Local address to send the reply from; NET_AF_UNSPEC means let the OS pick. */
        struct net_sockaddr_storage current_local_addr;
        struct net_sockaddr_storage pending_local_addr[CONFIG_COAP_SERVICE_PENDING_MESSAGES];
        /* Cached at coap_service_start() so the hot receive path doesn't recompute it. */
        bool secure;
        /* Set when the socket agreed to turn on PKTINFO. Some offloaded
         * sockets support recvfrom() but not recvmsg().
         */
        bool pktinfo_supported;
};

struct coap_service {
        const char *name;
        const char *host;
        uint16_t *port;
        uint8_t flags;
        struct coap_resource *res_begin;
        struct coap_resource *res_end;
        struct coap_service_data *data;
#if defined(CONFIG_NET_SOCKETS_ENABLE_DTLS)
        const sec_tag_t *sec_tag_list;
        size_t sec_tag_list_size;
#endif
#if defined(CONFIG_COAP_OSCORE) || defined(__DOXYGEN__)
        bool oscore_required;
#endif
};

#if defined(CONFIG_NET_SOCKETS_ENABLE_DTLS)
#define __z_coap_service_secure(_sec_tag_list, _sec_tag_list_size)                              \
                .sec_tag_list = _sec_tag_list,                                                  \
                .sec_tag_list_size = _sec_tag_list_size,
#else
#define __z_coap_service_secure(...)
#endif

#if defined(CONFIG_COAP_OSCORE)
/* Statically define the per-service OSCORE exchange cache. */
#define __z_coap_oscore_cache_define(_name)                                                        \
        static struct coap_oscore_exchange _CONCAT(coap_oscore_exchange_cache_,                    \
                                                   _name)[CONFIG_COAP_OSCORE_EXCHANGE_CACHE_SIZE];
#define __z_coap_oscore_cache_ptr(_name) (_CONCAT(coap_oscore_exchange_cache_, _name))
#define __z_coap_service_oscore(_required) .oscore_required = (_required),
#define __z_coap_service_oscore_data(_cache)                                                       \
        .oscore_exchange_cache = (_cache),
#else
#define __z_coap_service_oscore(...)
#define __z_coap_oscore_cache_define(_name)
#define __z_coap_oscore_cache_ptr(_name) NULL
#define __z_coap_service_oscore_data(...)
#endif

/* clang-format off */
#define __z_coap_service_define(_name, _host, _port, _flags, _res_begin, _res_end, _sec_tag_list,  \
                                _sec_tag_list_size, _oscore_required, _oscore_cache)               \
        static struct coap_service_data _CONCAT(coap_service_data_, _name) = {                     \
                .sock_fd = -1,                                                                     \
                __z_coap_service_oscore_data(_oscore_cache)                                        \
        };                                                                                         \
        const STRUCT_SECTION_ITERABLE(coap_service, _name) = {                                     \
                .name = STRINGIFY(_name),                                                          \
                .host = _host,                                                                     \
                .port = (uint16_t *)(_port),                                                       \
                .flags = _flags,                                                                   \
                .res_begin = (_res_begin),                                                         \
                .res_end = (_res_end),                                                             \
                .data = &_CONCAT(coap_service_data_, _name),                                       \
                __z_coap_service_secure(_sec_tag_list, _sec_tag_list_size)                         \
                __z_coap_service_oscore(_oscore_required)                                          \
        }
/* clang-format on */


#define COAP_RESOURCE_DEFINE(_name, _service, ...)                                              \
        STRUCT_SECTION_ITERABLE_ALTERNATE(_CONCAT(coap_resource_, _service), coap_resource,     \
                                          _name) = __VA_ARGS__

#define COAP_SERVICE_DEFINE(_name, _host, _port, _flags)                                           \
        extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[];       \
        extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[];         \
        __z_coap_service_define(_name, _host, _port, _flags,                                       \
                                &_CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[0],         \
                                &_CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[0], NULL, 0,  \
                                false, NULL)

#define COAPS_SERVICE_DEFINE(_name, _host, _port, _flags, _sec_tag_list, _sec_tag_list_size)       \
        BUILD_ASSERT(IS_ENABLED(CONFIG_NET_SOCKETS_ENABLE_DTLS),                                   \
                     "DTLS is required for CoAP secure (CONFIG_NET_SOCKETS_ENABLE_DTLS)");         \
        extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[];       \
        extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[];         \
        __z_coap_service_define(_name, _host, _port, _flags,                                       \
                                &_CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[0],         \
                                &_CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[0],           \
                                _sec_tag_list, _sec_tag_list_size, false, NULL)

#define COAP_SERVICE_DEFINE_OSCORE(_name, _host, _port, _flags, _oscore_required)                 \
        extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[];       \
        extern struct coap_resource _CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[];         \
        __z_coap_oscore_cache_define(_name) __z_coap_service_define(                               \
                _name, _host, _port, _flags,                                                       \
                &_CONCAT(_CONCAT(_coap_resource_, _name), _list_start)[0],                         \
                &_CONCAT(_CONCAT(_coap_resource_, _name), _list_end)[0], NULL, 0,                  \
                (_oscore_required), __z_coap_oscore_cache_ptr(_name))

#define COAPS_SERVICE_DEFINE_OSCORE(_name, _host, _port, _flags, _sec_tag_list,                    \
                                    _sec_tag_list_size, _oscore_required)                          \
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

#define COAP_SERVICE_COUNT(_dst) STRUCT_SECTION_COUNT(coap_service, _dst)

#define COAP_SERVICE_RESOURCE_COUNT(_service) ((_service)->res_end - (_service)->res_begin)

#define COAP_SERVICE_HAS_RESOURCE(_service, _resource)                                          \
        ((_service)->res_begin <= _resource && _resource < (_service)->res_end)

#define COAP_SERVICE_FOREACH(_it) STRUCT_SECTION_FOREACH(coap_service, _it)

#define COAP_RESOURCE_FOREACH(_service, _it)                                                    \
        STRUCT_SECTION_FOREACH_ALTERNATE(_CONCAT(coap_resource_, _service), coap_resource, _it)

#define COAP_SERVICE_FOREACH_RESOURCE(_service, _it)                                            \
        for (struct coap_resource *_it = (_service)->res_begin; ({                              \
                __ASSERT(_it <= (_service)->res_end, "unexpected list end location");           \
                _it < (_service)->res_end;                                                      \
        }); _it++)

int coap_service_start(const struct coap_service *service);

int coap_service_stop(const struct coap_service *service);

int coap_service_is_running(const struct coap_service *service);

int coap_service_send(const struct coap_service *service, const struct coap_packet *cpkt,
                      const struct net_sockaddr *addr, net_socklen_t addr_len,
                      const struct coap_transmission_parameters *params);

int coap_resource_send(const struct coap_resource *resource, const struct coap_packet *cpkt,
                       const struct net_sockaddr *addr, net_socklen_t addr_len,
                       const struct coap_transmission_parameters *params);

int coap_resource_parse_observe(struct coap_resource *resource, const struct coap_packet *request,
                                const struct net_sockaddr *addr);

int coap_resource_remove_observer_by_addr(struct coap_resource *resource,
                                          const struct net_sockaddr *addr);

int coap_resource_remove_observer_by_token(struct coap_resource *resource,
                                           const uint8_t *token, uint8_t token_len);


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_COAP_SERVICE_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Basalte bv。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 63 行

条件编译配置（Configuration）标记：`CONFIG_COAP_OSCORE`。

### 注释 3：原第 64 行

发送回复所用的本地地址（Local Address）；`NET_AF_UNSPEC` 表示由操作系统（OS）选择。

### 注释 4：原第 67 行

在 `coap_service_start()` 中缓存（Cache），使频繁执行的接收路径（Hot Receive Path）无需重复计算。

### 注释 5：原第 69 行

套接字（Socket）同意启用数据包信息（PKTINFO）时设置。某些卸载型套接字（Offloaded Sockets）支持 `recvfrom()`，但不支持 `recvmsg()`。

### 注释 6：原第 105 行

静态定义每个服务的受限 RESTful 环境对象安全交换缓存（Per-Service OSCORE Exchange Cache）。

### 注释 7：原第 120 行

关闭 clang-format 自动排版（clang-format off）。

### 注释 8：原第 138 行

开启 clang-format 自动排版（clang-format on）。

### 注释 9：原第 463 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_COAP_SERVICE_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/coap__service_8h.html)
- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [zephyr/net/tls_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)
- [zephyr/net/coap_oscore.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__oscore_8h.html)
- [coap_observer](../network_application_model_reference/P009_coap_observer_结构体.md)
- [coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)
- [coap_oscore_exchange](../network_application_model_reference/P011_coap_oscore_exchange_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [flags](../api_file_reference/P290_zephyr__net__http__parser.h_文件参考.md#ab6b306ef981f5e21bb41ea2c2dbe8cd9)
- [sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)
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
- [coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)
- [coap_oscore.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__oscore_8h.html)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [tls_credentials.h](https://docs.zephyrproject.org/latest/doxygen/html/tls__credentials_8h.html)

---

[上一章](P003_clock_control_bflb_common.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_color_dither.h_源码浏览.md)
