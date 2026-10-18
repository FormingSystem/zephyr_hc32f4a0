---
id: learning.zephyr-docs.api-source-reference.page-577
title: net_offload.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__offload_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第577章\_net\_offload.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__offload_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__offload_8h.html)。

## 577.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
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
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00052"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="l00100"></a>
<a id="l00101"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
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
<a id="l00198"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00201"></a>
<a id="l00202"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00210"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00300"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00335"></a>
<a id="l00336"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00339"></a>
<a id="l00340"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00377"></a>
<a id="l00378"></a>
<a id="l00379"></a>
<a id="l00380"></a>
<a id="l00381"></a>
<a id="l00382"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00385"></a>
<a id="l00386"></a>
<a id="l00387"></a>
<a id="l00388"></a>
<a id="l00389"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00433"></a>
<a id="l00434"></a>
<a id="l00435"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00443"></a>
<a id="l00444"></a>
<a id="l00445"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00461"></a>
<a id="l00462"></a>
<a id="l00463"></a>
<a id="l00464"></a>
<a id="l00465"></a>
<a id="l00466"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="l00474"></a>
<a id="l00476"></a>
<a id="l00477"></a>
<a id="l00478"></a>
<a id="l00479"></a>
<a id="l00480"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="l00488"></a>
<a id="l00489"></a>
<a id="l00490"></a>
<a id="l00491"></a>
<a id="l00492"></a>
<a id="l00493"></a>
<a id="l00494"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="l00502"></a>
<a id="l00503"></a>
<a id="l00504"></a>
<a id="l00505"></a>
<a id="l00506"></a>
<a id="l00507"></a>
<a id="l00508"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="l00516"></a>
<a id="l00517"></a>
<a id="l00518"></a>
<a id="l00519"></a>
<a id="l00520"></a>
<a id="l00521"></a>
<a id="l00522"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="l00530"></a>
<a id="l00531"></a>
<a id="l00532"></a>
<a id="l00533"></a>
<a id="l00534"></a>
<a id="l00535"></a>
<a id="l00536"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="l00544"></a>
<a id="l00545"></a>
<a id="l00546"></a>
<a id="l00547"></a>
<a id="l00548"></a>
<a id="l00549"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00557"></a>
<a id="l00558"></a>
<a id="l00559"></a>
<a id="l00560"></a>
<a id="l00561"></a>
<a id="l00562"></a>
<a id="l00563"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="agroup__clock__apis_html_ga0bb4b83f0222193b21a8910311bab0ca"></a>
<a id="agroup__clock__apis_html_ga3d9541cfe2e8395af66d186efa77362f"></a>
<a id="agroup__clock__apis_html_ga9abf00b34e16ab7ad0883603b6778b1b"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="agroup__ip__4__6_html_ga8b4cfadf1b284e52d6905ca88657b48a"></a>
<a id="agroup__ip__4__6_html_gaaab4268707dbe08348b98fb028e7aa5c"></a>
<a id="agroup__ip__4__6_html_gaf06819bf427cc58be1229b27b373ca31"></a>
<a id="agroup__net__context_html_ga120ae8d4ff788ab21b19c11ed1738a71"></a>
<a id="agroup__net__context_html_gab3caccfe9fa1bc7ce0e4654192a5de93"></a>
<a id="agroup__net__context_html_gaf05114d2edc8b5fb485fd37f3d0821ba"></a>
<a id="agroup__net__context_html_gafa485a6fae8237dd7e6856f4567b2317"></a>
<a id="agroup__net__if_html_ga520939e94620ca75475a71f153df6d4a"></a>
<a id="agroup__timeutil__unit__apis_html_ga6ecf0ab60ac29c60d6a6b66a45c86664"></a>
<a id="anet__buf_8h_html"></a>
<a id="anet__context_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="aposix_2sys_2socket_8h_html_a05b4e957a092db3e68281988ceb32df8"></a>
<a id="aposix_2sys_2socket_8h_html_a16485de18b1ec93572e5d74b4a04e42f"></a>
<a id="aposix_2sys_2socket_8h_html_a66e3de379c18201b21c889035ec54864"></a>
<a id="aposix_2sys_2socket_8h_html_a7005ffbeeff92be5394ff3244da79028"></a>
<a id="aposix_2sys_2socket_8h_html_a90f0aa598d0f4ab4ea99ecf289a6a7fb"></a>
<a id="aposix_2sys_2socket_8h_html_ac223969ed767c313123d06547db45ff8"></a>
<a id="aposix_2sys_2socket_8h_html_adee01662b0cf762a014efd87ab811276"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructk__timeout__t_html_a492605d3a8c76f0ce2ef129b9f4d40fa"></a>
<a id="astructnet__context_html"></a>
<a id="astructnet__context_html_ad71d151e1e9e35b934949482066f1947"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__pkt_html"></a>
<a id="astructnet__sockaddr_html"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_NET_OFFLOAD_H_
#define ZEPHYR_INCLUDE_NET_NET_OFFLOAD_H_


