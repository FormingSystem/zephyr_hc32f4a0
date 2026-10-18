---
id: learning.zephyr-docs.api-source-system-reference.page-6
title: coap_client.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/coap__client_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_coap\_client.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/coap__client_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/coap__client_8h.html)。

## 6.1\_原始可见代码（Source Code）

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
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="l00028"></a>
<a id="l00029"></a>
<a id="l00030"></a>
<a id="foldopen00032"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00036"></a>
<a id="foldopen00040"></a>
<a id="l00040"></a>
<a id="l00045"></a>
<a id="l00047"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00053"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00061"></a>
<a id="l00062"></a>
<a id="l00067"></a>
<a id="l00068"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00118"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00121"></a>
<a id="foldopen00125"></a>
<a id="l00125"></a>
<a id="l00127"></a>
<a id="l00128"></a>
<a id="l00130"></a>
<a id="l00132"></a>
<a id="l00133"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00139"></a>
<a id="l00140"></a>
<a id="l00142"></a>
<a id="l00143"></a>
<a id="l00145"></a>
<a id="foldopen00149"></a>
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
<a id="l00159"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00162"></a>
<a id="l00172"></a>
<a id="l00173"></a>
<a id="l00174"></a>
<a id="l00175"></a>
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
<a id="l00218"></a>
<a id="foldopen00222"></a>
<a id="l00222"></a>
<a id="l00224"></a>
<a id="l00225"></a>
<a id="l00226"></a>
<a id="l00227"></a>
<a id="l00228"></a>
<a id="l00229"></a>
<a id="l00231"></a>
<a id="l00232"></a>
<a id="l00242"></a>
<a id="l00243"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00276"></a>
<a id="l00277"></a>
<a id="l00288"></a>
<a id="l00289"></a>
<a id="l00303"></a>
<a id="l00304"></a>
<a id="l00325"></a>
<a id="l00326"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00373"></a>
<a id="l00374"></a>
<a id="l00390"></a>
<a id="l00391"></a>
<a id="l00392"></a>
<a id="l00393"></a>
<a id="l00394"></a>
<a id="l00395"></a>
<a id="l00399"></a>
<a id="l00400"></a>
<a id="acoap_8h_html"></a>
<a id="agroup__atomic__apis_html_ga124f07c3a788e53c3a40e4e1c06d8af8"></a>
<a id="agroup__coap__client_html_ga17f5d111a03ca0c02b83f5ad96c1caa8"></a>
<a id="agroup__coap__client_html_ga37e6c0891c3e8eef3316e34d4b7a0318"></a>
<a id="agroup__coap__client_html_ga3c35cc0227385124d0ebe25688e3bc1a"></a>
<a id="agroup__coap__client_html_ga3f511d4df22bece05c1ac97ff4d09a80"></a>
<a id="agroup__coap__client_html_ga437ead308ea92f314fd9ebb82a6300b7"></a>
<a id="agroup__coap__client_html_ga53c57dcb241786b6e0213a7198667bd0"></a>
<a id="agroup__coap__client_html_ga71abc48834df15e7550f7f9c75918117"></a>
<a id="agroup__coap__client_html_ga7453fafdd924ae0728694e9fb62682aa"></a>
<a id="agroup__coap__client_html_ga8d16c1066c555e570a97569973809f68"></a>
<a id="agroup__coap__client_html_ga9460711a90567fccb810fb4d93dbe841"></a>
<a id="agroup__coap__client_html_gab5a2ea7ca1852e14142b579f77bc5bf9"></a>
<a id="agroup__coap__client_html_gac85c4bcbc129b5d2be6a74f9024c84d9"></a>
<a id="agroup__coap_html_ga6a6547e3c755cf7a5033302c8294e0b7"></a>
<a id="agroup__coap_html_ga94a8f9956742d3928fc3c63b8d01ae73"></a>
<a id="agroup__ip__4__6_html_ga361fe60d9b96001f74363788352858a0"></a>
<a id="akernel_8h_html"></a>
<a id="astdint_8h_html_a0a8582351ac627ee8bde2973c825e47f"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astdint_8h_html_ac714c0d2c1a4adb10e73cab29623314b"></a>
<a id="astdint_8h_html_afe270aee8d96ad7f279a4020b9d58bdf"></a>
<a id="astructcoap__block__context_html"></a>
<a id="astructcoap__client__option_html"></a>
<a id="astructcoap__client__option_html_a3b0c23802edd7cbb162bff6cfb745bfb"></a>
<a id="astructcoap__client__option_html_ac60b63a5fd1e7ba8f1f3d232828c60ae"></a>
<a id="astructcoap__client__option_html_aebc27705f851af910757f0bb2a73bbe5"></a>
<a id="astructcoap__client__request_html"></a>
<a id="astructcoap__client__request_html_a03f9aec935feab0352254f2d425c59be"></a>
<a id="astructcoap__client__request_html_a04e7fd6614e0a4b0a0e78f5420019582"></a>
<a id="astructcoap__client__request_html_a14e1036a45b1bcfa60faaa5b158b535a"></a>
<a id="astructcoap__client__request_html_a308709b298a7449d32492ee1170a6791"></a>
<a id="astructcoap__client__request_html_a333d2ed265a1a002c1ce116057d6e454"></a>
<a id="astructcoap__client__request_html_a4db33f53cd9723d5c073d379578e5a18"></a>
<a id="astructcoap__client__request_html_a5ed6e1221dff24cc5d86a00c68620a36"></a>
<a id="astructcoap__client__request_html_aa50684b8d2c429eb2accc32a0c2908de"></a>
<a id="astructcoap__client__request_html_aca43b59a62328be1d87901ab3e30f399"></a>
<a id="astructcoap__client__request_html_ad725d95c1745d19e74d3ed39710b10b4"></a>
<a id="astructcoap__client__request_html_ae0a506b0baef3133f8665a5c8799e8d3"></a>
<a id="astructcoap__client__request_html_aefc85ec14f031aabe5ed0830d819069a"></a>
<a id="astructcoap__client__response__data_html"></a>
<a id="astructcoap__client__response__data_html_a4a600d4a686e2029b0a3c00c84d6ebe5"></a>
<a id="astructcoap__client__response__data_html_a5219445f266949bf3981a7dd337bb318"></a>
<a id="astructcoap__client__response__data_html_a8a0ac5afbab9feba492a31e2bf27c29f"></a>
<a id="astructcoap__client__response__data_html_aa4f0deb7f1c8462554f0d3c1904ab099"></a>
<a id="astructcoap__client__response__data_html_aac23eadaa55bab0bde1b9a9dd91e4650"></a>
<a id="astructcoap__client__response__data_html_ab11643c1c070644970889c3d53e0f26e"></a>
<a id="astructcoap__client__response__data_html_abdf9e0a188dbddb2a8c7390be53f4135"></a>
<a id="astructcoap__client__response__data_html_ad8342db8f7aa17740fc3e2688c54312e"></a>
<a id="astructcoap__client_html"></a>
<a id="astructcoap__option_html"></a>
<a id="astructcoap__packet_html"></a>
<a id="astructcoap__pending_html"></a>
<a id="astructcoap__transmission__parameters_html"></a>
<a id="astructk__mutex_html"></a>
<a id="astructk__timepoint__t_html"></a>
<a id="astructnet__sockaddr_html"></a>

