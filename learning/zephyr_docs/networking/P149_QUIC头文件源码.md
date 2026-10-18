---
id: learning.zephyr-docs.networking.api-149
title: QUIC头文件源码
kind: reference
status: maintained
domains: [zephyr, networking, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/quic_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第149章\_QUIC头文件源码

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/quic_8h_source.html)。读取日期：2026-10-14；基线为保存的 `latest` 页面，HTML 摘要见[来源记录](../SOURCES.md)。

## 149.1\_阅读说明与来源

译注：先读[QUIC传输接口指南](P143_QUIC传输接口.md)及[回显示例目录](P144_QUIC示例目录.md)，理解连接套接字、流套接字和 TLS 握手的关系，再按符号查询本组参考。

本组：[完整API参考](P147_QUIC完整API参考.md) · [头文件参考](P148_QUIC头文件参考.md) · [头文件源码](P149_QUIC头文件源码.md) · [会话状态](P150_QUIC会话状态.md) · [会话传输参数](P151_QUIC会话传输参数.md) · [统计数据](P152_QUIC统计数据.md) · [全局统计](P153_QUIC全局统计数据.md)。

下方保留官方 Doxygen 源码浏览页展示的全部代码、标识符和版权／许可注释。仅移除网页行号，将展示用不换行空格还原为空格，并清除行尾空白。原页面已省略用于生成 API 文档的部分注释，行号原本存在跳跃；本展示不能替代完整原始头文件。接口、参数和结构体注释均在本组参考页翻译。

