---
id: learning.zephyr-docs.api-source-compiler-device-reference.page-4
title: coap_client_tcp.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap__client__tcp_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_coap\_client\_tcp.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/coap__client__tcp_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/coap__client__tcp_8h.html)。

## 4.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00017"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="foldopen00034"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="l00044"></a>
<a id="l00045"></a>
<a id="l00046"></a>
<a id="l00059"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00077"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="foldopen00083"></a>
<a id="l00083"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00089"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="foldopen00097"></a>
<a id="l00097"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00103"></a>
<a id="l00104"></a>
<a id="l00106"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00121"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00124"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="foldopen00130"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00145"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00150"></a>
<a id="foldopen00154"></a>
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
<a id="l00196"></a>
<a id="l00197"></a>
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
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00213"></a>
<a id="l00214"></a>
<a id="l00215"></a>
<a id="l00216"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00222"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00248"></a>
<a id="l00249"></a>
<a id="l00250"></a>
<a id="l00251"></a>
<a id="l00263"></a>
<a id="l00264"></a>
<a id="l00272"></a>
<a id="l00273"></a>
<a id="l00274"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00297"></a>
<a id="l00298"></a>
<a id="l00306"></a>
<a id="l00307"></a>
<a id="l00314"></a>
<a id="l00315"></a>
<a id="l00322"></a>
<a id="l00323"></a>
<a id="l00333"></a>
<a id="l00334"></a>
<a id="l00346"></a>
<a id="l00347"></a>
<a id="l00348"></a>
<a id="l00356"></a>
<a id="l00357"></a>
<a id="l00358"></a>
<a id="l00359"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00367"></a>
<a id="l00368"></a>
<a id="acoap_8h_html"></a>
<a id="acoap__client_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__coap__client__tcp_html_ga0008f54568fe1ea489f052aa98c7cd2c"></a>
<a id="agroup__coap__client__tcp_html_ga04927f52d6f7495c635d0ced1515c3ca"></a>
<a id="agroup__coap__client__tcp_html_ga0857b3d8ccb249e46e636765b0570c8c"></a>
<a id="agroup__coap__client__tcp_html_ga37c2721b11b48b887ab3d6d6374a635a"></a>
<a id="agroup__coap__client__tcp_html_ga3e35576e92b53b22faf458c859339d41"></a>
<a id="agroup__coap__client__tcp_html_ga5a2cdabf25ccd37aa3e2db8aa60d5058"></a>
<a id="agroup__coap__client__tcp_html_ga84b766361341c2494aa127cc0ee1578c"></a>
<a id="agroup__coap__client__tcp_html_ga856f370559bb93b84b66238ce3a031eb"></a>
<a id="agroup__coap__client__tcp_html_ga8a4ec2cb48137f477ae5e3adc352dec7"></a>
<a id="agroup__coap__client__tcp_html_gaaac96d77cd1ee8abeb137717bd076b3e"></a>
<a id="agroup__coap__client__tcp_html_gaabd183897d2d59a23fca6848e463a400"></a>
<a id="agroup__coap__client__tcp_html_gab8b714180fd3bfa728e25abe09a9a8a1"></a>
<a id="agroup__coap__client__tcp_html_gabc8c1782e586f61a4ba196576279baad"></a>
<a id="agroup__coap__client__tcp_html_gacb66929e0d233cf9623845ca9803f34b"></a>
<a id="agroup__coap__client__tcp_html_gad10b972ab7a50a05afae900551f870d0"></a>
<a id="agroup__coap__client__tcp_html_gad7246717e5e1ae1f8664f7fb3c6d1a26"></a>
<a id="agroup__coap__client__tcp_html_gad97f2afc8f4fec4b8b13eb73707ef953"></a>
<a id="agroup__coap__client__tcp_html_gaeb9a69c7b6b91cfa26d63eeb561451c8"></a>
<a id="agroup__coap__client__tcp_html_ggab8b714180fd3bfa728e25abe09a9a8a1a048a67996e4b2dc450d6ee7366c1ab7a"></a>
<a id="agroup__coap__client__tcp_html_ggab8b714180fd3bfa728e25abe09a9a8a1a24082680ef6e1beaae7e7e6422468fe5"></a>
<a id="agroup__coap__client__tcp_html_ggab8b714180fd3bfa728e25abe09a9a8a1a336faab7ec179eaf2911de890ba3a590"></a>
<a id="agroup__coap__client__tcp_html_ggab8b714180fd3bfa728e25abe09a9a8a1a7d39c90561197d76d0c6393e234ac89f"></a>
<a id="agroup__coap__client_html_ga8d16c1066c555e570a97569973809f68"></a>
<a id="agroup__coap_html_ga6a6547e3c755cf7a5033302c8294e0b7"></a>
<a id="agroup__coap_html_ga94a8f9956742d3928fc3c63b8d01ae73"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdlib_8h_html_a4bef6384a1777699c6eba3125e690419"></a>
<a id="astructcoap__block__context_html"></a>
<a id="astructcoap__client__response__data_html"></a>
<a id="astructcoap__client__response__data_html_a4a600d4a686e2029b0a3c00c84d6ebe5"></a>
<a id="astructcoap__client__response__data_html_aac23eadaa55bab0bde1b9a9dd91e4650"></a>
<a id="astructcoap__client__response__data_html_ad8342db8f7aa17740fc3e2688c54312e"></a>
<a id="astructcoap__client__tcp__option_html"></a>
<a id="astructcoap__client__tcp__option_html_a16434738d3cc637181f5cfa5d8c0aa31"></a>
<a id="astructcoap__client__tcp__option_html_a229b8b96d893525ec2b6646eb959a385"></a>
<a id="astructcoap__client__tcp__option_html_ac04accc94f1bbca6906ef5a25af28628"></a>
<a id="astructcoap__client__tcp__request_html"></a>
<a id="astructcoap__client__tcp__request_html_a62c381846bd997abb6cdb07344e84370"></a>
<a id="astructcoap__client__tcp__request_html_a691ab55e31c3a4b51cb427a24273dd54"></a>
<a id="astructcoap__client__tcp__request_html_a8366b8978cb97f9fdcd1a4e7b419754f"></a>
<a id="astructcoap__client__tcp__request_html_a94815f05ca330d252a7800307e401782"></a>
<a id="astructcoap__client__tcp__request_html_a94af7ad3d156eb4a44525481073d5496"></a>
<a id="astructcoap__client__tcp__request_html_a9eacf07abaf9ddd2b8a7bf50c12e0258"></a>
<a id="astructcoap__client__tcp__request_html_aa32cf19f5e76d2c073f8fbb47b314a15"></a>
<a id="astructcoap__client__tcp__request_html_aae2ca57ccfeb43a6d29e47f714e97546"></a>
<a id="astructcoap__client__tcp__request_html_acf52d8cefdef4fef9540e7cd0ca67584"></a>
<a id="astructcoap__client__tcp__request_html_ad2d2fe88ab399178f3a1d8dd72f6cf89"></a>
<a id="astructcoap__packet_html"></a>
<a id="astructnet__sockaddr_html"></a>
<a id="aunioncoap__client__tcp__event__data_html"></a>
<a id="aunioncoap__client__tcp__event__data_html_a71afec4e9cff19d0d5f140f0683f7018"></a>
<a id="aunioncoap__client__tcp__event__data_html_aabf0c77c120433b0ac1d8ff71d938717"></a>
<a id="aunioncoap__client__tcp__event__data_html_acc9999996b787c1b58205a72aa6e3aef"></a>
<a id="aunioncoap__client__tcp__event__data_html_acfe56555936d032169ab875ec61aa385"></a>

