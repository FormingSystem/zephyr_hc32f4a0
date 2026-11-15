---
id: learning.zephyr-docs.api-source-reference.page-337
title: icmp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/icmp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第337章\_icmp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/icmp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/icmp_8h.html)。

## 337.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00020"></a>
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
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00086"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="foldopen00093"></a>
<a id="l00093"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00115"></a>
<a id="foldopen00119"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00127"></a>
<a id="l00129"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="foldopen00136"></a>
<a id="l00136"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00145"></a>
<a id="l00146"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00153"></a>
<a id="l00154"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="foldopen00235"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="agroup__icmp_html_ga35da387f482e5da0c944bbfa349c3ea2"></a>
<a id="agroup__icmp_html_ga4a1b59fac1b8934a8d0b8f1b981a65cf"></a>
<a id="agroup__icmp_html_ga588b1eecda05d5c275328fee4711b46b"></a>
<a id="agroup__icmp_html_ga6cec9e51d91483c33deae86f24e582ae"></a>
<a id="agroup__icmp_html_ga75f993c1f04d67c63689b5a6e1046d62"></a>
<a id="agroup__icmp_html_ga897d79bdeddb0890d4ef66f51d9505a7"></a>
<a id="agroup__icmp_html_gab90fe71303498c127f1f093d78d16ffa"></a>
<a id="agroup__icmp_html_gad18ca68c320d977abaa3b757c4a1e5b0"></a>
<a id="agroup__icmp_html_gad85b780080117bf3b53c5623f962ea71"></a>
<a id="agroup__ip__4__6_html_ga8b4cfadf1b284e52d6905ca88657b48a"></a>
<a id="agroup__net__core_html_ga8e5393f3bdd85491f221324e637c3896"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="akernel_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="anet__pkt_8h_html"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructnet__icmp__ctx_html"></a>
<a id="astructnet__icmp__ctx_html_a2701c104e363538adfffdf1c15fd21d7"></a>
<a id="astructnet__icmp__ctx_html_a2a718521d0b8c6de45c39fc8b45e47cf"></a>
<a id="astructnet__icmp__ctx_html_a792d11b7dc74b0c064e5471f385028e5"></a>
<a id="astructnet__icmp__ctx_html_a88e1f3dc6118366f37ff5a110fff4b08"></a>
<a id="astructnet__icmp__ctx_html_a8eaa061d7ade479523cfdbcb465f76b2"></a>
<a id="astructnet__icmp__ctx_html_a9da78845a12a69a359087607e11f7e72"></a>
<a id="astructnet__icmp__ctx_html_ae7ccf9c7bbcc89d656d20e9486cf7df5"></a>
<a id="astructnet__icmp__ip__hdr_html"></a>
<a id="astructnet__icmp__ip__hdr_html_a354d2ab876d9cb13f18d4ef905cf16cb"></a>
<a id="astructnet__icmp__ip__hdr_html_a3d0d8b7442611c74a71a72ab1d1c7a90"></a>
<a id="astructnet__icmp__ip__hdr_html_ac993b71afdd637dba048ba5038d489c8"></a>
<a id="astructnet__icmp__offload_html"></a>
<a id="astructnet__icmp__offload_html_aad5c9913e8bf68a7453bc773c5784772"></a>
<a id="astructnet__icmp__offload_html_ae28f8f6a0e15271b1f00b10abecdfc3e"></a>
<a id="astructnet__icmp__offload_html_ae31036c45fac89b321fe2c62c06be0b3"></a>
<a id="astructnet__icmp__offload_html_aeffe11b4701e58532e44b4cff37be680"></a>
<a id="astructnet__icmp__ping__params_html"></a>
<a id="astructnet__icmp__ping__params_html_a138d6de6072ebbf3ae454eb3ee28b138"></a>
<a id="astructnet__icmp__ping__params_html_a342b75123a32e35f91bda3e11601598b"></a>
<a id="astructnet__icmp__ping__params_html_a3756461b95ce1b7fde9d59819de10d85"></a>
<a id="astructnet__icmp__ping__params_html_a3a9abdb27bfb94ca6515e280bf6bee3c"></a>
<a id="astructnet__icmp__ping__params_html_aaf5a9493b5d98f72bb27758fd24c64ec"></a>
<a id="astructnet__icmp__ping__params_html_ac2247bc63eea000200429f0f441031bf"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnet__sockaddr_html"></a>

