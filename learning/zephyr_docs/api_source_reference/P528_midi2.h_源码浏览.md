---
id: learning.zephyr-docs.api-source-reference.page-528
title: midi2.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/midi2_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第528章\_midi2.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/midi2_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/midi2_8h.html)。

## 528.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00016"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="foldopen00093"></a>
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
<a id="foldopen00111"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00115"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="foldopen00121"></a>
<a id="l00121"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="foldopen00131"></a>
<a id="l00131"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00143"></a>
<a id="l00148"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00161"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00172"></a>
<a id="l00174"></a>
<a id="l00176"></a>
<a id="l00177"></a>
<a id="l00179"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00184"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="foldopen00192"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00196"></a>
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="foldopen00204"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="agroup__net__midi2_html_ga638d918c5e87be3d7f1013a2ad2810dd"></a>
<a id="agroup__net__midi2_html_ga694e4920c2091bfc532ad23e2e2bbd46"></a>
<a id="agroup__net__midi2_html_ga918cdeae835fd4aa1c6cd810b579b085"></a>
<a id="agroup__net__midi2_html_gabc608c8a74f503f729edfc0506a356cd"></a>
<a id="agroup__net__midi2_html_gae6ec636fa7aadbe9b7675404015d01e7"></a>
<a id="agroup__net__midi2_html_ggae6ec636fa7aadbe9b7675404015d01e7a42fa2f83dbd21f9747e32ac5f5180f90"></a>
<a id="agroup__net__midi2_html_ggae6ec636fa7aadbe9b7675404015d01e7a55b35a2303b341aa7309c0dc3898a414"></a>
<a id="agroup__net__midi2_html_ggae6ec636fa7aadbe9b7675404015d01e7ab0d6258fa6ce35e6e9a260d585d1647e"></a>
<a id="amidi_8h_html"></a>
<a id="anet_2socket_8h_html"></a>
<a id="aparser__state_8h_html_adc6e5733fc3c22f0a7b2914188c49c90"></a>
<a id="astdint_8h_html"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructk__work_html"></a>
<a id="astructmidi__ump_html"></a>
<a id="astructnet__buf_html"></a>
<a id="astructnet__sockaddr__in6_html"></a>
<a id="astructnet__sockaddr__in_html"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructnetmidi2__ep_html"></a>
<a id="astructnetmidi2__ep_html_a1389cb4e0a73ad7d44143d59c6cbac2e"></a>
<a id="astructnetmidi2__ep_html_a1da1c0bef306386df5d0923cadb04a10"></a>
<a id="astructnetmidi2__ep_html_a37befb690f98866d52abac009cc237c7"></a>
<a id="astructnetmidi2__ep_html_a439571c6a042c28e9002b090e617a391"></a>
<a id="astructnetmidi2__ep_html_a5d84716f1ff7f843391ec7faa633154d"></a>
<a id="astructnetmidi2__ep_html_a7093bf87340a47a46180e3a720ee94c4"></a>
<a id="astructnetmidi2__ep_html_aba537e498bc6210fd6b718879db711f3"></a>
<a id="astructnetmidi2__ep_html_ac6f1588dc3845a847dcebe81df64c776"></a>
<a id="astructnetmidi2__ep_html_adf7a2f4826320c614bcb2cea9b5b214e"></a>
<a id="astructnetmidi2__ep_html_ae73643aad93d83005fb5fa19b8a99ac7"></a>
<a id="astructnetmidi2__ep_html_afe9c4413a90f92834fdf06b59fc31363"></a>
<a id="astructnetmidi2__session_html"></a>
<a id="astructnetmidi2__session_html_a4c295b22b957f2a2317ab8b7c53a5b4f"></a>
<a id="astructnetmidi2__session_html_a5b346997cfada6aa8ebee00de696d297a17fd2771abb25775cce6372d1fbddbbc"></a>
<a id="astructnetmidi2__session_html_a5b346997cfada6aa8ebee00de696d297a50d0e9bb5d67e0710cfc7c0503404877"></a>
<a id="astructnetmidi2__session_html_a5b346997cfada6aa8ebee00de696d297a5c0dce1e59eb620eb299eb16c79c3124"></a>
<a id="astructnetmidi2__session_html_a5b346997cfada6aa8ebee00de696d297a85a50751609d84c4151a2393865bebcc"></a>
<a id="astructnetmidi2__session_html_a5b346997cfada6aa8ebee00de696d297a978ea2a084813e350383bcfe961ab964"></a>
<a id="astructnetmidi2__session_html_a5b346997cfada6aa8ebee00de696d297ae75b03f14efdd97f0859ff0edb4f7d64"></a>
<a id="astructnetmidi2__session_html_a5b346997cfada6aa8ebee00de696d297af88daf6789f7d887f069e5c11d91b18f"></a>
<a id="astructnetmidi2__session_html_a5db865937e4719ed2ee444c6b1edab6a"></a>
<a id="astructnetmidi2__session_html_a65c740d870d3d0a33e6d8c9150bf6534"></a>
<a id="astructnetmidi2__session_html_a6d2043af218d266065b90cc8762306a3"></a>
<a id="astructnetmidi2__session_html_a6d6d7cc6d97a83125b0422176e1d9a66"></a>
<a id="astructnetmidi2__session_html_a7a1d7bd416cc64e254e4a74c766a299c"></a>
<a id="astructnetmidi2__session_html_a8fdb57537d7ebefd4abae5443aed0cb6"></a>
<a id="astructnetmidi2__session_html_aa1e41d310563718ad152c21b88b516fe"></a>
<a id="astructnetmidi2__session_html_adb2f4b5f0b4a8728085877b1c73939f4"></a>
<a id="astructnetmidi2__user_html"></a>
<a id="astructnetmidi2__user_html_a71fb204799bd53af65899e46ea771844"></a>
<a id="astructnetmidi2__user_html_aa334b6f3b82e86e90b6c8c298cf094f6"></a>
<a id="astructnetmidi2__userlist_html"></a>
<a id="astructnetmidi2__userlist_html_a84b04acb7bb17f81f164af79e6b6950d"></a>
<a id="astructnetmidi2__userlist_html_aeca603e7b653c9dd616e32c00783d6dd"></a>
<a id="astructzsock__pollfd_html"></a>