```c
/*
 * Copyright (c) 2026 Nordic Semiconductor ASA
 * Copyright (c) 2026 Ellenby Technologies Inc.
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_NET_COAP_CLIENT_TCP_H_
#define ZEPHYR_INCLUDE_NET_COAP_CLIENT_TCP_H_



#include <zephyr/net/coap.h>
#include <zephyr/net/coap_client.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_COAP_TCP_MSG_LEN (CONFIG_COAP_CLIENT_MESSAGE_HEADER_SIZE + \
                              CONFIG_COAP_CLIENT_MESSAGE_SIZE)

typedef void (*coap_client_tcp_response_cb_t)(const struct coap_client_response_data *data,
                                              void *user_data);

typedef int (*coap_client_tcp_payload_cb_t)(size_t offset, const uint8_t **payload,
                                            size_t *len, bool *last_block,
                                            void *user_data);

typedef int (*coap_client_tcp_socket_config_cb_t)(int fd, void *user_data);

/* Forward declaration for event callback */
struct coap_client_tcp;

enum coap_client_tcp_event {
        COAP_CLIENT_TCP_EVENT_CSM_UPDATED,
        COAP_CLIENT_TCP_EVENT_PONG_RECEIVED,
        COAP_CLIENT_TCP_EVENT_RELEASE,
        COAP_CLIENT_TCP_EVENT_ABORT,
};

union coap_client_tcp_event_data {
        struct {
                const char *alt_addr;
                uint32_t hold_off_sec;
        } release;
        struct {
                uint16_t bad_csm_option;
        } abort;
};

typedef void (*coap_client_tcp_event_cb_t)(
        struct coap_client_tcp *client,
        enum coap_client_tcp_event event,
        const union coap_client_tcp_event_data *data,
        void *user_data);

struct coap_client_tcp_option {
        uint16_t code;
#if defined(CONFIG_COAP_EXTENDED_OPTIONS_LEN)
        uint16_t len;
        uint8_t value[CONFIG_COAP_EXTENDED_OPTIONS_LEN_VALUE];
#else
        uint8_t len;
        uint8_t value[MAX_COAP_CLIENT_OPTION_LEN];
#endif
};

#define MAX_TCP_PATH_SIZE (CONFIG_COAP_CLIENT_MAX_PATH_LENGTH + 1)
#define MAX_TCP_EXTRA_OPTIONS CONFIG_COAP_CLIENT_MAX_EXTRA_OPTIONS

struct coap_client_tcp_request {
        enum coap_method method;
        char path[MAX_TCP_PATH_SIZE];
        enum coap_content_format fmt;
        const uint8_t *payload;
        size_t len;
        coap_client_tcp_payload_cb_t payload_cb;
        coap_client_tcp_response_cb_t cb;
        struct coap_client_tcp_option
                options[MAX_TCP_EXTRA_OPTIONS];
        uint8_t num_options;
        void *user_data;
};

struct coap_client_tcp_internal_request {
        uint8_t request_token[COAP_TOKEN_MAX_LEN];
        uint32_t offset;
        uint8_t request_tkl;
        bool request_ongoing;
        atomic_t in_callback;
        struct coap_block_context recv_blk_ctx;
        uint8_t recv_etag[COAP_ETAG_MAX_LEN];
        uint8_t recv_etag_len;
        struct coap_block_context send_blk_ctx;
        struct coap_client_tcp_request coap_request;
        struct coap_packet request;
        uint8_t request_tag[COAP_TOKEN_MAX_LEN];
        uint8_t send_buf[MAX_COAP_TCP_MSG_LEN];

        /* TCP-specific timeout handling (no retransmission) */
        int64_t tcp_t0;
        uint32_t tcp_timeout_ms;

        /* For blockwise transfers */
        uint32_t last_payload_len;

        /* For GETs with observe option set */
        bool is_observe;
};

struct coap_client_tcp {
        int fd;
        struct k_mutex lock;
        uint8_t recv_buf[MAX_COAP_TCP_MSG_LEN];
        size_t recv_offset; /* Bytes received so far into recv_buf */
        struct coap_client_tcp_internal_request requests[CONFIG_COAP_CLIENT_MAX_REQUESTS];
        struct coap_option echo_option;
        bool send_echo;

        /* Max block/message size from CSM negotiation */
        uint32_t max_block_size;

        /* Blockwise transfer capability (negotiated via CSM BWT option) */
        bool blockwise_enabled;

        /* Ping/Pong tracking */
        bool ping_pending;
        int64_t ping_t0;

        /* Event callback for Release/Abort signals */
        coap_client_tcp_event_cb_t event_cb;
        void *event_cb_user_data;

        coap_client_tcp_socket_config_cb_t socket_config_cb;
        void *socket_config_cb_user_data;
};

int coap_client_tcp_init(struct coap_client_tcp *client, const char *info);

int coap_client_tcp_connect(struct coap_client_tcp *client,
                            const struct net_sockaddr *addr,
                            net_socklen_t addrlen, int proto);

int coap_client_tcp_close(struct coap_client_tcp *client);

int coap_client_tcp_req(struct coap_client_tcp *client,
                        struct coap_client_tcp_request *req);

int coap_client_tcp_csm_req(struct coap_client_tcp *client,
                            uint32_t max_block_size,
                            coap_client_tcp_response_cb_t cb,
                            void *user_data);

void coap_client_tcp_cancel_requests(struct coap_client_tcp *client);

void coap_client_tcp_cancel_and_reset_all(struct coap_client_tcp *client);

struct coap_client_tcp_option coap_client_tcp_option_initial_block2(struct coap_client_tcp *client);

bool coap_client_tcp_has_ongoing_exchange(struct coap_client_tcp *client);

int coap_client_tcp_ping(struct coap_client_tcp *client);

int coap_client_tcp_release(struct coap_client_tcp *client,
                            const char *alt_addr, uint32_t hold_off_sec);

void coap_client_tcp_set_event_cb(struct coap_client_tcp *client,
                                  coap_client_tcp_event_cb_t cb,
                                  void *user_data);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_COAP_CLIENT_TCP_H_ */
```

