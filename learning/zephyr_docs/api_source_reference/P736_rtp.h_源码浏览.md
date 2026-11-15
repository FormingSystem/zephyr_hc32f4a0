---
id: learning.zephyr-docs.api-source-reference.page-736
title: rtp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/rtp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第736章\_rtp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/rtp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/rtp_8h.html)。

## 736.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00095"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="foldopen00105"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00109"></a>
<a id="l00111"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00117"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00142"></a>
<a id="foldopen00144"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00152"></a>
<a id="foldopen00154"></a>
<a id="l00154"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00159"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00165"></a>
<a id="l00169"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="foldopen00175"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00182"></a>
<a id="l00187"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00193"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="l00196"></a>
<a id="l00197"></a>
<a id="foldopen00201"></a>
<a id="l00201"></a>
<a id="l00203"></a>
<a id="l00204"></a>
<a id="l00206"></a>
<a id="l00207"></a>
<a id="l00208"></a>
<a id="l00210"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="foldopen00230"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00235"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00242"></a>
<a id="l00244"></a>
<a id="l00245"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00258"></a>
<a id="l00259"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00267"></a>
<a id="l00269"></a>
<a id="foldopen00283"></a>
<a id="l00283"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00321"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="foldopen00341"></a>
<a id="l00341"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00345"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="foldopen00364"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="l00369"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="l00383"></a>
<a id="l00384"></a>
<a id="l00395"></a>
<a id="l00396"></a>
<a id="l00406"></a>
<a id="l00407"></a>
<a id="l00417"></a>
<a id="l00418"></a>
<a id="l00436"></a>
<a id="l00437"></a>
<a id="l00438"></a>
<a id="l00439"></a>
<a id="foldopen00454"></a>
<a id="l00454"></a>
<a id="l00455"></a>
<a id="l00456"></a>
<a id="l00457"></a>
<a id="l00458"></a>
<a id="l00459"></a>
<a id="foldopen00467"></a>
<a id="l00467"></a>
<a id="l00468"></a>
<a id="l00469"></a>
<a id="l00470"></a>
<a id="l00471"></a>
<a id="l00472"></a>
<a id="l00473"></a>
<a id="foldopen00481"></a>
<a id="l00481"></a>
<a id="l00482"></a>
<a id="l00483"></a>
<a id="l00484"></a>
<a id="l00485"></a>
<a id="l00486"></a>
<a id="l00487"></a>
<a id="foldopen00495"></a>
<a id="l00495"></a>
<a id="l00496"></a>
<a id="l00497"></a>
<a id="l00498"></a>
<a id="l00499"></a>
<a id="l00500"></a>
<a id="l00501"></a>
<a id="foldopen00509"></a>
<a id="l00509"></a>
<a id="l00510"></a>
<a id="l00511"></a>
<a id="l00512"></a>
<a id="l00513"></a>
<a id="l00514"></a>
<a id="l00515"></a>
<a id="foldopen00523"></a>
<a id="l00523"></a>
<a id="l00524"></a>
<a id="l00525"></a>
<a id="l00526"></a>
<a id="l00527"></a>
<a id="l00528"></a>
<a id="l00529"></a>
<a id="foldopen00537"></a>
<a id="l00537"></a>
<a id="l00538"></a>
<a id="l00539"></a>
<a id="l00540"></a>
<a id="l00541"></a>
<a id="l00542"></a>
<a id="l00543"></a>
<a id="foldopen00550"></a>
<a id="l00550"></a>
<a id="l00551"></a>
<a id="l00552"></a>
<a id="l00553"></a>
<a id="l00554"></a>
<a id="l00555"></a>
<a id="l00556"></a>
<a id="l00557"></a>
<a id="foldopen00564"></a>
<a id="l00564"></a>
<a id="l00565"></a>
<a id="l00566"></a>
<a id="l00567"></a>
<a id="l00568"></a>
<a id="l00569"></a>
<a id="l00570"></a>
<a id="l00571"></a>
<a id="foldopen00578"></a>
<a id="l00578"></a>
<a id="l00579"></a>
<a id="l00580"></a>
<a id="l00581"></a>
<a id="l00582"></a>
<a id="l00583"></a>
<a id="l00584"></a>
<a id="l00585"></a>
<a id="foldopen00592"></a>
<a id="l00592"></a>
<a id="l00593"></a>
<a id="l00594"></a>
<a id="l00595"></a>
<a id="l00596"></a>
<a id="l00597"></a>
<a id="l00598"></a>
<a id="l00599"></a>
<a id="foldopen00606"></a>
<a id="l00606"></a>
<a id="l00607"></a>
<a id="l00608"></a>
<a id="l00609"></a>
<a id="l00610"></a>
<a id="l00611"></a>
<a id="l00612"></a>
<a id="l00613"></a>
<a id="foldopen00620"></a>
<a id="l00620"></a>
<a id="l00621"></a>
<a id="l00622"></a>
<a id="l00623"></a>
<a id="l00624"></a>
<a id="l00625"></a>
<a id="l00626"></a>
<a id="l00627"></a>
<a id="l00628"></a>
<a id="l00629"></a>
<a id="l00630"></a>
<a id="l00631"></a>
<a id="l00635"></a>
<a id="l00636"></a>
<a id="agroup__rtp_html_ga02216271230f855d94b44b78f4757b5e"></a>
<a id="agroup__rtp_html_ga12f93f7d82054a193d42934f5f62b867"></a>
<a id="agroup__rtp_html_ga15d59475e540b1ddd310005700f52701"></a>
<a id="agroup__rtp_html_ga22597830166e0ad8a41edd743ccf5649"></a>
<a id="agroup__rtp_html_ga35eebe350579f0f8790cb94859955eb8"></a>
<a id="agroup__rtp_html_ga41080f91afac5e6f78f38d4d4e739917"></a>
<a id="agroup__rtp_html_ga42d0c8ff84d8a5f16f66bc6caa4a55dc"></a>
<a id="agroup__rtp_html_ga45003b240b30719982ab8862a47f6681"></a>
<a id="agroup__rtp_html_ga51107e583ef87b9d312dc524a1e1a9c8"></a>
<a id="agroup__rtp_html_ga5d7875fd2dda60e9bf827146b3ec6ad0"></a>
<a id="agroup__rtp_html_ga64f90b3a7f8c78a16f975bff108ba86e"></a>
<a id="agroup__rtp_html_ga6b47f65a67c20174c8f18197f78ea704"></a>
<a id="agroup__rtp_html_ga77afc3360c202c59b6b34bf8d5f9c872"></a>
<a id="agroup__rtp_html_ga7aea179489f9d2436925eadb922c3ed5"></a>
<a id="agroup__rtp_html_ga7dc5320de0686db3acc8ea9e75ac2bfc"></a>
<a id="agroup__rtp_html_ga7f815441c6bd7084da07ad73d159e1d0"></a>
<a id="agroup__rtp_html_ga80f1fa1792c888a1f02a5ec56d7e0429"></a>
<a id="agroup__rtp_html_ga81d02bb212d040c0087669c0c264a1b3"></a>
<a id="agroup__rtp_html_ga85cc09256304d0ee0ae3a578610b63ca"></a>
<a id="agroup__rtp_html_ga8b36233d74d14bda763cfa7188b10d89"></a>
<a id="agroup__rtp_html_ga95560c5687aa035c0d0a8f2cf0b9cb74"></a>
<a id="agroup__rtp_html_ga98688e1d781e8eb6285153429056b7bb"></a>
<a id="agroup__rtp_html_gaa0e466fdc7416ded15259e514866e84b"></a>
<a id="agroup__rtp_html_gaa488e6291ed45498d38597cbc7a63fab"></a>
<a id="agroup__rtp_html_gaad8d19269d142a82868052669fc73a40"></a>
<a id="agroup__rtp_html_gab132b3ceb7e7431b537dab3144351143"></a>
<a id="agroup__rtp_html_gab1df8386398cd1f4dd5ec5c470439bce"></a>
<a id="agroup__rtp_html_gab7925fd9990efef208bbd1562cf46fbf"></a>
<a id="agroup__rtp_html_gab926a5adae98b8b4e142ce834f7e1769"></a>
<a id="agroup__rtp_html_gac4e487b090ef9194accbab5a8370bab4"></a>
<a id="agroup__rtp_html_gad5c5d9a7c65f6a7ee02d640653cd9bd5"></a>
<a id="agroup__rtp_html_gaeb4d116a464674e0280efd5f2db67f69"></a>
<a id="agroup__rtp_html_gga15d59475e540b1ddd310005700f52701a850aaf89c815c0f69fd5dab361b4fe43"></a>
<a id="agroup__rtp_html_ggad5c5d9a7c65f6a7ee02d640653cd9bd5a296defa58c2c0f8348ff72133a426d00"></a>
<a id="agroup__rtp_html_ggad5c5d9a7c65f6a7ee02d640653cd9bd5a7ad4596947e09538ff21b529390140d6"></a>
<a id="agroup__rtp_html_ggad5c5d9a7c65f6a7ee02d640653cd9bd5ad0aacb43fde7fb0932dac083e82c2a76"></a>
<a id="akernel_8h_html"></a>
<a id="alog__core_8h_html"></a>
<a id="anet_2socket_8h_html"></a>
<a id="anet__context_8h_html"></a>
<a id="anet__if_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="aptp__time_8h_html"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa03c8b31bf67a097dd9f8153a04ef86b"></a>
<a id="asilabs-pinctrl-siwx91x_8h_html_aa49a456f06f7bdbedfcf3517e461947e"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructk__mutex_html"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__ptp__time_html"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructrtp__header__extension_html"></a>
<a id="astructrtp__header__extension_html_aaad7a4d30851522e4f3f224df2f31135"></a>
<a id="astructrtp__header__extension_html_acad1e7923764e9e67b3789898256ae3c"></a>
<a id="astructrtp__header__extension_html_acdf6aa685045acea96c92ad412eaecb2"></a>
<a id="astructrtp__header_html"></a>
<a id="astructrtp__header_html_a2608e48cddd0b18bafc279517cb98e5a"></a>
<a id="astructrtp__header_html_a36f45a621508f9f2c834f6572358fe7f"></a>
<a id="astructrtp__header_html_a967880697606545015c5078dd4af229c"></a>
<a id="astructrtp__header_html_aaff9f61cdfb53a9c43ce416a6ddf08bd"></a>
<a id="astructrtp__header_html_ac6307a27e70b53784832ba5cc92ad8cd"></a>
<a id="astructrtp__header_html_ad7ee2dd76dd05924c45b766c993f8dcb"></a>
<a id="astructrtp__header_html_ae9679a49fd44503d8a5a7d74bff98fb4"></a>
<a id="astructrtp__packet_html"></a>
<a id="astructrtp__packet_html_a4e7aa001830c27540830fae728d468a6"></a>
<a id="astructrtp__packet_html_a5fd40a8d15441f4aa22c989ad3a086af"></a>
<a id="astructrtp__packet_html_ab6b88aae97f87c11089cdd70f24c722f"></a>
<a id="astructrtp__session__context_html"></a>
<a id="astructrtp__session__context_html_a149d649197fd40a9e129a9e3e95b48b2"></a>
<a id="astructrtp__session__context_html_a1aceba2a7406f2be87186f925b4e8fda"></a>
<a id="astructrtp__session__context_html_a5684adbb6eecd726b154d2b97059fdd4"></a>
<a id="astructrtp__session__context_html_a936e1389e182bcc07c7ddb514dfd6745"></a>
<a id="astructrtp__session__context_html_ac25e4a61cb0724f7fa87773e6bd84fad"></a>
<a id="astructrtp__session__context_html_ad989ac0403bda54841f06a31877925fa"></a>
<a id="astructrtp__session_html"></a>
<a id="astructrtp__session_html_a272c8f29a37438938a4c8e9c4d2d16ca"></a>
<a id="astructrtp__session_html_a29f55e109e705fd0b9c08e2aef7c5b80"></a>
<a id="astructrtp__session_html_a2e449943d7d522022f977250513a7ac4"></a>
<a id="astructrtp__session_html_a60b793a3299cf64e7d319f992e6e9f37"></a>
<a id="astructrtp__session_html_a99b191ad08cd8fe5e20a4d8e1bae7547"></a>
<a id="astructrtp__session_html_aa2fadbf53d01bc8d0959e822a5753285"></a>
<a id="astructrtp__session_html_aad318a86f8e90f02597b3e9edff52c65"></a>
<a id="astructrtp__session_html_ab5899cb4c93868ca6ecbbf10762d37b1"></a>
<a id="astructrtp__session_html_ac859d15cfdcf02e93fcaf02dcb88cecd"></a>
<a id="astructrtp__session_html_aeb6fc69512410a953be85cea1f43ed41"></a>
<a id="astructrtp__transport_html"></a>
<a id="astructrtp__transport_html_a39a4570191bec0e16660aa666701aff4"></a>
<a id="asys_2util_8h_html"></a>
<a id="autil__macro_8h_html"></a>