```c
/*
 * Copyright (c) 2025 Titouan Christophe
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_MIDI2_H_
#define ZEPHYR_INCLUDE_NET_MIDI2_H_




#include <stdint.h>
#include <zephyr/audio/midi.h>
#include <zephyr/net/socket.h>

#define NETMIDI2_NONCE_SIZE  16

#define NETMIDI2_EP_DEFINE(_var_name, _ep_name, _piid, _port) \
        static struct netmidi2_ep _var_name = { \
                .name = (_ep_name), \
                .piid = (_piid), \
                .addr4.sin_port = (_port), \
                .auth_type = NETMIDI2_AUTH_NONE, \
        }

#define NETMIDI2_EP_DEFINE_WITH_AUTH(_var_name, _ep_name, _piid, _port, _secret) \
        static struct netmidi2_ep _var_name = { \
                .name = (_ep_name), \
                .piid = (_piid), \
                .addr4.sin_port = (_port), \
                .auth_type = NETMIDI2_AUTH_SHARED_SECRET, \
                .shared_auth_secret = (_secret), \
        }

#define NETMIDI2_EP_DEFINE_WITH_USERS(_var_name, _ep_name, _piid, _port, ...) \
        static const struct netmidi2_userlist users_of_##_var_name = { \
                .n_users = ARRAY_SIZE(((struct netmidi2_user []) { __VA_ARGS__ })), \
                .users = { __VA_ARGS__ }, \
        }; \
        static struct netmidi2_ep _var_name = { \
                .name = (_ep_name), \
                .piid = (_piid), \
                .addr4.sin_port = (_port), \
                .auth_type = NETMIDI2_AUTH_USER_PASSWORD, \
                .userlist = &users_of_##_var_name, \
        }

struct netmidi2_ep;

struct netmidi2_user {
        const char *name;
        const char *password;
};

struct netmidi2_userlist {
        size_t n_users;
        const struct netmidi2_user users[];
};

struct netmidi2_session {
        enum {
                NETMIDI2_SESSION_NOT_INITIALIZED = 0,
                NETMIDI2_SESSION_IDLE,
                NETMIDI2_SESSION_PENDING_INVITATION,
                NETMIDI2_SESSION_AUTH_REQUIRED,
                NETMIDI2_SESSION_ESTABLISHED,
                NETMIDI2_SESSION_PENDING_RESET,
                NETMIDI2_SESSION_PENDING_BYE,
        } state;
        uint16_t tx_ump_seq;
        uint16_t rx_ump_seq;
        struct net_sockaddr_storage addr;
        net_socklen_t addr_len;
        struct netmidi2_ep *ep;
#if defined(CONFIG_NETMIDI2_HOST_AUTH) || defined(__DOXYGEN__)
        const struct netmidi2_user *user;
        char nonce[NETMIDI2_NONCE_SIZE];
#endif
        struct net_buf *tx_buf;
        struct k_work tx_work;
};

enum netmidi2_auth_type {
        NETMIDI2_AUTH_NONE,
        NETMIDI2_AUTH_SHARED_SECRET,
        NETMIDI2_AUTH_USER_PASSWORD,
};

struct netmidi2_ep {
        const char *name;
        const char *piid;
        union {
                struct net_sockaddr addr;
                struct net_sockaddr_in addr4;
                struct net_sockaddr_in6 addr6;
        };
        struct zsock_pollfd pollsock;
        void (*rx_packet_cb)(struct netmidi2_session *session,
                             const struct midi_ump ump);
        struct netmidi2_session peers[CONFIG_NETMIDI2_HOST_MAX_CLIENTS];
        enum netmidi2_auth_type auth_type;
#if defined(CONFIG_NETMIDI2_HOST_AUTH) || defined(__DOXYGEN__)
        union {
                const char *shared_auth_secret;
                const struct netmidi2_userlist *userlist;
        };
#endif
};

int netmidi2_host_ep_start(struct netmidi2_ep *ep);

void netmidi2_broadcast(struct netmidi2_ep *ep, const struct midi_ump ump);

void netmidi2_send(struct netmidi2_session *sess, const struct midi_ump ump);


#endif
```

