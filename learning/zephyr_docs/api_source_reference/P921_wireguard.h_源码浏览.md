---
id: learning.zephyr-docs.api-source-reference.page-921
title: wireguard.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wireguard_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第921章\_wireguard.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/wireguard_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/wireguard_8h.html)。

## 921.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
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
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00048"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="foldopen00053"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="foldopen00067"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00080"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00084"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="foldopen00092"></a>
<a id="l00092"></a>
<a id="l00094"></a>
<a id="l00096"></a>
<a id="l00098"></a>
<a id="l00100"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00118"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00124"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00136"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="foldopen00160"></a>
<a id="l00160"></a>
<a id="l00162"></a>
<a id="l00164"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00170"></a>
<a id="l00171"></a>
<a id="l00172"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00187"></a>
<a id="l00199"></a>
<a id="l00200"></a>
<a id="l00208"></a>
<a id="l00209"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00233"></a>
<a id="l00234"></a>
<a id="agroup__wg__vpn__service_html_ga0e81f216e6856b6d73be215b32d62114"></a>
<a id="agroup__wg__vpn__service_html_ga6a5d56dbee1d44de463362d7f2345823"></a>
<a id="agroup__wg__vpn__service_html_ga6aa52085d382dc8075a870c9a151e1e3"></a>
<a id="agroup__wg__vpn__service_html_ga80aaf68ba45ba249ad91fce31bd5b116"></a>
<a id="agroup__wg__vpn__service_html_gae53430ad266fa487b822bb06c180c38c"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="alib_2libc_2minimal_2include_2sys_2types_8h_html"></a>
<a id="anet_2socket_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astructnet__event__vpn__peer_html"></a>
<a id="astructnet__event__vpn__peer_html_a48c12bdfa2f09998fe24d586f70ed35a"></a>
<a id="astructnet__event__vpn__peer_html_a668c569513326c8d1a9e235afab0ce7e"></a>
<a id="astructnet__event__vpn__peer_html_a94c46c495acd29cb29a0645da1dcd137"></a>
<a id="astructnet__event__vpn__peer_html_ab7b7c00b17c106a2f696401c1381de39"></a>
<a id="astructnet__event__vpn__peer_html_affc68879eae926cfcf6b5aaba745b62d"></a>
<a id="astructnet__if_html"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructnet__stats__vpn_html"></a>
<a id="astructnet__stats__vpn_html_a056c976add7ee0ef33408a031e6f7197"></a>
<a id="astructnet__stats__vpn_html_a11289adcdb8d08608425bedfde6bd143"></a>
<a id="astructnet__stats__vpn_html_a11d9999979ee421486b2af9288260187"></a>
<a id="astructnet__stats__vpn_html_a16018a6939274b078d555a25cede3f91"></a>
<a id="astructnet__stats__vpn_html_a21f4d8739b17b6a4f4e7021036bf2e5d"></a>
<a id="astructnet__stats__vpn_html_a27aed70a12946019541abe2dff8348f6"></a>
<a id="astructnet__stats__vpn_html_a3042940448514aa40f22bdbf16b56416"></a>
<a id="astructnet__stats__vpn_html_a404ae2009f1c92c35a08efe2853afc01"></a>
<a id="astructnet__stats__vpn_html_a4b56c0355d183ef955203960ce158f38"></a>
<a id="astructnet__stats__vpn_html_a526da409e515e96706053d1ba338b523"></a>
<a id="astructnet__stats__vpn_html_a625424c311d613f07f1451d82b30814d"></a>
<a id="astructnet__stats__vpn_html_a65a6f590952602ec7c0981243443717a"></a>
<a id="astructnet__stats__vpn_html_a6b95475546f9a8179d82348c7d3bd3ef"></a>
<a id="astructnet__stats__vpn_html_a6d4ec72b231a5896cc182dadc9668916"></a>
<a id="astructnet__stats__vpn_html_a7c994e163e01ffc4efdda372f3c87399"></a>
<a id="astructnet__stats__vpn_html_a9c481d278e8c345caea27cd74299e0d7"></a>
<a id="astructnet__stats__vpn_html_aa6c1df97501730a7efc279e97795d7d5"></a>
<a id="astructnet__stats__vpn_html_ab32df6f0be61194200cb0ca0b4719186"></a>
<a id="astructnet__stats__vpn_html_aba74653967d3235a132c2982a5a2f5ae"></a>
<a id="astructnet__stats__vpn_html_abfc70aed88c4f037757f365e53acdcb9"></a>
<a id="astructnet__stats__vpn_html_ac199357ab8fbf13dceaefe40b3a12ce5"></a>
<a id="astructnet__stats__vpn_html_ac66dac12113dc1e71699587da25688c4"></a>
<a id="astructnet__stats__vpn_html_ada1951a74e4d7faf6ac2819e0cc6573f"></a>
<a id="astructnet__stats__vpn_html_adac60bd39ea0fb623184c438783d243e"></a>
<a id="astructnet__stats__vpn_html_af3b87df2f50f042043830d946b3b0d8a"></a>
<a id="astructnet__stats__vpn_html_af40a96c70f8ab09f3f8a02317fafad6b"></a>
<a id="astructnet__stats__vpn_html_af636ef839bd6e873cd3e88d2ca5dd535"></a>
<a id="astructwireguard__allowed__ip_html"></a>
<a id="astructwireguard__allowed__ip_html_a8aa426557b26b39e0d75378bb3b6191a"></a>
<a id="astructwireguard__allowed__ip_html_a8fa36acaced72872623cdd31c263f53f"></a>
<a id="astructwireguard__allowed__ip_html_afc296b40c62a86ee8beb311fbbab3655"></a>
<a id="astructwireguard__peer__config_html"></a>
<a id="astructwireguard__peer__config_html_a67b63a434cf1d5147dcf988e85b7b958"></a>
<a id="astructwireguard__peer__config_html_a8728365d722ac2bb857cbf4e9eb82d97"></a>
<a id="astructwireguard__peer__config_html_a9632752c8cecccee550548d9b1c3ba97"></a>
<a id="astructwireguard__peer__config_html_a9ae02999964a23bdcd008648f99067b1"></a>
<a id="astructwireguard__peer__config_html_ab31a019c4af3e819f06c02171237ccba"></a>
<a id="astructwireguard__peer__config_html_aca7a334729c726198894e22a2cdb446c"></a>