## 4.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2026 Nordic Semiconductor ASA。

版权（Copyright）：© 2026 Ellenby Technologies Inc.。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 77 行

事件回调（event callback）的前置声明。

### 注释 3：原第 184 行

TCP 专用的超时处理（timeout handling），不进行重传。

### 注释 4：原第 188 行

用于分块传输（blockwise transfers）。

### 注释 5：原第 191 行

用于设置了观察选项（Observe Option）的 GET 请求。

### 注释 6：原第 199 行

到目前为止已接收到 `recv_buf` 中的字节数。

### 注释 7：原第 204 行

通过能力与设置消息（CSM）协商得到的最大块／消息大小。

### 注释 8：原第 207 行

分块传输能力（blockwise transfer capability），通过 CSM 的 BWT 选项协商。

### 注释 9：原第 210 行

Ping/Pong 跟踪。

### 注释 10：原第 214 行

用于 Release/Abort 信号的事件回调。

### 注释 11：原第 368 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_COAP_CLIENT_TCP_H_`。

## 4.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/coap__client__tcp_8h.html)
- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)
- [zephyr/net/coap_client.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__client_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [coap_client_tcp_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gaabd183897d2d59a23fca6848e463a400)
- [coap_client_response_data](../network_application_model_reference/P005_coap_client_response_data_结构体.md)
- [coap_client_tcp_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gad97f2afc8f4fec4b8b13eb73707ef953)
- [offset](../network_application_model_reference/P005_coap_client_response_data_结构体.md#ad8342db8f7aa17740fc3e2688c54312e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [payload](../network_application_model_reference/P005_coap_client_response_data_结构体.md#a4a600d4a686e2029b0a3c00c84d6ebe5)
- [last_block](../network_application_model_reference/P005_coap_client_response_data_结构体.md#aac23eadaa55bab0bde1b9a9dd91e4650)
- [coap_client_tcp_socket_config_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga8a4ec2cb48137f477ae5e3adc352dec7)
- [coap_client_tcp_event](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gab8b714180fd3bfa728e25abe09a9a8a1)
- [COAP_CLIENT_TCP_EVENT_CSM_UPDATED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ggab8b714180fd3bfa728e25abe09a9a8a1a24082680ef6e1beaae7e7e6422468fe5)
- [COAP_CLIENT_TCP_EVENT_PONG_RECEIVED](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ggab8b714180fd3bfa728e25abe09a9a8a1a7d39c90561197d76d0c6393e234ac89f)
- [COAP_CLIENT_TCP_EVENT_RELEASE](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ggab8b714180fd3bfa728e25abe09a9a8a1a048a67996e4b2dc450d6ee7366c1ab7a)
- [COAP_CLIENT_TCP_EVENT_ABORT](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ggab8b714180fd3bfa728e25abe09a9a8a1a336faab7ec179eaf2911de890ba3a590)
- [coap_client_tcp_event_data](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md)
- [alt_addr](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md#acfe56555936d032169ab875ec61aa385)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [hold_off_sec](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md#a71afec4e9cff19d0d5f140f0683f7018)
- [release](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md#aabf0c77c120433b0ac1d8ff71d938717)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [bad_csm_option](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md#acc9999996b787c1b58205a72aa6e3aef)
- [abort](../api_file_reference/P410_____w__zephyr__zephyr__lib__libc__minimal__include__stdlib.h_文件参考.md#a4bef6384a1777699c6eba3125e690419)
- [coap_client_tcp_event_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga04927f52d6f7495c635d0ced1515c3ca)
- [coap_client_tcp_option](../network_application_model_reference/P006_coap_client_tcp_option_结构体.md)
- [code](../network_application_model_reference/P006_coap_client_tcp_option_结构体.md#a229b8b96d893525ec2b6646eb959a385)
- [len](../network_application_model_reference/P006_coap_client_tcp_option_结构体.md#ac04accc94f1bbca6906ef5a25af28628)
- [value](../network_application_model_reference/P006_coap_client_tcp_option_结构体.md#a16434738d3cc637181f5cfa5d8c0aa31)
- [MAX_COAP_CLIENT_OPTION_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga8d16c1066c555e570a97569973809f68)
- [coap_client_tcp_request](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md)
- [coap_method](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6a6547e3c755cf7a5033302c8294e0b7)
- [method](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#a62c381846bd997abb6cdb07344e84370)
- [path](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#a691ab55e31c3a4b51cb427a24273dd54)
- [coap_content_format](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga94a8f9956742d3928fc3c63b8d01ae73)
- [fmt](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#ad2d2fe88ab399178f3a1d8dd72f6cf89)
- [payload](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#aa32cf19f5e76d2c073f8fbb47b314a15)
- [len](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#a94815f05ca330d252a7800307e401782)
- [payload_cb](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#acf52d8cefdef4fef9540e7cd0ca67584)
- [cb](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#a8366b8978cb97f9fdcd1a4e7b419754f)
- [options](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#a94af7ad3d156eb4a44525481073d5496)
- [num_options](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#a9eacf07abaf9ddd2b8a7bf50c12e0258)
- [user_data](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#aae2ca57ccfeb43a6d29e47f714e97546)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)
- [coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)
- [MAX_COAP_TCP_MSG_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gacb66929e0d233cf9623845ca9803f34b)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [coap_client_tcp_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gaeb9a69c7b6b91cfa26d63eeb561451c8)
- [coap_client_tcp_connect](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gabc8c1782e586f61a4ba196576279baad)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [coap_client_tcp_close](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga84b766361341c2494aa127cc0ee1578c)
- [coap_client_tcp_req](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gaaac96d77cd1ee8abeb137717bd076b3e)
- [coap_client_tcp_csm_req](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga856f370559bb93b84b66238ce3a031eb)
- [coap_client_tcp_cancel_requests](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga5a2cdabf25ccd37aa3e2db8aa60d5058)
- [coap_client_tcp_cancel_and_reset_all](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga0008f54568fe1ea489f052aa98c7cd2c)
- [coap_client_tcp_option_initial_block2](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga0857b3d8ccb249e46e636765b0570c8c)
- [coap_client_tcp_has_ongoing_exchange](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga3e35576e92b53b22faf458c859339d41)
- [coap_client_tcp_ping](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gad10b972ab7a50a05afae900551f870d0)
- [coap_client_tcp_release](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#ga37c2721b11b48b887ab3d6d6374a635a)
- [coap_client_tcp_set_event_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client__tcp.html#gad7246717e5e1ae1f8664f7fb3c6d1a26)
- [coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)
- [coap_client.h](https://docs.zephyrproject.org/latest/doxygen/html/coap__client_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [coap_client_response_data::payload](../network_application_model_reference/P005_coap_client_response_data_结构体.md#a4a600d4a686e2029b0a3c00c84d6ebe5)
- [coap_client_response_data::last_block](../network_application_model_reference/P005_coap_client_response_data_结构体.md#aac23eadaa55bab0bde1b9a9dd91e4650)
- [coap_client_response_data::offset](../network_application_model_reference/P005_coap_client_response_data_结构体.md#ad8342db8f7aa17740fc3e2688c54312e)
- [coap_client_tcp_option::value](../network_application_model_reference/P006_coap_client_tcp_option_结构体.md#a16434738d3cc637181f5cfa5d8c0aa31)
- [coap_client_tcp_option::code](../network_application_model_reference/P006_coap_client_tcp_option_结构体.md#a229b8b96d893525ec2b6646eb959a385)
- [coap_client_tcp_option::len](../network_application_model_reference/P006_coap_client_tcp_option_结构体.md#ac04accc94f1bbca6906ef5a25af28628)
- [coap_client_tcp_request::method](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#a62c381846bd997abb6cdb07344e84370)
- [coap_client_tcp_request::path](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#a691ab55e31c3a4b51cb427a24273dd54)
- [coap_client_tcp_request::cb](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#a8366b8978cb97f9fdcd1a4e7b419754f)
- [coap_client_tcp_request::len](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#a94815f05ca330d252a7800307e401782)
- [coap_client_tcp_request::options](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#a94af7ad3d156eb4a44525481073d5496)
- [coap_client_tcp_request::num_options](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#a9eacf07abaf9ddd2b8a7bf50c12e0258)
- [coap_client_tcp_request::payload](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#aa32cf19f5e76d2c073f8fbb47b314a15)
- [coap_client_tcp_request::user_data](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#aae2ca57ccfeb43a6d29e47f714e97546)
- [coap_client_tcp_request::payload_cb](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#acf52d8cefdef4fef9540e7cd0ca67584)
- [coap_client_tcp_request::fmt](../network_application_model_reference/P007_coap_client_tcp_request_结构体.md#ad2d2fe88ab399178f3a1d8dd72f6cf89)
- [coap_client_tcp_event_data::hold_off_sec](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md#a71afec4e9cff19d0d5f140f0683f7018)
- [coap_client_tcp_event_data::release](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md#aabf0c77c120433b0ac1d8ff71d938717)
- [coap_client_tcp_event_data::bad_csm_option](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md#acc9999996b787c1b58205a72aa6e3aef)
- [coap_client_tcp_event_data::alt_addr](../network_application_model_reference/P090_coap_client_tcp_event_data_联合体.md#acfe56555936d032169ab875ec61aa385)

---

[上一章](P003_cdb.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P005_dap_link.h_源码浏览.md)
