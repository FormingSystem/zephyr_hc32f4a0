---
id: learning.zephyr-docs.api-source-configuration-reference.page-104
title: socket_service.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/socket__service_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第104章\_socket\_service.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/socket__service_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/socket__service_8h.html)。

## 104.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="foldopen00050"></a>
<a id="l00050"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00056"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="foldopen00071"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
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
<a id="l00120"></a>
<a id="foldopen00139"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="foldopen00152"></a>
<a id="l00152"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00167"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="foldopen00179"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="foldopen00193"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="agroup__bsd__socket__service_html_ga0b817d72b63fd3369c6a26723cbbc4fa"></a>
<a id="agroup__bsd__socket__service_html_ga15f0c6f47c7f5e28a26309fe875b92bd"></a>
<a id="agroup__bsd__socket__service_html_ga5d9495470c1ade51791df56c59cfb1f5"></a>
<a id="agroup__bsd__socket__service_html_gaa72bb82aa413b711e61eda092504b091"></a>
<a id="agroup__bsd__socket__service_html_gacc78dbe6c186fc86f23ab90943ee3097"></a>
<a id="agroup__bsd__socket__service_html_gae2d4eea01c9ea4e6a48315681e05afd6"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="alog__core_8h_html"></a>
<a id="anet_2socket_8h_html"></a>
<a id="astructnet__socket__service__desc_html"></a>
<a id="astructnet__socket__service__desc_html_a08da5714fafa3f678771ea3d5204971a"></a>
<a id="astructnet__socket__service__desc_html_a480b960a8d130ded4668f355a8e5fd83"></a>
<a id="astructnet__socket__service__desc_html_a5c958339cbc98e7c4490952ce1e9fbc9"></a>
<a id="astructnet__socket__service__desc_html_a62104a9136d2abd88c25480eee2b187a"></a>
<a id="astructnet__socket__service__event_html"></a>
<a id="astructnet__socket__service__event_html_a7052fad6a65c5a1b610a69e16fc72785"></a>
<a id="astructnet__socket__service__event_html_a8246a87e2171474eb214bb8f909cb9bf"></a>
<a id="astructnet__socket__service__event_html_a82695b0eaa7c563033fce4afde33cab9"></a>
<a id="astructnet__socket__service__event_html_aa11bb43a2cc48d167bf8995d860fd638"></a>
<a id="astructzsock__pollfd_html"></a>

```c


/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_SOCKET_SERVICE_H_
#define ZEPHYR_INCLUDE_NET_SOCKET_SERVICE_H_


#include <sys/types.h>
#include <zephyr/types.h>
#include <zephyr/net/socket.h>
#include <zephyr/logging/log_core.h>

#ifdef __cplusplus
extern "C" {
#endif

struct net_socket_service_event;

typedef void (*net_socket_service_handler_t)(struct net_socket_service_event *pev);

struct net_socket_service_event {
        net_socket_service_handler_t callback;
        struct zsock_pollfd event;
        void *user_data;
        struct net_socket_service_desc *svc;
};

struct net_socket_service_desc {
#if CONFIG_NET_SOCKETS_LOG_LEVEL >= LOG_LEVEL_DBG
        const char *owner;
#endif
        struct net_socket_service_event *pev;
        int pev_len;
        int *idx;
};


#define __z_net_socket_svc_get_name(_svc_id) __z_net_socket_service_##_svc_id
#define __z_net_socket_svc_get_idx(_svc_id) __z_net_socket_service_idx_##_svc_id
#define __z_net_socket_svc_get_owner __FILE__ ":" STRINGIFY(__LINE__)

/* Request sockets to be closed in addition to unregistered */
#define NET_SOCKET_SERVICE_CLOSE_SOCKETS (void *)1

#if CONFIG_NET_SOCKETS_LOG_LEVEL >= LOG_LEVEL_DBG
#define NET_SOCKET_SERVICE_OWNER .owner = __z_net_socket_svc_get_owner,
#else
#define NET_SOCKET_SERVICE_OWNER
#endif

#define __z_net_socket_service_define(_name, _cb, _count, ...) \
        static int __z_net_socket_svc_get_idx(_name);                   \
        static struct net_socket_service_event                          \
                        __z_net_socket_svc_get_name(_name)[_count] = {  \
                [0 ... ((_count) - 1)] = {                              \
                        .event.fd = -1, /* Invalid socket */            \
                        .callback = _cb,                                \
                }                                                       \
        };                                                              \
        COND_CODE_0(NUM_VA_ARGS_LESS_1(__VA_ARGS__), (), __VA_ARGS__)   \
        const STRUCT_SECTION_ITERABLE(net_socket_service_desc, _name) = { \
                NET_SOCKET_SERVICE_OWNER                                \
                .pev = __z_net_socket_svc_get_name(_name),              \
                .pev_len = (_count),                                    \
                .idx = &__z_net_socket_svc_get_idx(_name),              \
        }


#define NET_SOCKET_SERVICE_SYNC_DEFINE(name, cb, count) \
        __z_net_socket_service_define(name, cb, count)

#define NET_SOCKET_SERVICE_SYNC_DEFINE_STATIC(name, cb, count)  \
        __z_net_socket_service_define(name, cb, count, static)

__syscall int net_socket_service_register(const struct net_socket_service_desc *service,
                                          struct zsock_pollfd *fds, int len, void *user_data);

static inline int net_socket_service_unregister(const struct net_socket_service_desc *service)
{
        return net_socket_service_register(service, NULL, 0, NULL);
}

static inline int net_socket_service_close(const struct net_socket_service_desc *service)
{
        return net_socket_service_register(service, NULL, 0, NET_SOCKET_SERVICE_CLOSE_SOCKETS);
}

typedef void (*net_socket_service_cb_t)(const struct net_socket_service_desc *svc,
                                        void *user_data);

void net_socket_service_foreach(net_socket_service_cb_t cb, void *user_data);

#ifdef __cplusplus
}
#endif

#include <zephyr/syscalls/socket_service.h>


#endif /* ZEPHYR_INCLUDE_NET_SOCKET_SERVICE_H_ */
```