```c
/*
 *  SPDX-FileCopyrightText: 2026 Basalte bv
 *
 *  SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_RTP_H_
#define ZEPHYR_INCLUDE_NET_RTP_H_

#include <zephyr/kernel.h>
#include <zephyr/logging/log_core.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/net_if.h>
#include <zephyr/net/socket.h>
#ifdef CONFIG_NET_PKT_TIMESTAMP
#include <zephyr/net/ptp_time.h>
#endif
#include <zephyr/net/net_context.h>
#include <zephyr/sys/util.h>
#include <zephyr/sys/util_macro.h>

#ifdef __cplusplus
extern "C" {
#endif


#define RTP_VERSION 2

#define RTP_MIN_HEADER_LEN 12

#define RTP_PAYLOAD_TYPE_MAX 127

#define RTP_MARKER 1

#define RTP_HDR_V_MASK  GENMASK(7, 6)
#define RTP_HDR_P_MASK  BIT(5)
#define RTP_HDR_X_MASK  BIT(4)
#define RTP_HDR_CC_MASK GENMASK(3, 0)
#define RTP_HDR_M_MASK  BIT(7)
#define RTP_HDR_PT_MASK GENMASK(6, 0)

#if defined(CONFIG_RTP_MAX_CSRC_COUNT) || defined(__DOXYGEN__)
#define RTP_MAX_CSRC_COUNT CONFIG_RTP_MAX_CSRC_COUNT
#else
#define RTP_MAX_CSRC_COUNT 0
#endif

struct rtp_header_extension {
        uint16_t definition;
        uint16_t length;
        uint8_t *data;
};

struct rtp_header {
        uint8_t vpxcc;
        uint8_t mpt;
        uint16_t seq;
        uint32_t ts;
        uint32_t ssrc;
        uint32_t csrc[RTP_MAX_CSRC_COUNT];
        struct rtp_header_extension header_extension;
};

struct rtp_packet {
        struct rtp_header header;
        uint8_t *payload;
        size_t payload_len;

#ifdef CONFIG_NET_PKT_TIMESTAMP
        struct net_ptp_time timestamp;
#endif
};

struct rtp_session;

typedef void (*rtp_rx_cb_t)(struct rtp_session *session, struct rtp_packet *packet,
                            void *user_data);

enum rtp_role {
        RTP_ROLE_SINK,
        RTP_ROLE_SOURCE,
        RTP_ROLE_BOTH,
};

struct rtp_session_context {
        struct net_if *iface;

        struct net_sockaddr_storage sock_addr;
        enum rtp_role role;

        uint8_t payload_type;

        rtp_rx_cb_t callback;
        void *user_data;
};

enum rtp_transport_type {
#ifdef CONFIG_RTP_TRANSPORT_SOCKET
        RTP_TRANSPORT_SOCKET,
#endif /* CONFIG_RTP_TRANSPORT_SOCKET */
#ifdef CONFIG_RTP_TRANSPORT_NET_PKT
        RTP_TRANSPORT_NET_PKT,
#endif /* CONFIG_RTP_TRANSPORT_NET_PKT */

        RTP_TRANSPORT_NUM,
};

BUILD_ASSERT(RTP_TRANSPORT_NUM > 0, "Please select at least 1 RTP transport backend");

struct rtp_transport {
        enum rtp_transport_type type;

        union {
#ifdef CONFIG_RTP_TRANSPORT_SOCKET
                struct {
                        int socket_rx_fd;
                        int socket_tx_fd;
                };
#endif /* CONFIG_RTP_TRANSPORT_SOCKET */
#ifdef CONFIG_RTP_TRANSPORT_NET_PKT
                struct {
                        struct net_conn_handle *net_handle_rtp;
                };
#endif /* CONFIG_RTP_TRANSPORT_NET_PKT */
        };
};

struct rtp_session {
        struct rtp_transport transport;
        struct rtp_session_context rtp_context;

        struct k_mutex lock;

        uint32_t ssrc;
        uint32_t timestamp;
        uint16_t sequence_number;

        uint16_t local_port;

        uint32_t csrc[RTP_MAX_CSRC_COUNT];
        size_t csrc_len;

#if CONFIG_RTP_LOG_LEVEL >= LOG_LEVEL_DBG
        const char *name;
#endif
};

#if CONFIG_RTP_LOG_LEVEL >= LOG_LEVEL_DBG
#define RTP_SESSION_NAME(_name) .name = STRINGIFY(_name),
#else
#define RTP_SESSION_NAME(_name)
#endif

#define RTP_SESSION_DEFINE(_name, _local_port)                                                     \
        struct rtp_session _name = {.local_port = _local_port, RTP_SESSION_NAME(_name)}

int rtp_init_header_extension(struct rtp_header_extension *hdr_x, uint16_t definition,
                              uint8_t *data, size_t len);

int rtp_session_init(struct rtp_session *session, struct net_if *iface,
                     struct net_sockaddr *sock_addr, enum rtp_role role, uint8_t payload_type,
                     rtp_rx_cb_t callback, void *user_data, enum rtp_transport_type transport_type);

static inline int rtp_session_init_rx(struct rtp_session *session, struct net_if *iface,
                                      struct net_sockaddr *sock_addr, rtp_rx_cb_t callback,
                                      void *user_data, enum rtp_transport_type transport_type)
{
        return rtp_session_init(session, iface, sock_addr, RTP_ROLE_SINK, 0, callback, user_data,
                                transport_type);
}

static inline int rtp_session_init_tx(struct rtp_session *session, struct net_if *iface,
                                      struct net_sockaddr *sock_addr, uint8_t payload_type,
                                      enum rtp_transport_type transport_type)
{
        return rtp_session_init(session, iface, sock_addr, RTP_ROLE_SOURCE, payload_type, NULL,
                                NULL, transport_type);
}

int rtp_session_start(struct rtp_session *session);

int rtp_session_stop(struct rtp_session *session);

int rtp_session_add_csrc(struct rtp_session *session, uint32_t csrc);

int rtp_session_remove_csrc(struct rtp_session *session, uint32_t csrc);

int rtp_session_send(struct rtp_session *session, void *data, size_t len, uint32_t delta_ts,
                     uint8_t padding, uint8_t marker, struct rtp_header_extension *hdr_x,
                     uint32_t *timestamp);

static inline int rtp_session_send_simple(struct rtp_session *session, void *data, size_t len,
                                          uint32_t delta_ts)
{
        return rtp_session_send(session, data, len, delta_ts, 0, 0, NULL, NULL);
}

static inline uint8_t rtp_header_get_v(const struct rtp_header *h)
{
        __ASSERT_NO_MSG(h != NULL);

        return FIELD_GET(RTP_HDR_V_MASK, h->vpxcc);
}

static inline uint8_t rtp_header_get_p(const struct rtp_header *h)
{
        __ASSERT_NO_MSG(h != NULL);

        return FIELD_GET(RTP_HDR_P_MASK, h->vpxcc);
}

static inline uint8_t rtp_header_get_x(const struct rtp_header *h)
{
        __ASSERT_NO_MSG(h != NULL);

        return FIELD_GET(RTP_HDR_X_MASK, h->vpxcc);
}

static inline uint8_t rtp_header_get_cc(const struct rtp_header *h)
{
        __ASSERT_NO_MSG(h != NULL);

        return FIELD_GET(RTP_HDR_CC_MASK, h->vpxcc);
}

static inline uint8_t rtp_header_get_m(const struct rtp_header *h)
{
        __ASSERT_NO_MSG(h != NULL);

        return FIELD_GET(RTP_HDR_M_MASK, h->mpt);
}

static inline uint8_t rtp_header_get_pt(const struct rtp_header *h)
{
        __ASSERT_NO_MSG(h != NULL);

        return FIELD_GET(RTP_HDR_PT_MASK, h->mpt);
}

static inline void rtp_header_set_v(struct rtp_header *h, uint8_t value)
{
        __ASSERT_NO_MSG(h != NULL);

        h->vpxcc &= ~RTP_HDR_V_MASK;
        h->vpxcc |= FIELD_PREP(RTP_HDR_V_MASK, value);
}

static inline void rtp_header_set_p(struct rtp_header *h, uint8_t value)
{
        __ASSERT_NO_MSG(h != NULL);

        h->vpxcc &= ~RTP_HDR_P_MASK;
        h->vpxcc |= FIELD_PREP(RTP_HDR_P_MASK, value);
}

static inline void rtp_header_set_x(struct rtp_header *h, uint8_t value)
{
        __ASSERT_NO_MSG(h != NULL);

        h->vpxcc &= ~RTP_HDR_X_MASK;
        h->vpxcc |= FIELD_PREP(RTP_HDR_X_MASK, value);
}

static inline void rtp_header_set_cc(struct rtp_header *h, uint8_t value)
{
        __ASSERT_NO_MSG(h != NULL);

        h->vpxcc &= ~RTP_HDR_CC_MASK;
        h->vpxcc |= FIELD_PREP(RTP_HDR_CC_MASK, value);
}

static inline void rtp_header_set_m(struct rtp_header *h, uint8_t value)
{
        __ASSERT_NO_MSG(h != NULL);

        h->mpt &= ~RTP_HDR_M_MASK;
        h->mpt |= FIELD_PREP(RTP_HDR_M_MASK, value);
}

static inline void rtp_header_set_pt(struct rtp_header *h, uint8_t value)
{
        __ASSERT_NO_MSG(h != NULL);

        h->mpt &= ~RTP_HDR_PT_MASK;
        h->mpt |= FIELD_PREP(RTP_HDR_PT_MASK, value);
}

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_RTP_H_ */
```