## 149.2\_原始源码展示

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
<a id="foldopen00039"></a>
<a id="l00039"></a>
<a id="l00041"></a>
<a id="l00043"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00059"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00065"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="foldopen00073"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00077"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00095"></a>
<a id="l00095"></a>
<a id="l00096"></a>
<a id="l00097"></a>
<a id="l00098"></a>
<a id="l00099"></a>
<a id="foldopen00101"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00112"></a>
<a id="l00113"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00136"></a>
<a id="l00150"></a>
<a id="l00151"></a>
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00175"></a>
<a id="l00176"></a>
<a id="l00184"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00188"></a>
<a id="l00189"></a>
<a id="l00191"></a>
<a id="l00192"></a>
<a id="l00194"></a>
<a id="l00195"></a>
<a id="foldopen00203"></a>
<a id="l00203"></a>
<a id="l00205"></a>
<a id="l00207"></a>
<a id="l00209"></a>
<a id="l00211"></a>
<a id="l00213"></a>
<a id="l00215"></a>
<a id="l00217"></a>
<a id="l00219"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="foldopen00230"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00234"></a>
<a id="l00236"></a>
<a id="l00238"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00248"></a>
<a id="l00250"></a>
<a id="l00252"></a>
<a id="l00254"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00319"></a>
<a id="l00320"></a>
<a id="l00328"></a>
<a id="l00329"></a>
<a id="l00337"></a>
<a id="l00338"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00349"></a>
<a id="l00350"></a>
<a id="l00351"></a>
<a id="l00352"></a>
<a id="l00353"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="agroup__quic_html_ga19d171ac47d79394d58b371b43585786"></a>
<a id="agroup__quic_html_ga290d25ba3fe401d61b0c35556e67a04c"></a>
<a id="agroup__quic_html_ga2d32dd11cff3f02426749955f5a72bd8"></a>
<a id="agroup__quic_html_ga520012661ae348538e817e3cfed35a70"></a>
<a id="agroup__quic_html_ga6ae488ec3f462f5a15c8b3106f293ad2"></a>
<a id="agroup__quic_html_ga6c21dda81654cab53209bc1dca4909d2"></a>
<a id="agroup__quic_html_ga8c36dbae839efb95be6ea6a8c98f8847"></a>
<a id="agroup__quic_html_ga8f757a00b692d8eaa39536557f326306"></a>
<a id="agroup__quic_html_gac5b95872bf7fa74b7a1d2c7b011fd99f"></a>
<a id="agroup__quic_html_gade13e997f7a3f9c79590c56ef2bb72c3"></a>
<a id="agroup__quic_html_gae1501fa858907f12bd308442425ebeeb"></a>
<a id="agroup__quic_html_gga006f049efb2b5a9e3ff7821434edc93ba05f712f8a31261e125468735d4c46bc8"></a>
<a id="agroup__quic_html_gga006f049efb2b5a9e3ff7821434edc93ba349bcf4a847826cd63e174ceaaa33f1e"></a>
<a id="agroup__quic_html_gga006f049efb2b5a9e3ff7821434edc93ba5f816ebe05cd77bbe7111337bbce49cc"></a>
<a id="agroup__quic_html_gga006f049efb2b5a9e3ff7821434edc93ba6222ebc1d597ca2dc9203db51c0bbdfe"></a>
<a id="agroup__quic_html_gga006f049efb2b5a9e3ff7821434edc93ba75de1d0c9aa28a01e0f9c6b36ba2f90f"></a>
<a id="agroup__quic_html_gga006f049efb2b5a9e3ff7821434edc93ba82c17b20fa9ffbfa2ce1430767734d05"></a>
<a id="agroup__quic_html_gga006f049efb2b5a9e3ff7821434edc93bab8ad7ba1d668055e6842651f768ec41b"></a>
<a id="agroup__quic_html_gga006f049efb2b5a9e3ff7821434edc93baeb6f405c6e2ffa93d3ad64f6ee854b06"></a>
<a id="agroup__quic_html_gga290d25ba3fe401d61b0c35556e67a04caed835dd5e19cbbf3f9d4e1a98017084f"></a>
<a id="agroup__quic_html_gga290d25ba3fe401d61b0c35556e67a04caef4a4cac2a980c26800f5ace0e1f5a55"></a>
<a id="agroup__quic_html_gga8c36dbae839efb95be6ea6a8c98f8847a5c654090eb3849cfc67e62168abb5ae1"></a>
<a id="agroup__quic_html_gga8c36dbae839efb95be6ea6a8c98f8847a5e1a358566686da7522ba96b2c8de3f1"></a>
<a id="ainclude_2zephyr_2types_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a2095b9bffea4b2656950c6c0419edbf1"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="astructnet__stats__quic__global_html"></a>
<a id="astructnet__stats__quic__global_html_a4dc2127f494e0d30a77476d64c5a6618"></a>
<a id="astructnet__stats__quic__global_html_a5aff8a6fc934624e6f400c95f5e5a1d0"></a>
<a id="astructnet__stats__quic__global_html_a61f59a107c296f0bf12b39edc699c3a7"></a>
<a id="astructnet__stats__quic__global_html_a828ecf5f479709cbcb3efcec3e3378b8"></a>
<a id="astructnet__stats__quic__global_html_a93a56f2b3e09fde2b1e0a06e1d109c1c"></a>
<a id="astructnet__stats__quic__global_html_aa19241ebc473b9f1433455f53ee663bd"></a>
<a id="astructnet__stats__quic__global_html_ab42d5446da9d7316b6ebb3cbf82a2dea"></a>
<a id="astructnet__stats__quic__global_html_ac7072fb6d9d5a4fe500f2b2ce44cb38b"></a>
<a id="astructnet__stats__quic__global_html_aeee6bcc9a4e292bbda5279caeddcfad7"></a>
<a id="astructnet__stats__quic_html"></a>
<a id="astructnet__stats__quic_html_a1cb94d0aad126499605ff0fd55a9c921"></a>
<a id="astructnet__stats__quic_html_a1fc16ecebf7520992168960c1075c7ea"></a>
<a id="astructnet__stats__quic_html_a3295a98cb2d8739d1162024f82e8fabd"></a>
<a id="astructnet__stats__quic_html_a379af69fa7b7709ceeb59ff5f69f9f0d"></a>
<a id="astructnet__stats__quic_html_a37ed9533ed28547b796a96806e96d3f2"></a>
<a id="astructnet__stats__quic_html_a4f0635d82af4c8820b881f700733f4c6"></a>
<a id="astructnet__stats__quic_html_a71ab60160b7053da6f65b34f6940ac5c"></a>
<a id="astructnet__stats__quic_html_a98554e8744477353c9d68377ea2717e8"></a>
<a id="astructnet__stats__quic_html_a9e6c36c55d518d601d18c213ab957f7a"></a>
<a id="astructnet__stats__quic_html_ab654695fadc0e6c8f12b19d32ac3b557"></a>
<a id="astructnet__stats__quic_html_ab940f3fa00526b78c9e25f664635b2cc"></a>
<a id="astructnet__stats__quic_html_abc28dda5b520ed707fd757ba18e5446f"></a>
<a id="astructnet__stats__quic_html_abd662d512982b4dcda59551a828fd768"></a>
<a id="astructnet__stats__quic_html_ac821e5206622610f1ac6619901d4aa0d"></a>
<a id="astructnet__stats__quic_html_ae8510e001e5188474836ce808eb3fe73"></a>
<a id="astructquic__session__state_html"></a>
<a id="astructquic__session__state_html_a15df59733196120323fc69c5f3b0306e"></a>
<a id="astructquic__session__state_html_a1ec2b67e34265eb62160a73b05ab724e"></a>
<a id="astructquic__session__state_html_a3eabe1807a38a5ef29d6ca9f36d206c7"></a>
<a id="astructquic__session__state_html_a56c6f48a588efb749ffe76d832331c9e"></a>
<a id="astructquic__session__state_html_a7144ad5f980931a49c2d3c93547c4f82"></a>
<a id="astructquic__session__state_html_ac9a0a0146cf97781402e6d49a2b400c9"></a>
<a id="astructquic__session__state_html_ace39205048525dca62d52eccdd4d3d8d"></a>
<a id="astructquic__session__state_html_add0f4633826fa0b1ba21269eb16dc541"></a>
<a id="astructquic__session__state_html_ae82a2ea1627494446e68eb374ea649b7"></a>
<a id="astructquic__session__state_html_aed88babe2f43f163983ae4894b531fb4"></a>
<a id="astructquic__session__state_html_afbf1dad97be7deb3e8988f440b8f09f3"></a>
<a id="astructquic__session__transport__params_html"></a>
<a id="astructquic__session__transport__params_html_a025a059a8b630be61e128cd108bea4ad"></a>
<a id="astructquic__session__transport__params_html_a5ea1c1f18506ac03b9c40effd843e1a2"></a>
<a id="astructquic__session__transport__params_html_a7ddc746aa834fbc97192f99ca5042128"></a>
<a id="astructquic__session__transport__params_html_a841404605dc741a8f3d52e31e9d2f102"></a>
<a id="astructquic__session__transport__params_html_a8955b20664d98dc46956e54fae75ac3c"></a>
<a id="astructquic__session__transport__params_html_aa8ddb2d0324be686e4de72ce46d6de1b"></a>
<a id="astructquic__session__transport__params_html_ad8219a81f06c0977fd25721061c2bf9c"></a>
<a id="astructquic__session__transport__params_html_af5b1546f88f1713ffd4d7fa2c54dbeb0"></a>
<a id="astructquic__session__transport__params_html_af782abfbd2085b9454f2a3341c3346e2"></a>