```c


/*
 * Copyright (c) 2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */
#ifndef ZEPHYR_INCLUDE_NET_COAP_CLIENT_H_
#define ZEPHYR_INCLUDE_NET_COAP_CLIENT_H_


#include <zephyr/net/coap.h>
#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif

#define MAX_COAP_MSG_LEN (CONFIG_COAP_CLIENT_MESSAGE_HEADER_SIZE + \
                          CONFIG_COAP_CLIENT_MESSAGE_SIZE)

#define MAX_COAP_CLIENT_OPTION_LEN (12)

struct coap_client_response_data {
        int16_t result_code;
        const struct coap_packet *packet;
        size_t offset;
        const uint8_t *payload;
        size_t payload_len;
        bool last_block;
#if defined(CONFIG_COAP_CLIENT_MULTICAST) || defined(__DOXYGEN__)
        const struct net_sockaddr *source;

        net_socklen_t source_len;
#endif
};

typedef void (*coap_client_response_cb_t)(const struct coap_client_response_data *data,
                                          void *user_data);

typedef int (*coap_client_payload_cb_t)(size_t offset, const uint8_t **payload,
                                        size_t *len, bool *last_block,
                                        void *user_data);

struct coap_client_option {
        uint16_t code;
#if defined(CONFIG_COAP_EXTENDED_OPTIONS_LEN)
        uint16_t len;
        uint8_t value[CONFIG_COAP_EXTENDED_OPTIONS_LEN_VALUE];
#else
        uint8_t len;
        uint8_t value[MAX_COAP_CLIENT_OPTION_LEN];
#endif
};

#define MAX_PATH_SIZE (CONFIG_COAP_CLIENT_MAX_PATH_LENGTH + 1)
#define MAX_EXTRA_OPTIONS CONFIG_COAP_CLIENT_MAX_EXTRA_OPTIONS

struct coap_client_request {
        enum coap_method method;
        bool confirmable;
        char path[MAX_PATH_SIZE];
        enum coap_content_format fmt;
        const uint8_t *payload;
        size_t len;
        coap_client_payload_cb_t payload_cb;
        coap_client_response_cb_t cb;
        struct coap_client_option
                options[MAX_EXTRA_OPTIONS];
        uint8_t num_options;
        void *user_data;
#if defined(CONFIG_COAP_CLIENT_MULTICAST) || defined(__DOXYGEN__)
        uint32_t multicast_timeout_ms;
#endif
};

struct coap_client_internal_request {
        struct net_sockaddr_storage addr;
        net_socklen_t addrlen;

        uint8_t request_token[COAP_TOKEN_MAX_LEN];
        uint32_t offset;
        uint16_t last_id;
        uint8_t request_tkl;
        bool request_ongoing;
        atomic_t in_callback;
        int unreported_error;
        struct coap_block_context recv_blk_ctx;
        uint8_t recv_etag[COAP_ETAG_MAX_LEN];
        uint8_t recv_etag_len;
        struct coap_block_context send_blk_ctx;
        struct coap_pending pending;
        struct coap_client_request coap_request;
        struct coap_packet request;
        uint8_t request_tag[COAP_TOKEN_MAX_LEN];
        uint8_t send_buf[MAX_COAP_MSG_LEN];

        /* A block-wise receive is in progress, so recv_blk_ctx is valid and
         * further requests of this exchange are continuation retrievals.
         */
        bool recv_blockwise;

        /* For GETs with observe option set */
        bool is_observe;
        /* Observe option value of the freshest accepted notification, < 0 if none */
        int last_observe_seq;
        /* Uptime at which the freshest notification was accepted */
        int64_t last_observe_at;
        int last_response_id;
        uint8_t observe_token[COAP_TOKEN_MAX_LEN]; /* registration token snapshot */
        uint8_t observe_tkl;
#if defined(CONFIG_COAP_CLIENT_MULTICAST)
        bool is_mcast;
        k_timepoint_t mcast_timeout;
#endif
};

struct coap_client {
        int fd;
        struct k_mutex lock;
        uint8_t recv_buf[MAX_COAP_MSG_LEN];
        struct coap_client_internal_request requests[CONFIG_COAP_CLIENT_MAX_REQUESTS];
        struct coap_option echo_option;
        bool send_echo;
};

int coap_client_init(struct coap_client *client, const char *info);


int coap_client_req(struct coap_client *client, int sock, const struct net_sockaddr *addr,
                    struct coap_client_request *req, struct coap_transmission_parameters *params);

void coap_client_cancel_requests(struct coap_client *client);

void coap_client_cancel_request(struct coap_client *client, struct coap_client_request *req);

int coap_client_deregister_observe(struct coap_client *client, struct coap_client_request *req);

int coap_client_reregister_observe(struct coap_client *client, struct coap_client_request *req);

struct coap_client_option coap_client_option_initial_block2(void);

bool coap_client_has_ongoing_exchange(struct coap_client *client);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_COAP_CLIENT_H_ */
```