```c


/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_WIREGUARD_H_
#define ZEPHYR_INCLUDE_NET_WIREGUARD_H_


#include <sys/types.h>
#include <zephyr/types.h>
#include <zephyr/net/socket.h>

#ifdef __cplusplus
extern "C" {
#endif


#if defined(CONFIG_WIREGUARD)
#define WIREGUARD_INTERFACE CONFIG_WIREGUARD_INTERFACE
#else
#define WIREGUARD_INTERFACE ""
#endif

#if defined(CONFIG_WIREGUARD_MAX_SRC_IPS)
#define WIREGUARD_MAX_SRC_IPS CONFIG_WIREGUARD_MAX_SRC_IPS
#else
#define WIREGUARD_MAX_SRC_IPS 1
#endif


#define WIREGUARD_TIMESTAMP_LEN (sizeof(uint64_t) + sizeof(uint32_t))

struct wireguard_allowed_ip {
        struct net_addr addr;
        uint8_t mask_len;
        bool is_valid : 1;
};

struct wireguard_peer_config {
        const char *public_key;

        const uint8_t *preshared_key;

        uint8_t timestamp[WIREGUARD_TIMESTAMP_LEN];

        struct net_sockaddr_storage endpoint_ip;

        struct wireguard_allowed_ip allowed_ip[WIREGUARD_MAX_SRC_IPS];

        int keepalive_interval;
};

struct net_stats_vpn {
        uint32_t keepalive_rx;
        uint32_t keepalive_tx;
        uint32_t invalid_keepalive;
        uint32_t handshake_init_rx;
        uint32_t handshake_init_tx;
        uint32_t handshake_resp_rx;
        uint32_t handshake_resp_tx;
        uint32_t invalid_handshake;
        uint32_t peer_not_found;
        uint32_t key_expired;
        uint32_t invalid_packet;
        uint32_t invalid_key;
        uint32_t invalid_mic;
        uint32_t invalid_packet_len;
        uint32_t invalid_cookie;
        uint32_t invalid_mac1;
        uint32_t invalid_mac2;
        uint32_t decrypt_failed;
        uint32_t drop_rx;
        uint32_t drop_tx;
        uint32_t alloc_failed;
        uint32_t invalid_ip_version;
        uint32_t invalid_ip_family;
        uint32_t denied_ip;
        uint32_t replay_error;
        uint32_t valid_rx;
        uint32_t valid_tx;
};

struct net_event_vpn_peer {
        uint32_t id;
        const char *public_key;
        struct net_sockaddr *endpoint;
        struct wireguard_allowed_ip *allowed_ip[WIREGUARD_MAX_SRC_IPS + 1];
        int keepalive_interval;
};

int wireguard_peer_add(struct wireguard_peer_config *peer_config,
                       struct net_if **peer_iface);

int wireguard_peer_remove(int peer_id);

int wireguard_peer_keepalive(int peer_id);

int wireguard_get_current_time(uint64_t *seconds, uint32_t *nanoseconds);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_WIREGUARD_H_ */
```