```c
/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */


#ifndef ZEPHYR_INCLUDE_NET_QUIC_H_
#define ZEPHYR_INCLUDE_NET_QUIC_H_


#include <zephyr/types.h>
#include <stddef.h>
#include <stdbool.h>
#include <zephyr/net/net_ip.h>

#ifdef __cplusplus
extern "C" {
#endif

struct net_stats_quic {
        uint32_t handshake_init_rx;
        uint32_t handshake_init_tx;
        uint32_t handshake_resp_rx;
        uint32_t handshake_resp_tx;
        uint32_t invalid_handshake;
        uint32_t peer_not_found;
        uint32_t invalid_packet;
        uint32_t invalid_key;
        uint32_t invalid_packet_len;
        uint32_t decrypt_failed;
        uint32_t drop_rx;
        uint32_t drop_tx;
        uint32_t alloc_failed;
        uint32_t valid_rx;
        uint32_t valid_tx;
};

struct net_stats_quic_global {
        uint32_t packets_rx;
        uint32_t connections_opened;
        uint32_t connections_closed;
        uint32_t streams_opened;
        uint32_t streams_closed;
        uint32_t connection_open_failed;
        uint32_t stream_open_failed;
        uint32_t connection_close_failed;
        uint32_t stream_close_failed;
};

enum quic_stream_direction {
        QUIC_STREAM_BIDIRECTIONAL  = 0x00,
        QUIC_STREAM_UNIDIRECTIONAL = 0x02,
};

enum quic_stream_initiator {
        QUIC_STREAM_CLIENT = 0x00,
        QUIC_STREAM_SERVER = 0x01,
};

#define ZSOCK_SOL_QUIC 284

enum {
        ZSOCK_QUIC_SO_STREAM_TYPE = 1,

        ZSOCK_QUIC_SO_CERT_CHAIN_ADD = 2,

        ZSOCK_QUIC_SO_CERT_CHAIN_DEL = 3,

        ZSOCK_QUIC_SO_STOP_SENDING_CODE = 4,

        ZSOCK_QUIC_SO_SESSION_STATE = 5,

        ZSOCK_QUIC_SO_SESSION_TICKET_ENABLE = 6,

        ZSOCK_QUIC_SO_MAX_EARLY_DATA_SIZE = 7,

        ZSOCK_QUIC_SO_STREAM_EARLY_DATA = 8,
};

#define QUIC_SESSION_STATE_VERSION 2U

#define QUIC_MAX_SESSION_TICKET_LEN 256U

#define QUIC_MAX_RESUMPTION_PSK_LEN 48U

struct quic_session_transport_params {
        bool valid;
        uint64_t initial_max_data;
        uint64_t initial_max_stream_data_bidi_local;
        uint64_t initial_max_stream_data_bidi_remote;
        uint64_t initial_max_stream_data_uni;
        uint64_t initial_max_streams_bidi;
        uint64_t initial_max_streams_uni;
        uint64_t max_idle_timeout;
        uint16_t max_udp_payload_size;
};

struct quic_session_state {
        uint16_t version;
        uint16_t cipher_suite;
        uint32_t ticket_lifetime;
        uint32_t ticket_age_add;
        uint32_t max_early_data_size;
        uint64_t issue_time_ms;
        uint16_t ticket_len;
        uint16_t psk_len;
        uint8_t ticket[QUIC_MAX_SESSION_TICKET_LEN];
        uint8_t psk[QUIC_MAX_RESUMPTION_PSK_LEN];
        struct quic_session_transport_params transport_params;
};

int quic_connection_open(const struct net_sockaddr *remote_addr,
                         const struct net_sockaddr *local_addr);

int quic_connection_close(int sock);

int quic_stream_open(int connection_sock,
                     enum quic_stream_initiator initiator,
                     enum quic_stream_direction direction,
                     uint8_t priority);

int quic_stream_close(int sock);

bool quic_is_stream_socket(int sock);

bool quic_is_connection_socket(int sock);

int quic_stream_get_id(int sock, uint64_t *stream_id);


#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_QUIC_H_ */
```

## 149.3\_源码注释译文

版权：2026 年 Nordic Semiconductor ASA；许可证标识为 `Apache-2.0`。原始法律署名保持原样。末尾 `#endif` 注释表示结束头文件包含保护（Header Include Guard）`ZEPHYR_INCLUDE_NET_QUIC_H_`。`extern "C"` 条件块为 C++ 调用方提供 C 链接约定。

## 149.4\_相关源码与使用边界

声明来自 `<zephyr/net/quic.h>`。本仓库的[对应头文件](../../../include/zephyr/net/quic.h)可用于源码追踪，版本可能与官网 `latest` 不同；官方原始头文件及实现的读取摘要见[来源记录](../SOURCES.md)。

[上一章](P148_QUIC头文件参考.md) · [返回大纲](大纲.md) · [下一章](P150_QUIC会话状态.md)