```c
/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_ICMP_H_
#define ZEPHYR_INCLUDE_NET_ICMP_H_

#include <stddef.h>

#include <zephyr/kernel.h>
#include <zephyr/types.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/net_pkt.h>

#ifdef __cplusplus
extern "C" {
#endif

#define NET_ICMPV4_ECHO_REQUEST 8
#define NET_ICMPV4_ECHO_REPLY   0
#define NET_ICMPV6_ECHO_REQUEST 128
#define NET_ICMPV6_ECHO_REPLY   129

struct net_icmp_ctx;
struct net_icmp_ip_hdr;
struct net_icmp_ping_params;

typedef enum net_verdict (*net_icmp_handler_t)(struct net_icmp_ctx *ctx,
                                               struct net_pkt *pkt,
                                               struct net_icmp_ip_hdr *ip_hdr,
                                               struct net_icmp_hdr *icmp_hdr,
                                               void *user_data);

typedef int (*net_icmp_offload_ping_handler_t)(struct net_icmp_ctx *ctx,
                                               struct net_if *iface,
                                               struct net_sockaddr *dst,
                                               struct net_icmp_ping_params *params,
                                               void *user_data);

struct net_icmp_ctx {
        sys_snode_t node;

        net_icmp_handler_t handler;

        struct net_if *iface;

        void *user_data;

        uint8_t family;

        uint8_t type;

        uint8_t code;
};

struct net_icmp_ip_hdr {
        union {
                struct net_ipv4_hdr *ipv4;

                struct net_ipv6_hdr *ipv6;
        };

        net_sa_family_t family;
};

struct net_icmp_ping_params {
        uint16_t identifier;

        uint16_t sequence;

        uint8_t tc_tos;

        int priority;

        const void *data;

        size_t data_size;
};

int net_icmp_init_ctx(struct net_icmp_ctx *ctx, uint8_t family, uint8_t type,
                      uint8_t code, net_icmp_handler_t handler);

int net_icmp_cleanup_ctx(struct net_icmp_ctx *ctx);

int net_icmp_send_echo_request(struct net_icmp_ctx *ctx,
                               struct net_if *iface,
                               struct net_sockaddr *dst,
                               struct net_icmp_ping_params *params,
                               void *user_data);

int net_icmp_send_echo_request_no_wait(struct net_icmp_ctx *ctx,
                                       struct net_if *iface,
                                       struct net_sockaddr *dst,
                                       struct net_icmp_ping_params *params,
                                       void *user_data);

struct net_icmp_offload {
        sys_snode_t node;

        net_icmp_handler_t handler;

        net_icmp_offload_ping_handler_t ping_handler;

        struct net_if *iface;
};

int net_icmp_register_offload_ping(struct net_icmp_offload *ctx,
                                   struct net_if *iface,
                                   net_icmp_offload_ping_handler_t ping_handler);

int net_icmp_unregister_offload_ping(struct net_icmp_offload *ctx);

int net_icmp_get_offload_rsp_handler(struct net_icmp_offload *ctx,
                                     net_icmp_handler_t *resp_handler);

#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_ICMP_H */

```

## 337.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 298 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_ICMP_H`。