## 736.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

SPDX 文件版权声明（FileCopyrightText）：2026 Basalte bv。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 181 行

条件编译配置（Configuration）标记：`CONFIG_RTP_TRANSPORT_SOCKET`。

### 注释 3：原第 188 行

条件编译配置（Configuration）标记：`CONFIG_RTP_TRANSPORT_NET_PKT`。

### 注释 4：原第 214 行

条件编译配置（Configuration）标记：`CONFIG_RTP_TRANSPORT_SOCKET`。

### 注释 5：原第 220 行

条件编译配置（Configuration）标记：`CONFIG_RTP_TRANSPORT_NET_PKT`。

### 注释 6：原第 636 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_RTP_H_`。

## 736.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/rtp_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/logging/log_core.h](../log_internal_reference/P001_日志核心头文件参考.md)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [zephyr/net/ptp_time.h](https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h.html)
- [zephyr/net/net_context.h](https://docs.zephyrproject.org/latest/doxygen/html/net__context_8h.html)
- [zephyr/sys/util.h](../util_reference/P002_通用工具头文件参考.md)
- [zephyr/sys/util_macro.h](../util_reference/P004_宏工具头文件参考.md)
- [rtp_header_extension](../network_application_model_reference/P082_rtp_header_extension_结构体.md)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [definition](../network_application_model_reference/P082_rtp_header_extension_结构体.md#acdf6aa685045acea96c92ad412eaecb2)
- [length](../network_application_model_reference/P082_rtp_header_extension_结构体.md#acad1e7923764e9e67b3789898256ae3c)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [data](../network_application_model_reference/P082_rtp_header_extension_结构体.md#aaad7a4d30851522e4f3f224df2f31135)
- [rtp_header](../network_application_model_reference/P081_rtp_header_结构体.md)
- [vpxcc](../network_application_model_reference/P081_rtp_header_结构体.md#ad7ee2dd76dd05924c45b766c993f8dcb)
- [mpt](../network_application_model_reference/P081_rtp_header_结构体.md#a2608e48cddd0b18bafc279517cb98e5a)
- [seq](../network_application_model_reference/P081_rtp_header_结构体.md#a36f45a621508f9f2c834f6572358fe7f)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [ts](../network_application_model_reference/P081_rtp_header_结构体.md#a967880697606545015c5078dd4af229c)
- [ssrc](../network_application_model_reference/P081_rtp_header_结构体.md#ac6307a27e70b53784832ba5cc92ad8cd)
- [csrc](../network_application_model_reference/P081_rtp_header_结构体.md#ae9679a49fd44503d8a5a7d74bff98fb4)
- [RTP_MAX_CSRC_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gab1df8386398cd1f4dd5ec5c470439bce)
- [header_extension](../network_application_model_reference/P081_rtp_header_结构体.md#aaff9f61cdfb53a9c43ce416a6ddf08bd)
- [rtp_packet](../network_application_model_reference/P083_rtp_packet_结构体.md)
- [header](../network_application_model_reference/P083_rtp_packet_结构体.md#a5fd40a8d15441f4aa22c989ad3a086af)
- [payload](../network_application_model_reference/P083_rtp_packet_结构体.md#a4e7aa001830c27540830fae728d468a6)
- [payload_len](../network_application_model_reference/P083_rtp_packet_结构体.md#ab6b88aae97f87c11089cdd70f24c722f)
- [net_ptp_time](../network_core_model_reference/P116_net_ptp_time_结构体.md)
- [rtp_session](../network_application_model_reference/P084_rtp_session_结构体.md)
- [rtp_rx_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga8b36233d74d14bda763cfa7188b10d89)
- [rtp_role](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gad5c5d9a7c65f6a7ee02d640653cd9bd5)
- [RTP_ROLE_SINK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ggad5c5d9a7c65f6a7ee02d640653cd9bd5ad0aacb43fde7fb0932dac083e82c2a76)
- [RTP_ROLE_SOURCE](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ggad5c5d9a7c65f6a7ee02d640653cd9bd5a7ad4596947e09538ff21b529390140d6)
- [RTP_ROLE_BOTH](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ggad5c5d9a7c65f6a7ee02d640653cd9bd5a296defa58c2c0f8348ff72133a426d00)
- [rtp_session_context](../network_application_model_reference/P085_rtp_session_context_结构体.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [iface](../network_application_model_reference/P085_rtp_session_context_结构体.md#ad989ac0403bda54841f06a31877925fa)
- [sock_addr](../network_application_model_reference/P085_rtp_session_context_结构体.md#a5684adbb6eecd726b154d2b97059fdd4)
- [role](../network_application_model_reference/P085_rtp_session_context_结构体.md#a936e1389e182bcc07c7ddb514dfd6745)
- [payload_type](../network_application_model_reference/P085_rtp_session_context_结构体.md#ac25e4a61cb0724f7fa87773e6bd84fad)
- [callback](../network_application_model_reference/P085_rtp_session_context_结构体.md#a1aceba2a7406f2be87186f925b4e8fda)
- [user_data](../network_application_model_reference/P085_rtp_session_context_结构体.md#a149d649197fd40a9e129a9e3e95b48b2)
- [rtp_transport_type](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga15d59475e540b1ddd310005700f52701)
- [RTP_TRANSPORT_NUM](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gga15d59475e540b1ddd310005700f52701a850aaf89c815c0f69fd5dab361b4fe43)
- [rtp_transport](../network_application_model_reference/P086_rtp_transport_结构体.md)
- [type](../network_application_model_reference/P086_rtp_transport_结构体.md#a39a4570191bec0e16660aa666701aff4)
- [transport](../network_application_model_reference/P084_rtp_session_结构体.md#a2e449943d7d522022f977250513a7ac4)
- [rtp_context](../network_application_model_reference/P084_rtp_session_结构体.md#ac859d15cfdcf02e93fcaf02dcb88cecd)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [lock](../network_application_model_reference/P084_rtp_session_结构体.md#aa2fadbf53d01bc8d0959e822a5753285)
- [ssrc](../network_application_model_reference/P084_rtp_session_结构体.md#aeb6fc69512410a953be85cea1f43ed41)
- [timestamp](../network_application_model_reference/P084_rtp_session_结构体.md#a272c8f29a37438938a4c8e9c4d2d16ca)
- [sequence_number](../network_application_model_reference/P084_rtp_session_结构体.md#ab5899cb4c93868ca6ecbbf10762d37b1)
- [local_port](../network_application_model_reference/P084_rtp_session_结构体.md#a29f55e109e705fd0b9c08e2aef7c5b80)
- [csrc](../network_application_model_reference/P084_rtp_session_结构体.md#aad318a86f8e90f02597b3e9edff52c65)
- [csrc_len](../network_application_model_reference/P084_rtp_session_结构体.md#a60b793a3299cf64e7d319f992e6e9f37)
- [name](../network_application_model_reference/P084_rtp_session_结构体.md#a99b191ad08cd8fe5e20a4d8e1bae7547)
- [rtp_init_header_extension](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga22597830166e0ad8a41edd743ccf5649)
- [rtp_session_init](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga7dc5320de0686db3acc8ea9e75ac2bfc)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [rtp_session_init_rx](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga77afc3360c202c59b6b34bf8d5f9c872)
- [rtp_session_init_tx](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gab926a5adae98b8b4e142ce834f7e1769)
- [rtp_session_start](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga5d7875fd2dda60e9bf827146b3ec6ad0)
- [rtp_session_stop](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga98688e1d781e8eb6285153429056b7bb)
- [rtp_session_add_csrc](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga64f90b3a7f8c78a16f975bff108ba86e)
- [rtp_session_remove_csrc](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga7f815441c6bd7084da07ad73d159e1d0)
- [rtp_session_send](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga02216271230f855d94b44b78f4757b5e)
- [rtp_session_send_simple](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga6b47f65a67c20174c8f18197f78ea704)
- [rtp_header_get_v](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gab132b3ceb7e7431b537dab3144351143)
- [FIELD_GET](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html#aa49a456f06f7bdbedfcf3517e461947e)
- [RTP_HDR_V_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga95560c5687aa035c0d0a8f2cf0b9cb74)
- [rtp_header_get_p](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaa488e6291ed45498d38597cbc7a63fab)
- [RTP_HDR_P_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga85cc09256304d0ee0ae3a578610b63ca)
- [rtp_header_get_x](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaa0e466fdc7416ded15259e514866e84b)
- [RTP_HDR_X_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga7aea179489f9d2436925eadb922c3ed5)
- [rtp_header_get_cc](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga80f1fa1792c888a1f02a5ec56d7e0429)
- [RTP_HDR_CC_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaad8d19269d142a82868052669fc73a40)
- [rtp_header_get_m](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga42d0c8ff84d8a5f16f66bc6caa4a55dc)
- [RTP_HDR_M_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gac4e487b090ef9194accbab5a8370bab4)
- [rtp_header_get_pt](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga35eebe350579f0f8790cb94859955eb8)
- [RTP_HDR_PT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga81d02bb212d040c0087669c0c264a1b3)
- [rtp_header_set_v](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaeb4d116a464674e0280efd5f2db67f69)
- [~RTP_HDR_V_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga95560c5687aa035c0d0a8f2cf0b9cb74)
- [FIELD_PREP](https://docs.zephyrproject.org/latest/doxygen/html/silabs-pinctrl-siwx91x_8h.html#aa03c8b31bf67a097dd9f8153a04ef86b)
- [rtp_header_set_p](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gab7925fd9990efef208bbd1562cf46fbf)
- [~RTP_HDR_P_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga85cc09256304d0ee0ae3a578610b63ca)
- [rtp_header_set_x](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga51107e583ef87b9d312dc524a1e1a9c8)
- [~RTP_HDR_X_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga7aea179489f9d2436925eadb922c3ed5)
- [rtp_header_set_cc](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga41080f91afac5e6f78f38d4d4e739917)
- [~RTP_HDR_CC_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gaad8d19269d142a82868052669fc73a40)
- [rtp_header_set_m](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga45003b240b30719982ab8862a47f6681)
- [~RTP_HDR_M_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#gac4e487b090ef9194accbab5a8370bab4)
- [rtp_header_set_pt](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga12f93f7d82054a193d42934f5f62b867)
- [~RTP_HDR_PT_MASK](https://docs.zephyrproject.org/latest/doxygen/html/group__rtp.html#ga81d02bb212d040c0087669c0c264a1b3)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [log_core.h](../log_internal_reference/P001_日志核心头文件参考.md)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [net_context.h](https://docs.zephyrproject.org/latest/doxygen/html/net__context_8h.html)
- [net_if.h](https://docs.zephyrproject.org/latest/doxygen/html/net__if_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [ptp_time.h](https://docs.zephyrproject.org/latest/doxygen/html/ptp__time_8h.html)
- [rtp_header_extension::data](../network_application_model_reference/P082_rtp_header_extension_结构体.md#aaad7a4d30851522e4f3f224df2f31135)
- [rtp_header_extension::length](../network_application_model_reference/P082_rtp_header_extension_结构体.md#acad1e7923764e9e67b3789898256ae3c)
- [rtp_header_extension::definition](../network_application_model_reference/P082_rtp_header_extension_结构体.md#acdf6aa685045acea96c92ad412eaecb2)
- [rtp_header::mpt](../network_application_model_reference/P081_rtp_header_结构体.md#a2608e48cddd0b18bafc279517cb98e5a)
- [rtp_header::seq](../network_application_model_reference/P081_rtp_header_结构体.md#a36f45a621508f9f2c834f6572358fe7f)
- [rtp_header::ts](../network_application_model_reference/P081_rtp_header_结构体.md#a967880697606545015c5078dd4af229c)
- [rtp_header::header_extension](../network_application_model_reference/P081_rtp_header_结构体.md#aaff9f61cdfb53a9c43ce416a6ddf08bd)
- [rtp_header::ssrc](../network_application_model_reference/P081_rtp_header_结构体.md#ac6307a27e70b53784832ba5cc92ad8cd)
- [rtp_header::vpxcc](../network_application_model_reference/P081_rtp_header_结构体.md#ad7ee2dd76dd05924c45b766c993f8dcb)
- [rtp_header::csrc](../network_application_model_reference/P081_rtp_header_结构体.md#ae9679a49fd44503d8a5a7d74bff98fb4)
- [rtp_packet::payload](../network_application_model_reference/P083_rtp_packet_结构体.md#a4e7aa001830c27540830fae728d468a6)
- [rtp_packet::header](../network_application_model_reference/P083_rtp_packet_结构体.md#a5fd40a8d15441f4aa22c989ad3a086af)
- [rtp_packet::payload_len](../network_application_model_reference/P083_rtp_packet_结构体.md#ab6b88aae97f87c11089cdd70f24c722f)
- [rtp_session_context::user_data](../network_application_model_reference/P085_rtp_session_context_结构体.md#a149d649197fd40a9e129a9e3e95b48b2)
- [rtp_session_context::callback](../network_application_model_reference/P085_rtp_session_context_结构体.md#a1aceba2a7406f2be87186f925b4e8fda)
- [rtp_session_context::sock_addr](../network_application_model_reference/P085_rtp_session_context_结构体.md#a5684adbb6eecd726b154d2b97059fdd4)
- [rtp_session_context::role](../network_application_model_reference/P085_rtp_session_context_结构体.md#a936e1389e182bcc07c7ddb514dfd6745)
- [rtp_session_context::payload_type](../network_application_model_reference/P085_rtp_session_context_结构体.md#ac25e4a61cb0724f7fa87773e6bd84fad)
- [rtp_session_context::iface](../network_application_model_reference/P085_rtp_session_context_结构体.md#ad989ac0403bda54841f06a31877925fa)
- [rtp_session::timestamp](../network_application_model_reference/P084_rtp_session_结构体.md#a272c8f29a37438938a4c8e9c4d2d16ca)
- [rtp_session::local_port](../network_application_model_reference/P084_rtp_session_结构体.md#a29f55e109e705fd0b9c08e2aef7c5b80)
- [rtp_session::transport](../network_application_model_reference/P084_rtp_session_结构体.md#a2e449943d7d522022f977250513a7ac4)
- [rtp_session::csrc_len](../network_application_model_reference/P084_rtp_session_结构体.md#a60b793a3299cf64e7d319f992e6e9f37)
- [rtp_session::name](../network_application_model_reference/P084_rtp_session_结构体.md#a99b191ad08cd8fe5e20a4d8e1bae7547)
- [rtp_session::lock](../network_application_model_reference/P084_rtp_session_结构体.md#aa2fadbf53d01bc8d0959e822a5753285)
- [rtp_session::csrc](../network_application_model_reference/P084_rtp_session_结构体.md#aad318a86f8e90f02597b3e9edff52c65)
- [rtp_session::sequence_number](../network_application_model_reference/P084_rtp_session_结构体.md#ab5899cb4c93868ca6ecbbf10762d37b1)
- [rtp_session::rtp_context](../network_application_model_reference/P084_rtp_session_结构体.md#ac859d15cfdcf02e93fcaf02dcb88cecd)
- [rtp_session::ssrc](../network_application_model_reference/P084_rtp_session_结构体.md#aeb6fc69512410a953be85cea1f43ed41)
- [rtp_transport::type](../network_application_model_reference/P086_rtp_transport_结构体.md#a39a4570191bec0e16660aa666701aff4)
- [util.h](../util_reference/P002_通用工具头文件参考.md)
- [util_macro.h](../util_reference/P004_宏工具头文件参考.md)

---

[上一章](P735_rtl87x2g-clocks.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P737_rts5817_clock.h_源码浏览.md)
