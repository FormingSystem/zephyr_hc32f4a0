---
id: learning.zephyr-docs.api-source-timing-sensor-reference.page-9
title: net_mgmt.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第9章\_net\_mgmt.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)。

## 9.1\_原始可见代码（Source Code）

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
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00017"></a>
<a id="l00018"></a>
<a id="l00019"></a>
<a id="l00020"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00047"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="foldopen00071"></a>
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
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="foldopen00122"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00134"></a>
<a id="foldopen00141"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="foldopen00164"></a>
<a id="l00164"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00170"></a>
<a id="l00173"></a>
<a id="l00177"></a>
<a id="l00178"></a>
<a id="l00179"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00183"></a>
<a id="l00184"></a>
<a id="l00190"></a>
<a id="l00199"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00206"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00231"></a>
<a id="l00233"></a>
<a id="foldopen00247"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00252"></a>
<a id="l00253"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="foldopen00262"></a>
<a id="l00262"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00268"></a>
<a id="l00269"></a>
<a id="l00270"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00280"></a>
<a id="l00281"></a>
<a id="l00282"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00292"></a>
<a id="l00293"></a>
<a id="l00294"></a>
<a id="l00295"></a>
<a id="l00296"></a>
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
<a id="l00320"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="foldopen00330"></a>
<a id="l00330"></a>
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
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00372"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00375"></a>
<a id="l00376"></a>
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
<a id="l00408"></a>
<a id="l00409"></a>
<a id="l00410"></a>
<a id="l00411"></a>
<a id="l00412"></a>
<a id="l00413"></a>
<a id="l00414"></a>
<a id="l00415"></a>
<a id="l00416"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00419"></a>
<a id="l00420"></a>
<a id="l00421"></a>
<a id="l00422"></a>
<a id="l00423"></a>
<a id="l00424"></a>
<a id="l00425"></a>
<a id="l00426"></a>
<a id="l00427"></a>
<a id="l00428"></a>
<a id="l00429"></a>
<a id="l00430"></a>
<a id="l00431"></a>
<a id="l00432"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="l00440"></a>
<a id="l00441"></a>
<a id="l00442"></a>
<a id="l00446"></a>
<a id="l00447"></a>
<a id="l00448"></a>
<a id="l00449"></a>
<a id="l00450"></a>
<a id="l00451"></a>
<a id="agroup__net__mgmt_html_ga2e83a5a769ac52c846f255e23aea84d2"></a>
<a id="agroup__net__mgmt_html_ga3ab114106df41144c0fae8e6faad12cb"></a>
<a id="agroup__net__mgmt_html_ga4960bfb01ecd891da72c57f17587f946"></a>
<a id="agroup__net__mgmt_html_ga4e42b6d16b863ca374d032682e8c11fb"></a>
<a id="agroup__net__mgmt_html_ga5e6911455b9ab9f4c82780001459461a"></a>
<a id="agroup__net__mgmt_html_ga6415ec1e2e7f477c8976022ac33b0654"></a>
<a id="agroup__net__mgmt_html_ga7137c77c55ee2609941c88db79e22d1a"></a>
<a id="agroup__net__mgmt_html_ga78b9302193bd0c5cc35d81d298a5eb6b"></a>
<a id="agroup__net__mgmt_html_gaab4fe2e9ea0657bf91fb1910af6729cc"></a>
<a id="agroup__net__mgmt_html_gabf710692e596a2d98f37b82da884a82a"></a>
<a id="agroup__net__mgmt_html_gae53f5bbc973b0f414107eca75ac0c26f"></a>
<a id="agroup__net__mgmt_html_gaf3773f8e945c4ec05b2fab46cd8b1881"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa06935e2c46523b1a3f414f4c981992fc"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa10876d890aac72553ab69c0964bef48a"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa25c33c6faa9d22f4ac5b70049bb4bbd2"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa2e23e545f7d78775adb5271f7bf42518"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa3206e13330183c74d20e89407e11c7cd"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa3ab69a93464d5fa0d5be9ac9f3757cb6"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa4893c212a3026909dcb8663abbdf2b2b"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa4e57a620f5778d346984398c0e786977"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa52b23f5afbf235bef6bc2aeea69271c1"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa5701861bfb5fae92e8c7b08ea02f61a7"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa7f2f4d110d3003974bd0da0154c2d789"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa8f1f092ecdfcf341458e7389cee3ace8"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aa997785b24761b410a1d33788c46f90b1"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aaa335a8c82c6d7614337e3501a69aa1d4"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aab60d69e5ee62cb0212b1e424d7847b4e"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aabf1c9ef98fb7237ba1591108c67bf1d7"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aac767c8da93a6d0f5a53e64cbfdf94fca"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aaef64c0749996046b313ebf366b3eab75"></a>
<a id="agroup__net__mgmt_html_gga5e6911455b9ab9f4c82780001459461aafd0569a3f3cde9e892751a84b74836b4"></a>
<a id="agroup__single-linked-list__apis_html_ga69bf43aad81e3ee2d55250c59b857493"></a>
<a id="anet__core_8h_html"></a>
<a id="anet__event_8h_html"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astructk__sem_html"></a>
<a id="astructk__timeout__t_html"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__mgmt__event__callback_html"></a>
<a id="astructnet__mgmt__event__callback_html_a05a4f445731f9f72209a652f2653e1ea"></a>
<a id="astructnet__mgmt__event__callback_html_a555d868d6a0d6ecb04d09607fab06b79"></a>
<a id="astructnet__mgmt__event__callback_html_a7403d98fe528c492a4b1b449b43c10d3"></a>
<a id="astructnet__mgmt__event__callback_html_a99e3174c1052488877b3db6349de61e8"></a>
<a id="astructnet__mgmt__event__callback_html_ada57aabc8acc3e9be93fb2726321f1b2"></a>
<a id="asys_2iterable__sections_8h_html"></a>