## 921.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2026 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 234 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_WIREGUARD_H_`。

## 921.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/wireguard_8h.html)
- [sys/types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [zephyr/types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [zephyr/net/socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [wireguard_allowed_ip](../network_service_model_reference/P070_wireguard_allowed_ip_结构体.md)
- [addr](../network_service_model_reference/P070_wireguard_allowed_ip_结构体.md#a8aa426557b26b39e0d75378bb3b6191a)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [mask_len](../network_service_model_reference/P070_wireguard_allowed_ip_结构体.md#a8fa36acaced72872623cdd31c263f53f)
- [is_valid](../network_service_model_reference/P070_wireguard_allowed_ip_结构体.md#afc296b40c62a86ee8beb311fbbab3655)
- [wireguard_peer_config](../network_service_model_reference/P071_wireguard_peer_config_结构体.md)
- [public_key](../network_service_model_reference/P071_wireguard_peer_config_结构体.md#a9ae02999964a23bdcd008648f99067b1)
- [preshared_key](../network_service_model_reference/P071_wireguard_peer_config_结构体.md#a9632752c8cecccee550548d9b1c3ba97)
- [timestamp](../network_service_model_reference/P071_wireguard_peer_config_结构体.md#a67b63a434cf1d5147dcf988e85b7b958)
- [WIREGUARD_TIMESTAMP_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#ga80aaf68ba45ba249ad91fce31bd5b116)
- [endpoint_ip](../network_service_model_reference/P071_wireguard_peer_config_结构体.md#ab31a019c4af3e819f06c02171237ccba)
- [allowed_ip](../network_service_model_reference/P071_wireguard_peer_config_结构体.md#aca7a334729c726198894e22a2cdb446c)
- [keepalive_interval](../network_service_model_reference/P071_wireguard_peer_config_结构体.md#a8728365d722ac2bb857cbf4e9eb82d97)
- [net_stats_vpn](../network_core_model_reference/P152_net_stats_vpn_结构体.md)
- [uint32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0a8582351ac627ee8bde2973c825e47f)
- [keepalive_rx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#abfc70aed88c4f037757f365e53acdcb9)
- [keepalive_tx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#aa6c1df97501730a7efc279e97795d7d5)
- [invalid_keepalive](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a16018a6939274b078d555a25cede3f91)
- [handshake_init_rx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#ac66dac12113dc1e71699587da25688c4)
- [handshake_init_tx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#af3b87df2f50f042043830d946b3b0d8a)
- [handshake_resp_rx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a65a6f590952602ec7c0981243443717a)
- [handshake_resp_tx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a21f4d8739b17b6a4f4e7021036bf2e5d)
- [invalid_handshake](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a526da409e515e96706053d1ba338b523)
- [peer_not_found](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a6d4ec72b231a5896cc182dadc9668916)
- [key_expired](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a27aed70a12946019541abe2dff8348f6)
- [invalid_packet](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a3042940448514aa40f22bdbf16b56416)
- [invalid_key](../network_core_model_reference/P152_net_stats_vpn_结构体.md#aba74653967d3235a132c2982a5a2f5ae)
- [invalid_mic](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a7c994e163e01ffc4efdda372f3c87399)
- [invalid_packet_len](../network_core_model_reference/P152_net_stats_vpn_结构体.md#adac60bd39ea0fb623184c438783d243e)
- [invalid_cookie](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a11289adcdb8d08608425bedfde6bd143)
- [invalid_mac1](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a11d9999979ee421486b2af9288260187)
- [invalid_mac2](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a4b56c0355d183ef955203960ce158f38)
- [decrypt_failed](../network_core_model_reference/P152_net_stats_vpn_结构体.md#af40a96c70f8ab09f3f8a02317fafad6b)
- [drop_rx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a625424c311d613f07f1451d82b30814d)
- [drop_tx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#ada1951a74e4d7faf6ac2819e0cc6573f)
- [alloc_failed](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a056c976add7ee0ef33408a031e6f7197)
- [invalid_ip_version](../network_core_model_reference/P152_net_stats_vpn_结构体.md#af636ef839bd6e873cd3e88d2ca5dd535)
- [invalid_ip_family](../network_core_model_reference/P152_net_stats_vpn_结构体.md#ab32df6f0be61194200cb0ca0b4719186)
- [denied_ip](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a404ae2009f1c92c35a08efe2853afc01)
- [replay_error](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a9c481d278e8c345caea27cd74299e0d7)
- [valid_rx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a6b95475546f9a8179d82348c7d3bd3ef)
- [valid_tx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#ac199357ab8fbf13dceaefe40b3a12ce5)
- [net_event_vpn_peer](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md)
- [id](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md#ab7b7c00b17c106a2f696401c1381de39)
- [public_key](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md#a48c12bdfa2f09998fe24d586f70ed35a)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [endpoint](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md#a668c569513326c8d1a9e235afab0ce7e)
- [allowed_ip](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md#a94c46c495acd29cb29a0645da1dcd137)
- [keepalive_interval](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md#affc68879eae926cfcf6b5aaba745b62d)
- [wireguard_peer_add](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#ga0e81f216e6856b6d73be215b32d62114)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [wireguard_peer_remove](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#gae53430ad266fa487b822bb06c180c38c)
- [wireguard_peer_keepalive](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#ga6a5d56dbee1d44de463362d7f2345823)
- [wireguard_get_current_time](https://docs.zephyrproject.org/latest/doxygen/html/group__wg__vpn__service.html#ga6aa52085d382dc8075a870c9a151e1e3)
- [uint64_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a2095b9bffea4b2656950c6c0419edbf1)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/include_2zephyr_2types_8h.html)
- [types.h](https://docs.zephyrproject.org/latest/doxygen/html/lib_2libc_2minimal_2include_2sys_2types_8h.html)
- [socket.h](https://docs.zephyrproject.org/latest/doxygen/html/net_2socket_8h.html)
- [net_event_vpn_peer::public_key](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md#a48c12bdfa2f09998fe24d586f70ed35a)
- [net_event_vpn_peer::endpoint](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md#a668c569513326c8d1a9e235afab0ce7e)
- [net_event_vpn_peer::allowed_ip](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md#a94c46c495acd29cb29a0645da1dcd137)
- [net_event_vpn_peer::id](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md#ab7b7c00b17c106a2f696401c1381de39)
- [net_event_vpn_peer::keepalive_interval](../network_core_model_reference/P074_net_event_vpn_peer_结构体.md#affc68879eae926cfcf6b5aaba745b62d)
- [net_stats_vpn::alloc_failed](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a056c976add7ee0ef33408a031e6f7197)
- [net_stats_vpn::invalid_cookie](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a11289adcdb8d08608425bedfde6bd143)
- [net_stats_vpn::invalid_mac1](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a11d9999979ee421486b2af9288260187)
- [net_stats_vpn::invalid_keepalive](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a16018a6939274b078d555a25cede3f91)
- [net_stats_vpn::handshake_resp_tx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a21f4d8739b17b6a4f4e7021036bf2e5d)
- [net_stats_vpn::key_expired](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a27aed70a12946019541abe2dff8348f6)
- [net_stats_vpn::invalid_packet](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a3042940448514aa40f22bdbf16b56416)
- [net_stats_vpn::denied_ip](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a404ae2009f1c92c35a08efe2853afc01)
- [net_stats_vpn::invalid_mac2](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a4b56c0355d183ef955203960ce158f38)
- [net_stats_vpn::invalid_handshake](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a526da409e515e96706053d1ba338b523)
- [net_stats_vpn::drop_rx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a625424c311d613f07f1451d82b30814d)
- [net_stats_vpn::handshake_resp_rx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a65a6f590952602ec7c0981243443717a)
- [net_stats_vpn::valid_rx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a6b95475546f9a8179d82348c7d3bd3ef)
- [net_stats_vpn::peer_not_found](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a6d4ec72b231a5896cc182dadc9668916)
- [net_stats_vpn::invalid_mic](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a7c994e163e01ffc4efdda372f3c87399)
- [net_stats_vpn::replay_error](../network_core_model_reference/P152_net_stats_vpn_结构体.md#a9c481d278e8c345caea27cd74299e0d7)
- [net_stats_vpn::keepalive_tx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#aa6c1df97501730a7efc279e97795d7d5)
- [net_stats_vpn::invalid_ip_family](../network_core_model_reference/P152_net_stats_vpn_结构体.md#ab32df6f0be61194200cb0ca0b4719186)
- [net_stats_vpn::invalid_key](../network_core_model_reference/P152_net_stats_vpn_结构体.md#aba74653967d3235a132c2982a5a2f5ae)
- [net_stats_vpn::keepalive_rx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#abfc70aed88c4f037757f365e53acdcb9)
- [net_stats_vpn::valid_tx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#ac199357ab8fbf13dceaefe40b3a12ce5)
- [net_stats_vpn::handshake_init_rx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#ac66dac12113dc1e71699587da25688c4)
- [net_stats_vpn::drop_tx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#ada1951a74e4d7faf6ac2819e0cc6573f)
- [net_stats_vpn::invalid_packet_len](../network_core_model_reference/P152_net_stats_vpn_结构体.md#adac60bd39ea0fb623184c438783d243e)
- [net_stats_vpn::handshake_init_tx](../network_core_model_reference/P152_net_stats_vpn_结构体.md#af3b87df2f50f042043830d946b3b0d8a)
- [net_stats_vpn::decrypt_failed](../network_core_model_reference/P152_net_stats_vpn_结构体.md#af40a96c70f8ab09f3f8a02317fafad6b)
- [net_stats_vpn::invalid_ip_version](../network_core_model_reference/P152_net_stats_vpn_结构体.md#af636ef839bd6e873cd3e88d2ca5dd535)
- [wireguard_allowed_ip::addr](../network_service_model_reference/P070_wireguard_allowed_ip_结构体.md#a8aa426557b26b39e0d75378bb3b6191a)
- [wireguard_allowed_ip::mask_len](../network_service_model_reference/P070_wireguard_allowed_ip_结构体.md#a8fa36acaced72872623cdd31c263f53f)
- [wireguard_allowed_ip::is_valid](../network_service_model_reference/P070_wireguard_allowed_ip_结构体.md#afc296b40c62a86ee8beb311fbbab3655)
- [wireguard_peer_config::timestamp](../network_service_model_reference/P071_wireguard_peer_config_结构体.md#a67b63a434cf1d5147dcf988e85b7b958)
- [wireguard_peer_config::keepalive_interval](../network_service_model_reference/P071_wireguard_peer_config_结构体.md#a8728365d722ac2bb857cbf4e9eb82d97)
- [wireguard_peer_config::preshared_key](../network_service_model_reference/P071_wireguard_peer_config_结构体.md#a9632752c8cecccee550548d9b1c3ba97)
- [wireguard_peer_config::public_key](../network_service_model_reference/P071_wireguard_peer_config_结构体.md#a9ae02999964a23bdcd008648f99067b1)
- [wireguard_peer_config::endpoint_ip](../network_service_model_reference/P071_wireguard_peer_config_结构体.md#ab31a019c4af3e819f06c02171237ccba)
- [wireguard_peer_config::allowed_ip](../network_service_model_reference/P071_wireguard_peer_config_结构体.md#aca7a334729c726198894e22a2cdb446c)

---

[上一章](P920_wifi_utils.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P922_wisblock-io-slot.h_源码浏览.md)