## 6.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 198 行

正在进行分块接收（Block-Wise Receive），因此 `recv_blk_ctx` 有效；此交换（Exchange）的后续请求用于继续获取剩余内容（Continuation Retrievals）。

### 注释 3：原第 203 行

用于设置了观察选项（Observe Option）的 GET 请求。

### 注释 4：原第 205 行

最近接受的通知（Notification）的观察选项值（Observe Option Value）；尚无通知时小于 0。

### 注释 5：原第 207 行

接受最近通知（Notification）时的系统运行时间（Uptime）。

### 注释 6：原第 210 行

注册令牌快照（Registration Token Snapshot）。

### 注释 7：原第 400 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_COAP_CLIENT_H_`。

## 6.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/coap__client_8h.html)
- [zephyr/net/coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [coap_client_response_data](../network_application_model_reference/P005_coap_client_response_data_结构体.md)
- [int16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#afe270aee8d96ad7f279a4020b9d58bdf)
- [result_code](../network_application_model_reference/P005_coap_client_response_data_结构体.md#a5219445f266949bf3981a7dd337bb318)
- [coap_packet](../network_application_model_reference/P013_coap_packet_结构体.md)
- [packet](../network_application_model_reference/P005_coap_client_response_data_结构体.md#a8a0ac5afbab9feba492a31e2bf27c29f)
- [offset](../network_application_model_reference/P005_coap_client_response_data_结构体.md#ad8342db8f7aa17740fc3e2688c54312e)
- [uint8_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [payload](../network_application_model_reference/P005_coap_client_response_data_结构体.md#a4a600d4a686e2029b0a3c00c84d6ebe5)
- [payload_len](../network_application_model_reference/P005_coap_client_response_data_结构体.md#ab11643c1c070644970889c3d53e0f26e)
- [last_block](../network_application_model_reference/P005_coap_client_response_data_结构体.md#aac23eadaa55bab0bde1b9a9dd91e4650)
- [net_sockaddr](../network_core_model_reference/P117_net_sockaddr_结构体.md)
- [source](../network_application_model_reference/P005_coap_client_response_data_结构体.md#abdf9e0a188dbddb2a8c7390be53f4135)
- [net_socklen_t](https://docs.zephyrproject.org/latest/doxygen/html/group__ip__4__6.html#ga361fe60d9b96001f74363788352858a0)
- [source_len](../network_application_model_reference/P005_coap_client_response_data_结构体.md#aa4f0deb7f1c8462554f0d3c1904ab099)
- [coap_client_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga37e6c0891c3e8eef3316e34d4b7a0318)
- [coap_client_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga3c35cc0227385124d0ebe25688e3bc1a)
- [coap_client_option](../network_application_model_reference/P003_coap_client_option_结构体.md)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [code](../network_application_model_reference/P003_coap_client_option_结构体.md#a3b0c23802edd7cbb162bff6cfb745bfb)
- [len](../network_application_model_reference/P003_coap_client_option_结构体.md#aebc27705f851af910757f0bb2a73bbe5)
- [value](../network_application_model_reference/P003_coap_client_option_结构体.md#ac60b63a5fd1e7ba8f1f3d232828c60ae)
- [MAX_COAP_CLIENT_OPTION_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga8d16c1066c555e570a97569973809f68)
- [coap_client_request](../network_application_model_reference/P004_coap_client_request_结构体.md)
- [coap_method](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga6a6547e3c755cf7a5033302c8294e0b7)
- [method](../network_application_model_reference/P004_coap_client_request_结构体.md#a308709b298a7449d32492ee1170a6791)
- [confirmable](../network_application_model_reference/P004_coap_client_request_结构体.md#a4db33f53cd9723d5c073d379578e5a18)
- [path](../network_application_model_reference/P004_coap_client_request_结构体.md#a5ed6e1221dff24cc5d86a00c68620a36)
- [coap_content_format](https://docs.zephyrproject.org/latest/doxygen/html/group__coap.html#ga94a8f9956742d3928fc3c63b8d01ae73)
- [fmt](../network_application_model_reference/P004_coap_client_request_结构体.md#ae0a506b0baef3133f8665a5c8799e8d3)
- [payload](../network_application_model_reference/P004_coap_client_request_结构体.md#aca43b59a62328be1d87901ab3e30f399)
- [len](../network_application_model_reference/P004_coap_client_request_结构体.md#a04e7fd6614e0a4b0a0e78f5420019582)
- [payload_cb](../network_application_model_reference/P004_coap_client_request_结构体.md#a14e1036a45b1bcfa60faaa5b158b535a)
- [cb](../network_application_model_reference/P004_coap_client_request_结构体.md#aefc85ec14f031aabe5ed0830d819069a)
- [options](../network_application_model_reference/P004_coap_client_request_结构体.md#a333d2ed265a1a002c1ce116057d6e454)
- [num_options](../network_application_model_reference/P004_coap_client_request_结构体.md#a03f9aec935feab0352254f2d425c59be)
- [user_data](../network_application_model_reference/P004_coap_client_request_结构体.md#ad725d95c1745d19e74d3ed39710b10b4)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [multicast_timeout_ms](../network_application_model_reference/P004_coap_client_request_结构体.md#aa50684b8d2c429eb2accc32a0c2908de)
- [atomic_t](../atomic_reference/P001_原子操作公共接口.md#ga124f07c3a788e53c3a40e4e1c06d8af8)
- [coap_block_context](../network_application_model_reference/P001_coap_block_context_结构体.md)
- [coap_pending](../network_application_model_reference/P014_coap_pending_结构体.md)
- [MAX_COAP_MSG_LEN](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga53c57dcb241786b6e0213a7198667bd0)
- [int64_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#ac714c0d2c1a4adb10e73cab29623314b)
- [k_timepoint_t](../timer_reference/P088_内核时间点类型.md)
- [coap_client](../network_application_model_reference/P002_coap_client_结构体.md)
- [k_mutex](../synchronization_reference/P007_内核互斥量结构.md)
- [coap_option](../network_application_model_reference/P010_coap_option_结构体.md)
- [coap_client_init](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#gac85c4bcbc129b5d2be6a74f9024c84d9)
- [coap_client_req](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#gab5a2ea7ca1852e14142b579f77bc5bf9)
- [coap_transmission_parameters](../network_application_model_reference/P017_coap_transmission_parameters_结构体.md)
- [coap_client_cancel_requests](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga3f511d4df22bece05c1ac97ff4d09a80)
- [coap_client_cancel_request](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga71abc48834df15e7550f7f9c75918117)
- [coap_client_deregister_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga7453fafdd924ae0728694e9fb62682aa)
- [coap_client_reregister_observe](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga17f5d111a03ca0c02b83f5ad96c1caa8)
- [coap_client_option_initial_block2](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga437ead308ea92f314fd9ebb82a6300b7)
- [coap_client_has_ongoing_exchange](https://docs.zephyrproject.org/latest/doxygen/html/group__coap__client.html#ga9460711a90567fccb810fb4d93dbe841)
- [coap.h](https://docs.zephyrproject.org/latest/doxygen/html/coap_8h.html)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [coap_client_option::code](../network_application_model_reference/P003_coap_client_option_结构体.md#a3b0c23802edd7cbb162bff6cfb745bfb)
- [coap_client_option::value](../network_application_model_reference/P003_coap_client_option_结构体.md#ac60b63a5fd1e7ba8f1f3d232828c60ae)
- [coap_client_option::len](../network_application_model_reference/P003_coap_client_option_结构体.md#aebc27705f851af910757f0bb2a73bbe5)
- [coap_client_request::num_options](../network_application_model_reference/P004_coap_client_request_结构体.md#a03f9aec935feab0352254f2d425c59be)
- [coap_client_request::len](../network_application_model_reference/P004_coap_client_request_结构体.md#a04e7fd6614e0a4b0a0e78f5420019582)
- [coap_client_request::payload_cb](../network_application_model_reference/P004_coap_client_request_结构体.md#a14e1036a45b1bcfa60faaa5b158b535a)
- [coap_client_request::method](../network_application_model_reference/P004_coap_client_request_结构体.md#a308709b298a7449d32492ee1170a6791)
- [coap_client_request::options](../network_application_model_reference/P004_coap_client_request_结构体.md#a333d2ed265a1a002c1ce116057d6e454)
- [coap_client_request::confirmable](../network_application_model_reference/P004_coap_client_request_结构体.md#a4db33f53cd9723d5c073d379578e5a18)
- [coap_client_request::path](../network_application_model_reference/P004_coap_client_request_结构体.md#a5ed6e1221dff24cc5d86a00c68620a36)
- [coap_client_request::multicast_timeout_ms](../network_application_model_reference/P004_coap_client_request_结构体.md#aa50684b8d2c429eb2accc32a0c2908de)
- [coap_client_request::payload](../network_application_model_reference/P004_coap_client_request_结构体.md#aca43b59a62328be1d87901ab3e30f399)
- [coap_client_request::user_data](../network_application_model_reference/P004_coap_client_request_结构体.md#ad725d95c1745d19e74d3ed39710b10b4)
- [coap_client_request::fmt](../network_application_model_reference/P004_coap_client_request_结构体.md#ae0a506b0baef3133f8665a5c8799e8d3)
- [coap_client_request::cb](../network_application_model_reference/P004_coap_client_request_结构体.md#aefc85ec14f031aabe5ed0830d819069a)
- [coap_client_response_data::payload](../network_application_model_reference/P005_coap_client_response_data_结构体.md#a4a600d4a686e2029b0a3c00c84d6ebe5)
- [coap_client_response_data::result_code](../network_application_model_reference/P005_coap_client_response_data_结构体.md#a5219445f266949bf3981a7dd337bb318)
- [coap_client_response_data::packet](../network_application_model_reference/P005_coap_client_response_data_结构体.md#a8a0ac5afbab9feba492a31e2bf27c29f)
- [coap_client_response_data::source_len](../network_application_model_reference/P005_coap_client_response_data_结构体.md#aa4f0deb7f1c8462554f0d3c1904ab099)
- [coap_client_response_data::last_block](../network_application_model_reference/P005_coap_client_response_data_结构体.md#aac23eadaa55bab0bde1b9a9dd91e4650)
- [coap_client_response_data::payload_len](../network_application_model_reference/P005_coap_client_response_data_结构体.md#ab11643c1c070644970889c3d53e0f26e)
- [coap_client_response_data::source](../network_application_model_reference/P005_coap_client_response_data_结构体.md#abdf9e0a188dbddb2a8c7390be53f4135)
- [coap_client_response_data::offset](../network_application_model_reference/P005_coap_client_response_data_结构体.md#ad8342db8f7aa17740fc3e2688c54312e)

---

[上一章](P005_buf.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P007_cts.h_源码浏览.md)