## 528.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2025 Titouan Christophe。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

## 528.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/midi2_8h.html)
- [stdint.h](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html)
- [zephyr/audio/midi.h](https://docs.zephyrproject.org/latest/doxygen/html/midi_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [netmidi2_ep](../network_service_model_reference/P031_netmidi2_ep_结构体.md)
- [netmidi2_user](../network_service_model_reference/P033_netmidi2_user_结构体.md)
- [name](../network_service_model_reference/P033_netmidi2_user_结构体.md#a71fb204799bd53af65899e46ea771844)
- [password](../network_service_model_reference/P033_netmidi2_user_结构体.md#aa334b6f3b82e86e90b6c8c298cf094f6)
- [netmidi2_userlist](../network_service_model_reference/P034_netmidi2_userlist_结构体.md)
- [n_users](../network_service_model_reference/P034_netmidi2_userlist_结构体.md#a84b04acb7bb17f81f164af79e6b6950d)
- [users](../network_service_model_reference/P034_netmidi2_userlist_结构体.md#aeca603e7b653c9dd616e32c00783d6dd)
- [netmidi2_session](../network_service_model_reference/P032_netmidi2_session_结构体.md)
- [NETMIDI2_SESSION_NOT_INITIALIZED](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297a85a50751609d84c4151a2393865bebcc)
- [NETMIDI2_SESSION_IDLE](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297a978ea2a084813e350383bcfe961ab964)
- [NETMIDI2_SESSION_PENDING_INVITATION](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297a17fd2771abb25775cce6372d1fbddbbc)
- [NETMIDI2_SESSION_AUTH_REQUIRED](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297a5c0dce1e59eb620eb299eb16c79c3124)
- [NETMIDI2_SESSION_ESTABLISHED](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297af88daf6789f7d887f069e5c11d91b18f)
- [NETMIDI2_SESSION_PENDING_RESET](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297a50d0e9bb5d67e0710cfc7c0503404877)
- [NETMIDI2_SESSION_PENDING_BYE](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297ae75b03f14efdd97f0859ff0edb4f7d64)
- [state](https://docs.zephyrproject.org/latest/doxygen/html/parser__state_8h.html#adc6e5733fc3c22f0a7b2914188c49c90)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [tx_ump_seq](../network_service_model_reference/P032_netmidi2_session_结构体.md#a6d6d7cc6d97a83125b0422176e1d9a66)
- [rx_ump_seq](../network_service_model_reference/P032_netmidi2_session_结构体.md#adb2f4b5f0b4a8728085877b1c73939f4)
- [addr](../network_service_model_reference/P032_netmidi2_session_结构体.md#a7a1d7bd416cc64e254e4a74c766a299c)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [addr_len](../network_service_model_reference/P032_netmidi2_session_结构体.md#a6d2043af218d266065b90cc8762306a3)
- [ep](../network_service_model_reference/P032_netmidi2_session_结构体.md#aa1e41d310563718ad152c21b88b516fe)
- [user](../network_service_model_reference/P032_netmidi2_session_结构体.md#a4c295b22b957f2a2317ab8b7c53a5b4f)
- [nonce](../network_service_model_reference/P032_netmidi2_session_结构体.md#a8fdb57537d7ebefd4abae5443aed0cb6)
- [NETMIDI2_NONCE_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga918cdeae835fd4aa1c6cd810b579b085)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [tx_buf](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5db865937e4719ed2ee444c6b1edab6a)
- [k_work](../kernel_runtime_model_reference/P008_k_work_结构体.md)
- [tx_work](../network_service_model_reference/P032_netmidi2_session_结构体.md#a65c740d870d3d0a33e6d8c9150bf6534)
- [netmidi2_auth_type](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#gae6ec636fa7aadbe9b7675404015d01e7)
- [NETMIDI2_AUTH_NONE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ggae6ec636fa7aadbe9b7675404015d01e7ab0d6258fa6ce35e6e9a260d585d1647e)
- [NETMIDI2_AUTH_SHARED_SECRET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ggae6ec636fa7aadbe9b7675404015d01e7a42fa2f83dbd21f9747e32ac5f5180f90)
- [NETMIDI2_AUTH_USER_PASSWORD](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ggae6ec636fa7aadbe9b7675404015d01e7a55b35a2303b341aa7309c0dc3898a414)
- [name](../network_service_model_reference/P031_netmidi2_ep_结构体.md#a439571c6a042c28e9002b090e617a391)
- [piid](../network_service_model_reference/P031_netmidi2_ep_结构体.md#adf7a2f4826320c614bcb2cea9b5b214e)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [addr](../network_service_model_reference/P031_netmidi2_ep_结构体.md#a1da1c0bef306386df5d0923cadb04a10)
- [net_sockaddr_in](../network_core_model_reference/P119_net_sockaddr_in_结构体.md)
- [addr4](../network_service_model_reference/P031_netmidi2_ep_结构体.md#a37befb690f98866d52abac009cc237c7)
- [net_sockaddr_in6](../network_core_model_reference/P120_net_sockaddr_in6_结构体.md)
- [addr6](../network_service_model_reference/P031_netmidi2_ep_结构体.md#a5d84716f1ff7f843391ec7faa633154d)
- [zsock_pollfd](../posix_system_model_reference/P030_zsock_pollfd_结构体.md)
- [pollsock](../network_service_model_reference/P031_netmidi2_ep_结构体.md#aba537e498bc6210fd6b718879db711f3)
- [rx_packet_cb](../network_service_model_reference/P031_netmidi2_ep_结构体.md#ac6f1588dc3845a847dcebe81df64c776)
- [midi_ump](../usb/P099_通用MIDI数据包结构.md)
- [peers](../network_service_model_reference/P031_netmidi2_ep_结构体.md#ae73643aad93d83005fb5fa19b8a99ac7)
- [auth_type](../network_service_model_reference/P031_netmidi2_ep_结构体.md#afe9c4413a90f92834fdf06b59fc31363)
- [shared_auth_secret](../network_service_model_reference/P031_netmidi2_ep_结构体.md#a7093bf87340a47a46180e3a720ee94c4)
- [userlist](../network_service_model_reference/P031_netmidi2_ep_结构体.md#a1389cb4e0a73ad7d44143d59c6cbac2e)
- [netmidi2_host_ep_start](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#gabc608c8a74f503f729edfc0506a356cd)
- [netmidi2_broadcast](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga694e4920c2091bfc532ad23e2e2bbd46)
- [netmidi2_send](https://docs.zephyrproject.org/latest/doxygen/html/group__net__midi2.html#ga638d918c5e87be3d7f1013a2ad2810dd)
- [midi.h](https://docs.zephyrproject.org/latest/doxygen/html/midi_8h.html)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [netmidi2_ep::userlist](../network_service_model_reference/P031_netmidi2_ep_结构体.md#a1389cb4e0a73ad7d44143d59c6cbac2e)
- [netmidi2_ep::addr](../network_service_model_reference/P031_netmidi2_ep_结构体.md#a1da1c0bef306386df5d0923cadb04a10)
- [netmidi2_ep::addr4](../network_service_model_reference/P031_netmidi2_ep_结构体.md#a37befb690f98866d52abac009cc237c7)
- [netmidi2_ep::name](../network_service_model_reference/P031_netmidi2_ep_结构体.md#a439571c6a042c28e9002b090e617a391)
- [netmidi2_ep::addr6](../network_service_model_reference/P031_netmidi2_ep_结构体.md#a5d84716f1ff7f843391ec7faa633154d)
- [netmidi2_ep::shared_auth_secret](../network_service_model_reference/P031_netmidi2_ep_结构体.md#a7093bf87340a47a46180e3a720ee94c4)
- [netmidi2_ep::pollsock](../network_service_model_reference/P031_netmidi2_ep_结构体.md#aba537e498bc6210fd6b718879db711f3)
- [netmidi2_ep::rx_packet_cb](../network_service_model_reference/P031_netmidi2_ep_结构体.md#ac6f1588dc3845a847dcebe81df64c776)
- [netmidi2_ep::piid](../network_service_model_reference/P031_netmidi2_ep_结构体.md#adf7a2f4826320c614bcb2cea9b5b214e)
- [netmidi2_ep::peers](../network_service_model_reference/P031_netmidi2_ep_结构体.md#ae73643aad93d83005fb5fa19b8a99ac7)
- [netmidi2_ep::auth_type](../network_service_model_reference/P031_netmidi2_ep_结构体.md#afe9c4413a90f92834fdf06b59fc31363)
- [netmidi2_session::user](../network_service_model_reference/P032_netmidi2_session_结构体.md#a4c295b22b957f2a2317ab8b7c53a5b4f)
- [netmidi2_session::NETMIDI2_SESSION_PENDING_INVITATION](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297a17fd2771abb25775cce6372d1fbddbbc)
- [netmidi2_session::NETMIDI2_SESSION_PENDING_RESET](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297a50d0e9bb5d67e0710cfc7c0503404877)
- [netmidi2_session::NETMIDI2_SESSION_AUTH_REQUIRED](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297a5c0dce1e59eb620eb299eb16c79c3124)
- [netmidi2_session::NETMIDI2_SESSION_NOT_INITIALIZED](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297a85a50751609d84c4151a2393865bebcc)
- [netmidi2_session::NETMIDI2_SESSION_IDLE](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297a978ea2a084813e350383bcfe961ab964)
- [netmidi2_session::NETMIDI2_SESSION_PENDING_BYE](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297ae75b03f14efdd97f0859ff0edb4f7d64)
- [netmidi2_session::NETMIDI2_SESSION_ESTABLISHED](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5b346997cfada6aa8ebee00de696d297af88daf6789f7d887f069e5c11d91b18f)
- [netmidi2_session::tx_buf](../network_service_model_reference/P032_netmidi2_session_结构体.md#a5db865937e4719ed2ee444c6b1edab6a)
- [netmidi2_session::tx_work](../network_service_model_reference/P032_netmidi2_session_结构体.md#a65c740d870d3d0a33e6d8c9150bf6534)
- [netmidi2_session::addr_len](../network_service_model_reference/P032_netmidi2_session_结构体.md#a6d2043af218d266065b90cc8762306a3)
- [netmidi2_session::tx_ump_seq](../network_service_model_reference/P032_netmidi2_session_结构体.md#a6d6d7cc6d97a83125b0422176e1d9a66)
- [netmidi2_session::addr](../network_service_model_reference/P032_netmidi2_session_结构体.md#a7a1d7bd416cc64e254e4a74c766a299c)
- [netmidi2_session::nonce](../network_service_model_reference/P032_netmidi2_session_结构体.md#a8fdb57537d7ebefd4abae5443aed0cb6)
- [netmidi2_session::ep](../network_service_model_reference/P032_netmidi2_session_结构体.md#aa1e41d310563718ad152c21b88b516fe)
- [netmidi2_session::rx_ump_seq](../network_service_model_reference/P032_netmidi2_session_结构体.md#adb2f4b5f0b4a8728085877b1c73939f4)
- [netmidi2_user::name](../network_service_model_reference/P033_netmidi2_user_结构体.md#a71fb204799bd53af65899e46ea771844)
- [netmidi2_user::password](../network_service_model_reference/P033_netmidi2_user_结构体.md#aa334b6f3b82e86e90b6c8c298cf094f6)
- [netmidi2_userlist::n_users](../network_service_model_reference/P034_netmidi2_userlist_结构体.md#a84b04acb7bb17f81f164af79e6b6950d)
- [netmidi2_userlist::users](../network_service_model_reference/P034_netmidi2_userlist_结构体.md#aeca603e7b653c9dd616e32c00783d6dd)

---

[上一章](P527_microchip-smartfusion2-irq.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P529_midi.h_源码浏览.md)