#include <zephyr/net_buf.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_context.h>

#ifdef __cplusplus
extern "C" {
#endif

#if defined(CONFIG_NET_OFFLOAD)


static inline int32_t timeout_to_int32(k_timeout_t timeout)
{
        if (K_TIMEOUT_EQ(timeout, K_NO_WAIT)) {
                return 0;
        } else if (K_TIMEOUT_EQ(timeout, K_FOREVER)) {
                return -1;
        } else {
                return k_ticks_to_ms_floor32(timeout.ticks);
        }
}


struct net_offload {
        int (*get)(net_sa_family_t family,
                   enum net_sock_type type,
                   enum net_ip_protocol ip_proto,
                   struct net_context **context);

        int (*bind)(struct net_context *context,
                    const struct net_sockaddr *addr,
                    net_socklen_t addrlen);

        int (*listen)(struct net_context *context, int backlog);

        int (*connect)(struct net_context *context,
                       const struct net_sockaddr *addr,
                       net_socklen_t addrlen,
                       net_context_connect_cb_t cb,
                       int32_t timeout,
                       void *user_data);

        int (*accept)(struct net_context *context,
                      net_tcp_accept_cb_t cb,
                      int32_t timeout,
                      void *user_data);

        int (*send)(struct net_pkt *pkt,
                    net_context_send_cb_t cb,
                    int32_t timeout,
                    void *user_data);

        int (*sendto)(struct net_pkt *pkt,
                      const struct net_sockaddr *dst_addr,
                      net_socklen_t addrlen,
                      net_context_send_cb_t cb,
                      int32_t timeout,
                      void *user_data);

        int (*recv)(struct net_context *context,
                    net_context_recv_cb_t cb,
                    int32_t timeout,
                    void *user_data);

        int (*put)(struct net_context *context);
};

static inline int net_offload_get(struct net_if *iface,
                                  net_sa_family_t family,
                                  enum net_sock_type type,
                                  enum net_ip_protocol ip_proto,
                                  struct net_context **context)
{
        struct net_offload *offload = net_if_offload(iface);

        NET_ASSERT(iface);
        NET_ASSERT(offload);
        NET_ASSERT(offload->get);

        return offload->get(family, type, ip_proto, context);
}

static inline int net_offload_bind(struct net_if *iface,
                                   struct net_context *context,
                                   const struct net_sockaddr *addr,
                                   net_socklen_t addrlen)
{
        struct net_offload *offload = net_if_offload(iface);

        NET_ASSERT(iface);
        NET_ASSERT(offload);
        NET_ASSERT(offload->bind);

        return offload->bind(context, addr, addrlen);
}

static inline int net_offload_listen(struct net_if *iface,
                                     struct net_context *context,
                                     int backlog)
{
        struct net_offload *offload = net_if_offload(iface);

        NET_ASSERT(iface);
        NET_ASSERT(offload);
        NET_ASSERT(offload->listen);

        return offload->listen(context, backlog);
}

static inline int net_offload_connect(struct net_if *iface,
                                      struct net_context *context,
                                      const struct net_sockaddr *addr,
                                      net_socklen_t addrlen,
                                      net_context_connect_cb_t cb,
                                      k_timeout_t timeout,
                                      void *user_data)
{
        struct net_offload *offload = net_if_offload(iface);

        NET_ASSERT(iface);
        NET_ASSERT(offload);
        NET_ASSERT(offload->connect);

        return offload->connect(
                context, addr, addrlen, cb,
                timeout_to_int32(timeout),
                user_data);
}

static inline int net_offload_accept(struct net_if *iface,
                                     struct net_context *context,
                                     net_tcp_accept_cb_t cb,
                                     k_timeout_t timeout,
                                     void *user_data)
{
        struct net_offload *offload = net_if_offload(iface);

        NET_ASSERT(iface);
        NET_ASSERT(offload);
        NET_ASSERT(offload->accept);

        return offload->accept(
                context, cb,
                timeout_to_int32(timeout),
                user_data);
}

static inline int net_offload_send(struct net_if *iface,
                                   struct net_pkt *pkt,
                                   net_context_send_cb_t cb,
                                   k_timeout_t timeout,
                                   void *user_data)
{
        struct net_offload *offload = net_if_offload(iface);

        NET_ASSERT(iface);
        NET_ASSERT(offload);
        NET_ASSERT(offload->send);

        return offload->send(
                pkt, cb,
                timeout_to_int32(timeout),
                user_data);
}

static inline int net_offload_sendto(struct net_if *iface,
                                     struct net_pkt *pkt,
                                     const struct net_sockaddr *dst_addr,
                                     net_socklen_t addrlen,
                                     net_context_send_cb_t cb,
                                     k_timeout_t timeout,
                                     void *user_data)
{
        struct net_offload *offload = net_if_offload(iface);

        NET_ASSERT(iface);
        NET_ASSERT(offload);
        NET_ASSERT(offload->sendto);

        return offload->sendto(
                pkt, dst_addr, addrlen, cb,
                timeout_to_int32(timeout),
                user_data);
}

static inline int net_offload_recv(struct net_if *iface,
                                   struct net_context *context,
                                   net_context_recv_cb_t cb,
                                   k_timeout_t timeout,
                                   void *user_data)
{
        struct net_offload *offload = net_if_offload(iface);

        NET_ASSERT(iface);
        NET_ASSERT(offload);
        NET_ASSERT(offload->recv);

        return offload->recv(
                context, cb,
                timeout_to_int32(timeout),
                user_data);
}

static inline int net_offload_put(struct net_if *iface,
                                  struct net_context *context)
{
        struct net_offload *offload = net_if_offload(iface);

        NET_ASSERT(iface);
        NET_ASSERT(offload);
        NET_ASSERT(offload->put);

        return offload->put(context);
}

#else


static inline int net_offload_get(struct net_if *iface,
                                  net_sa_family_t family,
                                  enum net_sock_type type,
                                  enum net_ip_protocol ip_proto,
                                  struct net_context **context)
{
        return 0;
}

static inline int net_offload_bind(struct net_if *iface,
                                   struct net_context *context,
                                   const struct net_sockaddr *addr,
                                   net_socklen_t addrlen)
{
        return 0;
}

static inline int net_offload_listen(struct net_if *iface,
                                     struct net_context *context,
                                     int backlog)
{
        return 0;
}

static inline int net_offload_connect(struct net_if *iface,
                                      struct net_context *context,
                                      const struct net_sockaddr *addr,
                                      net_socklen_t addrlen,
                                      net_context_connect_cb_t cb,
                                      k_timeout_t timeout,
                                      void *user_data)
{
        return 0;
}

static inline int net_offload_accept(struct net_if *iface,
                                     struct net_context *context,
                                     net_tcp_accept_cb_t cb,
                                     k_timeout_t timeout,
                                     void *user_data)
{
        return 0;
}

static inline int net_offload_send(struct net_if *iface,
                                   struct net_pkt *pkt,
                                   net_context_send_cb_t cb,
                                   k_timeout_t timeout,
                                   void *user_data)
{
        return 0;
}

static inline int net_offload_sendto(struct net_if *iface,
                                     struct net_pkt *pkt,
                                     const struct net_sockaddr *dst_addr,
                                     net_socklen_t addrlen,
                                     net_context_send_cb_t cb,
                                     k_timeout_t timeout,
                                     void *user_data)
{
        return 0;
}

static inline int net_offload_recv(struct net_if *iface,
                                   struct net_context *context,
                                   net_context_recv_cb_t cb,
                                   k_timeout_t timeout,
                                   void *user_data)
{
        return 0;
}

static inline int net_offload_put(struct net_if *iface,
                                  struct net_context *context)
{
        return 0;
}


#endif /* CONFIG_NET_OFFLOAD */

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_NET_OFFLOAD_H_ */
```

## 577.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 558 行

条件编译配置（Configuration）标记：`CONFIG_NET_OFFLOAD`。

### 注释 3：原第 568 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_OFFLOAD_H_`。

## 577.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__offload_8h.html)
- [zephyr/net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_context.h](https://docs.zephyrproject.org/latest/doxygen/html/net__context_8h.html)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [K_TIMEOUT_EQ](../timer_reference/P086_系统时钟公共接口.md#ga9abf00b34e16ab7ad0883603b6778b1b)
- [K_NO_WAIT](../timer_reference/P086_系统时钟公共接口.md#ga3d9541cfe2e8395af66d186efa77362f)
- [K_FOREVER](../timer_reference/P086_系统时钟公共接口.md#ga0bb4b83f0222193b21a8910311bab0ca)
- [k_ticks_to_ms_floor32](../timeutil_reference/P007_时间单位辅助接口.md#ga6ecf0ab60ac29c60d6a6b66a45c86664)
- [ticks](../timer_reference/P087_内核超时类型.md#a492605d3a8c76f0ce2ef129b9f4d40fa)
- [net_sa_family_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga8b4cfadf1b284e52d6905ca88657b48a)
- [net_sock_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaaab4268707dbe08348b98fb028e7aa5c)
- [net_ip_protocol](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#gaf06819bf427cc58be1229b27b373ca31)
- [bind](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a05b4e957a092db3e68281988ceb32df8)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [listen](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a7005ffbeeff92be5394ff3244da79028)
- [connect](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a90f0aa598d0f4ab4ea99ecf289a6a7fb)
- [net_context_connect_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#ga120ae8d4ff788ab21b19c11ed1738a71)
- [accept](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a66e3de379c18201b21c889035ec54864)
- [net_tcp_accept_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gaf05114d2edc8b5fb485fd37f3d0821ba)
- [send](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#a16485de18b1ec93572e5d74b4a04e42f)
- [net_context_send_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gab3caccfe9fa1bc7ce0e4654192a5de93)
- [sendto](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#ac223969ed767c313123d06547db45ff8)
- [recv](https://docs.zephyrproject.org/latest/doxygen/html/posix_2sys_2socket_8h.html#adee01662b0cf762a014efd87ab811276)
- [net_context_recv_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__context.html#gafa485a6fae8237dd7e6856f4567b2317)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [iface](../network_core_model_reference/P055_net_context_结构体.md#ad71d151e1e9e35b934949482066f1947)
- [net_context](../network_core_model_reference/P055_net_context_结构体.md)
- [net_if_offload](https://docs.zephyrproject.org/latest/doxygen/html/group__net__if.html#ga520939e94620ca75475a71f153df6d4a)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_pkt](../network_core_model_reference/P114_net_pkt_结构体.md)
- [net_buf.h](https://docs.zephyrproject.org/latest/doxygen/html/net__buf_8h.html)
- [net_context.h](https://docs.zephyrproject.org/latest/doxygen/html/net__context_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [k_timeout_t::ticks](../timer_reference/P087_内核超时类型.md#a492605d3a8c76f0ce2ef129b9f4d40fa)
- [net_context::iface](../network_core_model_reference/P055_net_context_结构体.md#ad71d151e1e9e35b934949482066f1947)

---

[上一章](P576_net_linkaddr.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P578_netdb.h_源码浏览.md)