```c
/*
 * Copyright (c) 2016 Intel Corporation.
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_NET_MGMT_H_
#define ZEPHYR_INCLUDE_NET_NET_MGMT_H_

#include <zephyr/sys/__assert.h>
#include <zephyr/net/net_core.h>
#include <zephyr/sys/iterable_sections.h>

#ifdef __cplusplus
extern "C" {
#endif


struct net_if;

#define NET_MGMT_EVENT_MASK        GENMASK64(63, 63) /* 0x8000000000000000 */
#define NET_MGMT_ON_IFACE_MASK     GENMASK64(62, 62) /* 0x4000000000000000 */
#define NET_MGMT_LAYER_MASK        GENMASK64(61, 60) /* 0x3000000000000000 */
#define NET_MGMT_SYNC_EVENT_MASK   GENMASK64(59, 59) /* 0x0800000000000000 */
#define NET_MGMT_LAYER_CODE_MASK   GENMASK64(58, 52) /* 0x07F0000000000000 */
#define NET_MGMT_COMMAND_MASK      GENMASK64(51, 0)  /* 0x000FFFFFFFFFFFFF */

#define NET_MGMT_MAX_COMMANDS 52 /* TODO: figure out the value from mask */

#define NET_MGMT_EVENT_BIT         BIT64(63)
#define NET_MGMT_IFACE_BIT         BIT64(62)
#define NET_MGMT_SYNC_EVENT_BIT    BIT64(59)

#define NET_MGMT_LAYER(_layer)     FIELD_PREP(NET_MGMT_LAYER_MASK, (_layer))
#define NET_MGMT_LAYER_CODE(_code) FIELD_PREP(NET_MGMT_LAYER_CODE_MASK, (_code))

#define NET_MGMT_EVENT(mgmt_request)             FIELD_GET(NET_MGMT_EVENT_MASK, mgmt_request)
#define NET_MGMT_ON_IFACE(mgmt_request)          FIELD_GET(NET_MGMT_ON_IFACE_MASK, mgmt_request)
#define NET_MGMT_EVENT_SYNCHRONOUS(mgmt_request) FIELD_GET(NET_MGMT_SYNC_EVENT_MASK, mgmt_request)
#define NET_MGMT_GET_LAYER(mgmt_request)         FIELD_GET(NET_MGMT_LAYER_MASK, mgmt_request)
#define NET_MGMT_GET_LAYER_CODE(mgmt_request)    FIELD_GET(NET_MGMT_LAYER_CODE_MASK, mgmt_request)
#define NET_MGMT_GET_COMMAND(mgmt_request)       FIELD_GET(NET_MGMT_COMMAND_MASK, mgmt_request)

#define NET_MGMT_CMD(cmd) cmd = BIT64(cmd ##_VAL)

/* Useful generic definitions */
#define NET_MGMT_LAYER_L2               1
#define NET_MGMT_LAYER_L3               2
#define NET_MGMT_LAYER_L4               3


enum net_mgmt_layer_code {
        NET_MGMT_LAYER_CODE_UNKNOWN    = 0x00,
        NET_MGMT_LAYER_CODE_IFACE      = 0x01,
        NET_MGMT_LAYER_CODE_CONN       = 0x02,
        NET_MGMT_LAYER_CODE_IPV4       = 0x03,
        NET_MGMT_LAYER_CODE_IPV6       = 0x04,
        NET_MGMT_LAYER_CODE_L4         = 0x05,
        NET_MGMT_LAYER_CODE_COAP       = 0x06,
        NET_MGMT_LAYER_CODE_STATS      = 0x07,
        NET_MGMT_LAYER_CODE_HOSTAP     = 0x08,
        NET_MGMT_LAYER_CODE_ETHERNET   = 0x09,
        NET_MGMT_LAYER_CODE_IEEE802514 = 0x0A,
        NET_MGMT_LAYER_CODE_PPP        = 0x0B,
        NET_MGMT_LAYER_CODE_VIRTUAL    = 0x0C,
        NET_MGMT_LAYER_CODE_WIFI       = 0x0D,
        NET_MGMT_LAYER_CODE_PACKET     = 0x0E,

        /* Out of tree code can use the following userX layer codes */
        NET_MGMT_LAYER_CODE_USER3      = 0x7C,
        NET_MGMT_LAYER_CODE_USER2      = 0x7D,
        NET_MGMT_LAYER_CODE_USER1      = 0x7E,

        /* Reserved layer code for future use */
        NET_MGMT_LAYER_CODE_RESERVED   = 0x7F
};

#include <zephyr/net/net_event.h>

typedef int (*net_mgmt_request_handler_t)(uint64_t mgmt_request,
                                          struct net_if *iface,
                                          void *data, size_t len);

#define net_mgmt(_mgmt_request, _iface, _data, _len)                    \
        net_mgmt_##_mgmt_request(_mgmt_request, _iface, _data, _len)

#define NET_MGMT_DEFINE_REQUEST_HANDLER(_mgmt_request)                  \
        extern int net_mgmt_##_mgmt_request(uint64_t mgmt_request,      \
                                            struct net_if *iface,       \
                                            void *data, size_t len)

#define NET_MGMT_REGISTER_REQUEST_HANDLER(_mgmt_request, _func) \
        FUNC_ALIAS(_func, net_mgmt_##_mgmt_request, int)

struct net_mgmt_event_callback;

typedef void (*net_mgmt_event_handler_t)(struct net_mgmt_event_callback *cb,
                                         uint64_t mgmt_event,
                                         struct net_if *iface);

struct net_mgmt_event_callback {
        sys_snode_t node;

        union {
                net_mgmt_event_handler_t handler;
                struct k_sem *sync_call;
        };

#ifdef CONFIG_NET_MGMT_EVENT_INFO
        const void *info;
        size_t info_length;
#endif

        union {
                uint64_t event_mask;
                uint64_t raised_event;
        };
};

typedef void (*net_mgmt_event_static_handler_t)(uint64_t mgmt_event,
                                                struct net_if *iface,
                                                void *info, size_t info_length,
                                                void *user_data);


/* Structure for event handler registered at compile time */
struct net_mgmt_event_static_handler {
        uint64_t event_mask;
        net_mgmt_event_static_handler_t handler;
        void *user_data;
};


#define NET_MGMT_REGISTER_EVENT_HANDLER(_name, _event_mask, _func, _user_data)  \
        const STRUCT_SECTION_ITERABLE(net_mgmt_event_static_handler, _name) = { \
                .event_mask = _event_mask,                                      \
                .handler = _func,                                               \
                .user_data = (void *)_user_data,                                \
        }

#ifdef CONFIG_NET_MGMT_EVENT
static inline
void net_mgmt_init_event_callback(struct net_mgmt_event_callback *cb,
                                  net_mgmt_event_handler_t handler,
                                  uint64_t mgmt_event_mask)
{
        __ASSERT(cb, "Callback pointer should not be NULL");
        __ASSERT(handler, "Handler pointer should not be NULL");

        cb->handler = handler;
        cb->event_mask = mgmt_event_mask;
};
#else
#define net_mgmt_init_event_callback(...)
#endif

#ifdef CONFIG_NET_MGMT_EVENT
void net_mgmt_add_event_callback(struct net_mgmt_event_callback *cb);
#else
#define net_mgmt_add_event_callback(...)
#endif

#ifdef CONFIG_NET_MGMT_EVENT
void net_mgmt_del_event_callback(struct net_mgmt_event_callback *cb);
#else
#define net_mgmt_del_event_callback(...)
#endif

#if defined(CONFIG_NET_MGMT_EVENT) || defined(__DOXYGEN__)
void net_mgmt_event_notify_with_info(uint64_t mgmt_event, struct net_if *iface,
                                     const void *info, size_t length);
#else
static inline void net_mgmt_event_notify_with_info(uint64_t mgmt_event, struct net_if *iface,
                                                   const void *info, size_t length)
{
        ARG_UNUSED(mgmt_event);
        ARG_UNUSED(iface);
        ARG_UNUSED(info);
        ARG_UNUSED(length);
}
#endif

#if defined(CONFIG_NET_MGMT_EVENT) || defined(__DOXYGEN__)
static inline void net_mgmt_event_notify(uint64_t mgmt_event,
                                         struct net_if *iface)
{
        net_mgmt_event_notify_with_info(mgmt_event, iface, NULL, 0);
}
#else
static inline void net_mgmt_event_notify(uint64_t mgmt_event,
                                         struct net_if *iface)
{
        ARG_UNUSED(mgmt_event);
        ARG_UNUSED(iface);
}
#endif

#ifdef CONFIG_NET_MGMT_EVENT
int net_mgmt_event_wait(uint64_t mgmt_event_mask,
                        uint64_t *raised_event,
                        struct net_if **iface,
                        const void **info,
                        size_t *info_length,
                        k_timeout_t timeout);
#else
static inline int net_mgmt_event_wait(uint64_t mgmt_event_mask,
                                      uint64_t *raised_event,
                                      struct net_if **iface,
                                      const void **info,
                                      size_t *info_length,
                                      k_timeout_t timeout)
{
        ARG_UNUSED(mgmt_event_mask);
        ARG_UNUSED(raised_event);
        ARG_UNUSED(iface);
        ARG_UNUSED(info);
        ARG_UNUSED(info_length);
        ARG_UNUSED(timeout);
        return 0;
}
#endif

#ifdef CONFIG_NET_MGMT_EVENT
int net_mgmt_event_wait_on_iface(struct net_if *iface,
                                 uint64_t mgmt_event_mask,
                                 uint64_t *raised_event,
                                 const void **info,
                                 size_t *info_length,
                                 k_timeout_t timeout);
#else
static inline int net_mgmt_event_wait_on_iface(struct net_if *iface,
                                               uint64_t mgmt_event_mask,
                                               uint64_t *raised_event,
                                               const void **info,
                                               size_t *info_length,
                                               k_timeout_t timeout)
{
        ARG_UNUSED(iface);
        ARG_UNUSED(mgmt_event_mask);
        ARG_UNUSED(raised_event);
        ARG_UNUSED(info);
        ARG_UNUSED(info_length);
        ARG_UNUSED(timeout);
        return 0;
}
#endif

#ifdef CONFIG_NET_MGMT_EVENT
void net_mgmt_event_init(void);
#else
#define net_mgmt_event_init(...)
#endif /* CONFIG_NET_MGMT_EVENT */


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_NET_NET_MGMT_H_ */
```