## 104.2\_可见注释译文（Comments）

### 注释 1：原第 9 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 93 行

请求在注销套接字之外，也关闭这些套接字。

### 注释 3：原第 107 行

无效套接字（Invalid socket）。

### 注释 4：原第 226 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SOCKET_SERVICE_H_`。

## 104.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/socket__service_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [zephyr/logging/log_core.h](../log_internal_reference/P001_日志核心头文件参考.md)
- [net_socket_service_event](../network_core_model_reference/P124_net_socket_service_event_结构体.md)
- [net_socket_service_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga5d9495470c1ade51791df56c59cfb1f5)
- [callback](../network_core_model_reference/P124_net_socket_service_event_结构体.md#a82695b0eaa7c563033fce4afde33cab9)
- [zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)
- [event](../network_core_model_reference/P124_net_socket_service_event_结构体.md#a8246a87e2171474eb214bb8f909cb9bf)
- [user_data](../network_core_model_reference/P124_net_socket_service_event_结构体.md#aa11bb43a2cc48d167bf8995d860fd638)
- [net_socket_service_desc](../network_core_model_reference/P123_net_socket_service_desc_结构体.md)
- [svc](../network_core_model_reference/P124_net_socket_service_event_结构体.md#a7052fad6a65c5a1b610a69e16fc72785)
- [owner](../network_core_model_reference/P123_net_socket_service_desc_结构体.md#a08da5714fafa3f678771ea3d5204971a)
- [pev](../network_core_model_reference/P123_net_socket_service_desc_结构体.md#a62104a9136d2abd88c25480eee2b187a)
- [pev_len](../network_core_model_reference/P123_net_socket_service_desc_结构体.md#a5c958339cbc98e7c4490952ce1e9fbc9)
- [idx](../network_core_model_reference/P123_net_socket_service_desc_结构体.md#a480b960a8d130ded4668f355a8e5fd83)
- [net_socket_service_register](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#gaa72bb82aa413b711e61eda092504b091)
- [net_socket_service_unregister](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#gae2d4eea01c9ea4e6a48315681e05afd6)
- [net_socket_service_close](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga0b817d72b63fd3369c6a26723cbbc4fa)
- [net_socket_service_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#ga15f0c6f47c7f5e28a26309fe875b92bd)
- [net_socket_service_foreach](https://docs.zephyrproject.org/latest/doxygen/html/group__bsd__socket__service.html#gacc78dbe6c186fc86f23ab90943ee3097)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [log_core.h](../log_internal_reference/P001_日志核心头文件参考.md)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [net_socket_service_desc::owner](../network_core_model_reference/P123_net_socket_service_desc_结构体.md#a08da5714fafa3f678771ea3d5204971a)
- [net_socket_service_desc::idx](../network_core_model_reference/P123_net_socket_service_desc_结构体.md#a480b960a8d130ded4668f355a8e5fd83)
- [net_socket_service_desc::pev_len](../network_core_model_reference/P123_net_socket_service_desc_结构体.md#a5c958339cbc98e7c4490952ce1e9fbc9)
- [net_socket_service_desc::pev](../network_core_model_reference/P123_net_socket_service_desc_结构体.md#a62104a9136d2abd88c25480eee2b187a)
- [net_socket_service_event::svc](../network_core_model_reference/P124_net_socket_service_event_结构体.md#a7052fad6a65c5a1b610a69e16fc72785)
- [net_socket_service_event::event](../network_core_model_reference/P124_net_socket_service_event_结构体.md#a8246a87e2171474eb214bb8f909cb9bf)
- [net_socket_service_event::callback](../network_core_model_reference/P124_net_socket_service_event_结构体.md#a82695b0eaa7c563033fce4afde33cab9)
- [net_socket_service_event::user_data](../network_core_model_reference/P124_net_socket_service_event_结构体.md#aa11bb43a2cc48d167bf8995d860fd638)

---

[上一章](P103_six301-clock.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P105_socket_types.h_源码浏览.md)