## 337.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/icmp_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [net_icmp_ctx](../network_core_model_reference/P075_net_icmp_ctx_结构体.md)
- [net_icmp_ip_hdr](../network_core_model_reference/P076_net_icmp_ip_hdr_结构体.md)
- [net_icmp_ping_params](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md)
- [net_verdict](https://docs.zephyrproject.org/latest/doxygen/html/group__net__core.html#ga8e5393f3bdd85491f221324e637c3896)
- [net_icmp_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga35da387f482e5da0c944bbfa349c3ea2)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_icmp_offload_ping_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gad85b780080117bf3b53c5623f962ea71)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#a792d11b7dc74b0c064e5471f385028e5)
- [handler](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#a9da78845a12a69a359087607e11f7e72)
- [iface](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#a88e1f3dc6118366f37ff5a110fff4b08)
- [user_data](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#a2a718521d0b8c6de45c39fc8b45e47cf)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [family](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#a2701c104e363538adfffdf1c15fd21d7)
- [type](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#ae7ccf9c7bbcc89d656d20e9486cf7df5)
- [code](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#a8eaa061d7ade479523cfdbcb465f76b2)
- [ipv4](../network_core_model_reference/P076_net_icmp_ip_hdr_结构体.md#a3d0d8b7442611c74a71a72ab1d1c7a90)
- [ipv6](../network_core_model_reference/P076_net_icmp_ip_hdr_结构体.md#ac993b71afdd637dba048ba5038d489c8)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [family](../network_core_model_reference/P076_net_icmp_ip_hdr_结构体.md#a354d2ab876d9cb13f18d4ef905cf16cb)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [identifier](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md#a138d6de6072ebbf3ae454eb3ee28b138)
- [sequence](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md#a3756461b95ce1b7fde9d59819de10d85)
- [tc_tos](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md#aaf5a9493b5d98f72bb27758fd24c64ec)
- [priority](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md#a3a9abdb27bfb94ca6515e280bf6bee3c)
- [data](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md#ac2247bc63eea000200429f0f441031bf)
- [data_size](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md#a342b75123a32e35f91bda3e11601598b)
- [net_icmp_init_ctx](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga897d79bdeddb0890d4ef66f51d9505a7)
- [net_icmp_cleanup_ctx](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gab90fe71303498c127f1f093d78d16ffa)
- [net_icmp_send_echo_request](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga588b1eecda05d5c275328fee4711b46b)
- [net_icmp_send_echo_request_no_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga4a1b59fac1b8934a8d0b8f1b981a65cf)
- [net_icmp_offload](../network_core_model_reference/P077_net_icmp_offload_结构体.md)
- [node](../network_core_model_reference/P077_net_icmp_offload_结构体.md#ae31036c45fac89b321fe2c62c06be0b3)
- [handler](../network_core_model_reference/P077_net_icmp_offload_结构体.md#aad5c9913e8bf68a7453bc773c5784772)
- [ping_handler](../network_core_model_reference/P077_net_icmp_offload_结构体.md#ae28f8f6a0e15271b1f00b10abecdfc3e)
- [iface](../network_core_model_reference/P077_net_icmp_offload_结构体.md#aeffe11b4701e58532e44b4cff37be680)
- [net_icmp_register_offload_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga6cec9e51d91483c33deae86f24e582ae)
- [net_icmp_unregister_offload_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#ga75f993c1f04d67c63689b5a6e1046d62)
- [net_icmp_get_offload_rsp_handler](https://docs.zephyrproject.org/latest/doxygen/html/group__icmp.html#gad18ca68c320d977abaa3b757c4a1e5b0)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [net_pkt.h](https://docs.zephyrproject.org/latest/doxygen/html/net__pkt_8h.html)
- [net_icmp_ctx::family](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#a2701c104e363538adfffdf1c15fd21d7)
- [net_icmp_ctx::user_data](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#a2a718521d0b8c6de45c39fc8b45e47cf)
- [net_icmp_ctx::node](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#a792d11b7dc74b0c064e5471f385028e5)
- [net_icmp_ctx::iface](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#a88e1f3dc6118366f37ff5a110fff4b08)
- [net_icmp_ctx::code](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#a8eaa061d7ade479523cfdbcb465f76b2)
- [net_icmp_ctx::handler](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#a9da78845a12a69a359087607e11f7e72)
- [net_icmp_ctx::type](../network_core_model_reference/P075_net_icmp_ctx_结构体.md#ae7ccf9c7bbcc89d656d20e9486cf7df5)
- [net_icmp_ip_hdr::family](../network_core_model_reference/P076_net_icmp_ip_hdr_结构体.md#a354d2ab876d9cb13f18d4ef905cf16cb)
- [net_icmp_ip_hdr::ipv4](../network_core_model_reference/P076_net_icmp_ip_hdr_结构体.md#a3d0d8b7442611c74a71a72ab1d1c7a90)
- [net_icmp_ip_hdr::ipv6](../network_core_model_reference/P076_net_icmp_ip_hdr_结构体.md#ac993b71afdd637dba048ba5038d489c8)
- [net_icmp_offload::handler](../network_core_model_reference/P077_net_icmp_offload_结构体.md#aad5c9913e8bf68a7453bc773c5784772)
- [net_icmp_offload::ping_handler](../network_core_model_reference/P077_net_icmp_offload_结构体.md#ae28f8f6a0e15271b1f00b10abecdfc3e)
- [net_icmp_offload::node](../network_core_model_reference/P077_net_icmp_offload_结构体.md#ae31036c45fac89b321fe2c62c06be0b3)
- [net_icmp_offload::iface](../network_core_model_reference/P077_net_icmp_offload_结构体.md#aeffe11b4701e58532e44b4cff37be680)
- [net_icmp_ping_params::identifier](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md#a138d6de6072ebbf3ae454eb3ee28b138)
- [net_icmp_ping_params::data_size](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md#a342b75123a32e35f91bda3e11601598b)
- [net_icmp_ping_params::sequence](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md#a3756461b95ce1b7fde9d59819de10d85)
- [net_icmp_ping_params::priority](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md#a3a9abdb27bfb94ca6515e280bf6bee3c)
- [net_icmp_ping_params::tc_tos](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md#aaf5a9493b5d98f72bb27758fd24c64ec)
- [net_icmp_ping_params::data](../network_core_model_reference/P078_net_icmp_ping_params_结构体.md#ac2247bc63eea000200429f0f441031bf)

---

[上一章](P336_icm45686.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P338_ieee802154_frame.h_源码浏览.md)