## 9.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2016 Intel Corporation.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 38 行

十六进制值：`0x8000000000000000`。

### 注释 3：原第 39 行

十六进制值：`0x4000000000000000`。

### 注释 4：原第 40 行

十六进制值：`0x3000000000000000`。

### 注释 5：原第 41 行

十六进制值：`0x0800000000000000`。

### 注释 6：原第 42 行

十六进制值：`0x07F0000000000000`。

### 注释 7：原第 43 行

十六进制值：`0x000FFFFFFFFFFFFF`。

### 注释 8：原第 45 行

待办（TODO）：根据掩码（mask）确定该值。

### 注释 9：原第 63 行

实用的通用定义（generic definitions）。

### 注释 10：原第 88 行

源码树之外（out-of-tree）的代码可以使用以下 `userX` 层代码（layer codes）。

### 注释 11：原第 93 行

保留供将来使用的层代码（layer code）。

### 注释 12：原第 225 行

在编译时注册的事件处理函数（event handler）的结构体。

### 注释 13：原第 441 行

条件编译配置（Configuration）标记：`CONFIG_NET_MGMT_EVENT`。

### 注释 14：原第 451 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_NET_MGMT_H_`。

## 9.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/net__mgmt_8h.html)
- [zephyr/net/net_core.h](../api_file_interface_reference/P037_zephyr__net__net_core.h_文件参考.md)
- [zephyr/sys/iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [net_mgmt_layer_code](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga5e6911455b9ab9f4c82780001459461a)
- [NET_MGMT_LAYER_CODE_UNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa3206e13330183c74d20e89407e11c7cd)
- [NET_MGMT_LAYER_CODE_IFACE](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa2e23e545f7d78775adb5271f7bf42518)
- [NET_MGMT_LAYER_CODE_CONN](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aabf1c9ef98fb7237ba1591108c67bf1d7)
- [NET_MGMT_LAYER_CODE_IPV4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa25c33c6faa9d22f4ac5b70049bb4bbd2)
- [NET_MGMT_LAYER_CODE_IPV6](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa8f1f092ecdfcf341458e7389cee3ace8)
- [NET_MGMT_LAYER_CODE_L4](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aab60d69e5ee62cb0212b1e424d7847b4e)
- [NET_MGMT_LAYER_CODE_COAP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa5701861bfb5fae92e8c7b08ea02f61a7)
- [NET_MGMT_LAYER_CODE_STATS](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa3ab69a93464d5fa0d5be9ac9f3757cb6)
- [NET_MGMT_LAYER_CODE_HOSTAP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa06935e2c46523b1a3f414f4c981992fc)
- [NET_MGMT_LAYER_CODE_ETHERNET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aafd0569a3f3cde9e892751a84b74836b4)
- [NET_MGMT_LAYER_CODE_IEEE802514](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa4893c212a3026909dcb8663abbdf2b2b)
- [NET_MGMT_LAYER_CODE_PPP](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa52b23f5afbf235bef6bc2aeea69271c1)
- [NET_MGMT_LAYER_CODE_VIRTUAL](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aac767c8da93a6d0f5a53e64cbfdf94fca)
- [NET_MGMT_LAYER_CODE_WIFI](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa7f2f4d110d3003974bd0da0154c2d789)
- [NET_MGMT_LAYER_CODE_PACKET](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa997785b24761b410a1d33788c46f90b1)
- [NET_MGMT_LAYER_CODE_USER3](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa4e57a620f5778d346984398c0e786977)
- [NET_MGMT_LAYER_CODE_USER2](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aaa335a8c82c6d7614337e3501a69aa1d4)
- [NET_MGMT_LAYER_CODE_USER1](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aa10876d890aac72553ab69c0964bef48a)
- [NET_MGMT_LAYER_CODE_RESERVED](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gga5e6911455b9ab9f4c82780001459461aaef64c0749996046b313ebf366b3eab75)
- [zephyr/net/net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h.html)
- [net_mgmt_request_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga78b9302193bd0c5cc35d81d298a5eb6b)
- [uint64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a2095b9bffea4b2656950c6c0419edbf1)
- [net_mgmt_event_callback](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md)
- [net_mgmt_event_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga2e83a5a769ac52c846f255e23aea84d2)
- [sys_snode_t](../slist_reference/P001_单向链表公共接口.md#ga69bf43aad81e3ee2d55250c59b857493)
- [node](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md#a05a4f445731f9f72209a652f2653e1ea)
- [handler](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md#ada57aabc8acc3e9be93fb2726321f1b2)
- [k_sem](../synchronization_reference/P009_内核信号量结构.md)
- [sync_call](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md#a7403d98fe528c492a4b1b449b43c10d3)
- [event_mask](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md#a99e3174c1052488877b3db6349de61e8)
- [raised_event](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md#a555d868d6a0d6ecb04d09607fab06b79)
- [net_mgmt_event_static_handler_t](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaf3773f8e945c4ec05b2fab46cd8b1881)
- [net_mgmt_init_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga4e42b6d16b863ca374d032682e8c11fb)
- [net_mgmt_add_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gae53f5bbc973b0f414107eca75ac0c26f)
- [net_mgmt_del_event_callback](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga4960bfb01ecd891da72c57f17587f946)
- [net_mgmt_event_notify_with_info](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga6415ec1e2e7f477c8976022ac33b0654)
- [net_mgmt_event_notify](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gabf710692e596a2d98f37b82da884a82a)
- [net_mgmt_event_wait](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga7137c77c55ee2609941c88db79e22d1a)
- [k_timeout_t](../timer_reference/P087_内核超时类型.md)
- [net_mgmt_event_wait_on_iface](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#ga3ab114106df41144c0fae8e6faad12cb)
- [net_mgmt_event_init](https://docs.zephyrproject.org/latest/doxygen/html/group__net__mgmt.html#gaab4fe2e9ea0657bf91fb1910af6729cc)
- [net_core.h](../api_file_interface_reference/P037_zephyr__net__net_core.h_文件参考.md)
- [net_event.h](https://docs.zephyrproject.org/latest/doxygen/html/net__event_8h.html)
- [net_mgmt_event_callback::node](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md#a05a4f445731f9f72209a652f2653e1ea)
- [net_mgmt_event_callback::raised_event](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md#a555d868d6a0d6ecb04d09607fab06b79)
- [net_mgmt_event_callback::sync_call](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md#a7403d98fe528c492a4b1b449b43c10d3)
- [net_mgmt_event_callback::event_mask](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md#a99e3174c1052488877b3db6349de61e8)
- [net_mgmt_event_callback::handler](../network_core_model_reference/P110_net_mgmt_event_callback_结构体.md#ada57aabc8acc3e9be93fb2726321f1b2)
- [iterable_sections.h](../iterable_reference/P002_可遍历段辅助头文件参考.md)

---

[上一章](P008_msos_desc.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P010_pzem004t.h_源码浏览.md)
