---
id: learning.zephyr-docs.api-source-supplement-reference.page-88
title: client.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/http_2client_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第88章\_client.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/http_2client_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/http_2client_8h.html)。

## 88.1\_原始可见代码（Source Code）

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
<a id="l00033"></a>
<a id="l00034"></a>
<a id="l00036"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="l00046"></a>
<a id="foldopen00048"></a>
<a id="l00048"></a>
<a id="l00049"></a>
<a id="l00050"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00089"></a>
<a id="l00090"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00110"></a>
<a id="foldopen00114"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00160"></a>
<a id="l00161"></a>
<a id="l00165"></a>
<a id="l00166"></a>
<a id="l00168"></a>
<a id="l00169"></a>
<a id="l00180"></a>
<a id="l00181"></a>
<a id="l00185"></a>
<a id="l00186"></a>
<a id="l00192"></a>
<a id="l00193"></a>
<a id="l00204"></a>
<a id="l00205"></a>
<a id="l00211"></a>
<a id="l00212"></a>
<a id="l00217"></a>
<a id="l00218"></a>
<a id="l00219"></a>
<a id="l00220"></a>
<a id="l00221"></a>
<a id="l00222"></a>
<a id="l00223"></a>
<a id="l00224"></a>
<a id="foldopen00227"></a>
<a id="l00227"></a>
<a id="l00229"></a>
<a id="l00230"></a>
<a id="l00232"></a>
<a id="l00233"></a>
<a id="l00237"></a>
<a id="l00238"></a>
<a id="l00240"></a>
<a id="l00241"></a>
<a id="l00243"></a>
<a id="l00244"></a>
<a id="l00246"></a>
<a id="l00247"></a>
<a id="l00248"></a>
<a id="foldopen00253"></a>
<a id="l00253"></a>
<a id="l00255"></a>
<a id="l00256"></a>
<a id="l00257"></a>
<a id="l00258"></a>
<a id="l00260"></a>
<a id="l00261"></a>
<a id="l00265"></a>
<a id="l00266"></a>
<a id="l00271"></a>
<a id="l00272"></a>
<a id="l00274"></a>
<a id="l00275"></a>
<a id="l00277"></a>
<a id="l00278"></a>
<a id="l00284"></a>
<a id="l00285"></a>
<a id="l00287"></a>
<a id="l00288"></a>
<a id="l00290"></a>
<a id="l00291"></a>
<a id="l00298"></a>
<a id="l00299"></a>
<a id="l00301"></a>
<a id="l00302"></a>
<a id="l00304"></a>
<a id="l00305"></a>
<a id="l00307"></a>
<a id="l00308"></a>
<a id="l00315"></a>
<a id="l00316"></a>
<a id="l00318"></a>
<a id="l00319"></a>
<a id="l00323"></a>
<a id="l00324"></a>
<a id="l00331"></a>
<a id="l00332"></a>
<a id="l00342"></a>
<a id="l00343"></a>
<a id="l00344"></a>
<a id="l00360"></a>
<a id="l00361"></a>
<a id="l00362"></a>
<a id="l00363"></a>
<a id="l00364"></a>
<a id="l00365"></a>
<a id="l00366"></a>
<a id="l00370"></a>
<a id="l00371"></a>
<a id="agroup__http__client_html_ga04fc31de51404e35b3dfab6261bb8e6d"></a>
<a id="agroup__http__client_html_ga34a431c54c52b86618ca0e27ce3862b4"></a>
<a id="agroup__http__client_html_ga6141c94f7da92b71713079063f3426be"></a>
<a id="agroup__http__client_html_gaa38b6efb03f88d6959273a41b6acac81"></a>
<a id="agroup__http__client_html_gaf46ede77bdc83602c84b9342dd8d30ed"></a>
<a id="agroup__http__client_html_gga04fc31de51404e35b3dfab6261bb8e6da3f75fb095e40bfb4efd2c16059093359"></a>
<a id="agroup__http__client_html_gga04fc31de51404e35b3dfab6261bb8e6da428633ff4a67c00c67fb5cbc23269d61"></a>
<a id="agroup__http__methods_html_gaacd5f203e33ac338ca5cb8f02a3ff3b8"></a>
<a id="akernel_8h_html"></a>
<a id="anet__ip_8h_html"></a>
<a id="aparser_8h_html"></a>
<a id="astdbool_8h_html"></a>
<a id="astdint_8h_html_a0c18914b3041c2f583aba76f418399c2"></a>
<a id="astdint_8h_html_a3cb4a16b0e8d6af0af86d4fd6ba5fd9d"></a>
<a id="astdint_8h_html_a5debae8b2a1ec20a6694c0c443ee399e"></a>
<a id="astructhttp__client__internal__data_html"></a>
<a id="astructhttp__client__internal__data_html_a06509a514b81f2fe72394fe147f3d86f"></a>
<a id="astructhttp__client__internal__data_html_a1620ae6631414c3ba5e462d97deca157"></a>
<a id="astructhttp__client__internal__data_html_a19876ea20cdca3a016d6e260e2795e83"></a>
<a id="astructhttp__client__internal__data_html_a330102d665b6601949eb7331ab45d517"></a>
<a id="astructhttp__client__internal__data_html_a8486d8e8b64474e75cadeb9fb166a4a5"></a>
<a id="astructhttp__client__internal__data_html_aa132cb0366969c04250f64075866227c"></a>
<a id="astructhttp__content__range_html"></a>
<a id="astructhttp__parser__settings_html"></a>
<a id="astructhttp__parser_html"></a>
<a id="astructhttp__request_html"></a>
<a id="astructhttp__request_html_a0da554e18c6b159f55fe12e6ba9fe4ca"></a>
<a id="astructhttp__request_html_a15551f2e8c772479fb7acac20765fa12"></a>
<a id="astructhttp__request_html_a1e610f06e9a8ec05cb0de382163a8c79"></a>
<a id="astructhttp__request_html_a38cad3f92ed5b712f749851bbeed9a2f"></a>
<a id="astructhttp__request_html_a3ed1146d59f33e9042fae421619df27c"></a>
<a id="astructhttp__request_html_a589615592c6c14bdecc03553c395c12f"></a>
<a id="astructhttp__request_html_a6a7573252e31fddb5cad5a6764c486c1"></a>
<a id="astructhttp__request_html_a775ef341a6a85b135b10786e9b4a1cbf"></a>
<a id="astructhttp__request_html_a9da5216bbd27ad54fd11368897ed660f"></a>
<a id="astructhttp__request_html_aa29c2bcb70011c9776c959667e10bcf5"></a>
<a id="astructhttp__request_html_ab6fe0ec09c24302279124043e82f17ff"></a>
<a id="astructhttp__request_html_aba8bf528f3e279d55662eedc9168d25c"></a>
<a id="astructhttp__request_html_abaabd58d149720720ffd61025d58e4a9"></a>
<a id="astructhttp__request_html_abb86ccd0e0801c278ef37a78a4b7a958"></a>
<a id="astructhttp__request_html_abe9fdaab40cac6afb16acc2560dfe7e7"></a>
<a id="astructhttp__request_html_adbfcd3bcaf57205360bad957a13999e6"></a>
<a id="astructhttp__request_html_af201ae38024233307ed2c87684ea70d3"></a>
<a id="astructhttp__request_html_afbe0c199a4a58029bf2d83a0b463639c"></a>
<a id="astructhttp__response_html"></a>
<a id="astructhttp__response_html_a0d28b200a74c150e98b5fc18c61638cc"></a>
<a id="astructhttp__response_html_a0eb2181115c753a3e1676a18d9a3ed59"></a>
<a id="astructhttp__response_html_a1936119331645bb421d4a5dc0d3fffb5"></a>
<a id="astructhttp__response_html_a1f88915f82406ae3592dec32b7430851"></a>
<a id="astructhttp__response_html_a4208cf209674441a25231732aad91f89"></a>
<a id="astructhttp__response_html_a45c8596746f5a359a1e18c95838b59d9"></a>
<a id="astructhttp__response_html_a4f107746bfff244a841b950dd84b8162"></a>
<a id="astructhttp__response_html_a58405582a11aa86892b80133f8b4fa43"></a>
<a id="astructhttp__response_html_a6bf553c9399385afeb921f6abef9a875"></a>
<a id="astructhttp__response_html_a7454c5963b7bb1c5311f77971d0d1d2f"></a>
<a id="astructhttp__response_html_a94cd246204b04992712deefe51fc0c26"></a>
<a id="astructhttp__response_html_aa16de8f3485062bf01b0536e64f58b46"></a>
<a id="astructhttp__response_html_ac713af14995e36c1889291d12803ca18"></a>
<a id="astructhttp__response_html_ade896effa407ccdc5c9a7ef3720e66e2"></a>
<a id="astructhttp__response_html_aedcb476d4055a7ba04516cc7a8ef800f"></a>
<a id="astructhttp__response_html_af306ff4c8424b5abad76037abbfe2833"></a>

```c


/*
 * Copyright (c) 2019 Intel Corporation
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_HTTP_CLIENT_H_
#define ZEPHYR_INCLUDE_NET_HTTP_CLIENT_H_


#include <stdbool.h>

#include <zephyr/kernel.h>
#include <zephyr/net/net_ip.h>
#include <zephyr/net/http/parser.h>

#ifdef __cplusplus
extern "C" {
#endif


#if !defined(HTTP_CRLF)
#define HTTP_CRLF "\r\n"
#endif

#if !defined(HTTP_STATUS_STR_SIZE)
#define HTTP_STATUS_STR_SIZE    32
#endif


enum http_final_call {
        HTTP_DATA_MORE = 0,
        HTTP_DATA_FINAL = 1,
};

struct http_request;
struct http_response;

typedef int (*http_payload_cb_t)(int sock,
                                 struct http_request *req,
                                 void *user_data);

typedef int (*http_header_cb_t)(int sock,
                                struct http_request *req,
                                void *user_data);

typedef int (*http_response_cb_t)(struct http_response *rsp,
                                  enum http_final_call final_data,
                                  void *user_data);

struct http_response {
        const struct http_parser_settings *http_cb;

        http_response_cb_t cb;

        uint8_t *body_frag_start;

        size_t body_frag_len;

        uint8_t *recv_buf;

        size_t recv_buf_len;

        size_t data_len;

        size_t content_length;

        size_t processed;

        char http_status[HTTP_STATUS_STR_SIZE];

        uint16_t http_status_code;

        struct http_content_range content_range;

        uint8_t cl_present : 1;
        uint8_t body_found : 1;
        uint8_t message_complete : 1;
        uint8_t cr_present : 1;
};

struct http_client_internal_data {
        struct http_parser parser;

        struct http_parser_settings parser_settings;

        struct http_response response;

        void *user_data;

        int sock;

        bool aborted;
};

struct http_request {
        struct http_client_internal_data internal;

        /* User should fill in following parameters */

        enum http_method method;

        http_response_cb_t response;

        const struct http_parser_settings *http_cb;

        uint8_t *recv_buf;

        size_t recv_buf_len;

        size_t data_len;

        const char *url;

        const char *protocol;

        const char * const *header_fields;

        const char *content_type_value;

        const char *host;

        const char *port;

        http_payload_cb_t payload_cb;

        const char *payload;

        size_t payload_len;

        http_header_cb_t optional_headers_cb;

        const char **optional_headers;
};

int http_client_req(int sock, struct http_request *req,
                    int32_t timeout, void *user_data);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_HTTP_CLIENT_H_ */
```

## 88.2\_可见注释译文（Comments）

### 注释 1：原第 7 行

版权（Copyright）：© 2019 Intel Corporation。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 257 行

用户应填写以下参数。

### 注释 3：原第 371 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_HTTP_CLIENT_H_`。

## 88.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/http_2client_8h.html)
- [stdbool.h](https://docs.zephyrproject.org/latest/doxygen/html/stdbool_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [zephyr/net/net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [zephyr/net/http/parser.h](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html)
- [http_final_call](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga04fc31de51404e35b3dfab6261bb8e6d)
- [HTTP_DATA_MORE](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gga04fc31de51404e35b3dfab6261bb8e6da3f75fb095e40bfb4efd2c16059093359)
- [HTTP_DATA_FINAL](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gga04fc31de51404e35b3dfab6261bb8e6da428633ff4a67c00c67fb5cbc23269d61)
- [http_request](../network_application_model_reference/P035_http_request_结构体.md)
- [http_response](../network_application_model_reference/P043_http_response_结构体.md)
- [http_payload_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gaf46ede77bdc83602c84b9342dd8d30ed)
- [http_header_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga34a431c54c52b86618ca0e27ce3862b4)
- [http_response_cb_t](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#ga6141c94f7da92b71713079063f3426be)
- [http_parser_settings](../network_application_model_reference/P033_http_parser_settings_结构体.md)
- [http_cb](../network_application_model_reference/P043_http_response_结构体.md#af306ff4c8424b5abad76037abbfe2833)
- [cb](../network_application_model_reference/P043_http_response_结构体.md#a1936119331645bb421d4a5dc0d3fffb5)
- [uint8_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a3cb4a16b0e8d6af0af86d4fd6ba5fd9d)
- [body_frag_start](../network_application_model_reference/P043_http_response_结构体.md#a45c8596746f5a359a1e18c95838b59d9)
- [body_frag_len](../network_application_model_reference/P043_http_response_结构体.md#a58405582a11aa86892b80133f8b4fa43)
- [recv_buf](../network_application_model_reference/P043_http_response_结构体.md#aa16de8f3485062bf01b0536e64f58b46)
- [recv_buf_len](../network_application_model_reference/P043_http_response_结构体.md#a7454c5963b7bb1c5311f77971d0d1d2f)
- [data_len](../network_application_model_reference/P043_http_response_结构体.md#a4208cf209674441a25231732aad91f89)
- [content_length](../network_application_model_reference/P043_http_response_结构体.md#aedcb476d4055a7ba04516cc7a8ef800f)
- [processed](../network_application_model_reference/P043_http_response_结构体.md#a0eb2181115c753a3e1676a18d9a3ed59)
- [http_status](../network_application_model_reference/P043_http_response_结构体.md#a6bf553c9399385afeb921f6abef9a875)
- [uint16_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a5debae8b2a1ec20a6694c0c443ee399e)
- [http_status_code](../network_application_model_reference/P043_http_response_结构体.md#a94cd246204b04992712deefe51fc0c26)
- [http_content_range](../network_application_model_reference/P028_http_content_range_结构体.md)
- [content_range](../network_application_model_reference/P043_http_response_结构体.md#a1f88915f82406ae3592dec32b7430851)
- [cl_present](../network_application_model_reference/P043_http_response_结构体.md#a0d28b200a74c150e98b5fc18c61638cc)
- [body_found](../network_application_model_reference/P043_http_response_结构体.md#ac713af14995e36c1889291d12803ca18)
- [message_complete](../network_application_model_reference/P043_http_response_结构体.md#a4f107746bfff244a841b950dd84b8162)
- [cr_present](../network_application_model_reference/P043_http_response_结构体.md#ade896effa407ccdc5c9a7ef3720e66e2)
- [http_client_internal_data](../network_application_model_reference/P027_http_client_internal_data_结构体.md)
- [http_parser](../network_application_model_reference/P032_http_parser_结构体.md)
- [parser](../network_application_model_reference/P027_http_client_internal_data_结构体.md#a1620ae6631414c3ba5e462d97deca157)
- [parser_settings](../network_application_model_reference/P027_http_client_internal_data_结构体.md#a19876ea20cdca3a016d6e260e2795e83)
- [response](../network_application_model_reference/P027_http_client_internal_data_结构体.md#aa132cb0366969c04250f64075866227c)
- [user_data](../network_application_model_reference/P027_http_client_internal_data_结构体.md#a330102d665b6601949eb7331ab45d517)
- [sock](../network_application_model_reference/P027_http_client_internal_data_结构体.md#a8486d8e8b64474e75cadeb9fb166a4a5)
- [aborted](../network_application_model_reference/P027_http_client_internal_data_结构体.md#a06509a514b81f2fe72394fe147f3d86f)
- [internal](../network_application_model_reference/P035_http_request_结构体.md#abb86ccd0e0801c278ef37a78a4b7a958)
- [http_method](https://docs.zephyrproject.org/latest/doxygen/html/group__http__methods.html#gaacd5f203e33ac338ca5cb8f02a3ff3b8)
- [method](../network_application_model_reference/P035_http_request_结构体.md#adbfcd3bcaf57205360bad957a13999e6)
- [response](../network_application_model_reference/P035_http_request_结构体.md#aba8bf528f3e279d55662eedc9168d25c)
- [http_cb](../network_application_model_reference/P035_http_request_结构体.md#afbe0c199a4a58029bf2d83a0b463639c)
- [recv_buf](../network_application_model_reference/P035_http_request_结构体.md#abaabd58d149720720ffd61025d58e4a9)
- [recv_buf_len](../network_application_model_reference/P035_http_request_结构体.md#a9da5216bbd27ad54fd11368897ed660f)
- [data_len](../network_application_model_reference/P035_http_request_结构体.md#a0da554e18c6b159f55fe12e6ba9fe4ca)
- [url](../network_application_model_reference/P035_http_request_结构体.md#a6a7573252e31fddb5cad5a6764c486c1)
- [protocol](../network_application_model_reference/P035_http_request_结构体.md#a38cad3f92ed5b712f749851bbeed9a2f)
- [header_fields](../network_application_model_reference/P035_http_request_结构体.md#a775ef341a6a85b135b10786e9b4a1cbf)
- [content_type_value](../network_application_model_reference/P035_http_request_结构体.md#a1e610f06e9a8ec05cb0de382163a8c79)
- [host](../network_application_model_reference/P035_http_request_结构体.md#a3ed1146d59f33e9042fae421619df27c)
- [port](../network_application_model_reference/P035_http_request_结构体.md#abe9fdaab40cac6afb16acc2560dfe7e7)
- [payload_cb](../network_application_model_reference/P035_http_request_结构体.md#a15551f2e8c772479fb7acac20765fa12)
- [payload](../network_application_model_reference/P035_http_request_结构体.md#af201ae38024233307ed2c87684ea70d3)
- [payload_len](../network_application_model_reference/P035_http_request_结构体.md#a589615592c6c14bdecc03553c395c12f)
- [optional_headers_cb](../network_application_model_reference/P035_http_request_结构体.md#ab6fe0ec09c24302279124043e82f17ff)
- [optional_headers](../network_application_model_reference/P035_http_request_结构体.md#aa29c2bcb70011c9776c959667e10bcf5)
- [http_client_req](https://docs.zephyrproject.org/latest/doxygen/html/group__http__client.html#gaa38b6efb03f88d6959273a41b6acac81)
- [int32_t](https://docs.zephyrproject.org/latest/doxygen/html/stdint_8h.html#a0c18914b3041c2f583aba76f418399c2)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [net_ip.h](https://docs.zephyrproject.org/latest/doxygen/html/net__ip_8h.html)
- [parser.h](https://docs.zephyrproject.org/latest/doxygen/html/parser_8h.html)
- [http_client_internal_data::aborted](../network_application_model_reference/P027_http_client_internal_data_结构体.md#a06509a514b81f2fe72394fe147f3d86f)
- [http_client_internal_data::parser](../network_application_model_reference/P027_http_client_internal_data_结构体.md#a1620ae6631414c3ba5e462d97deca157)
- [http_client_internal_data::parser_settings](../network_application_model_reference/P027_http_client_internal_data_结构体.md#a19876ea20cdca3a016d6e260e2795e83)
- [http_client_internal_data::user_data](../network_application_model_reference/P027_http_client_internal_data_结构体.md#a330102d665b6601949eb7331ab45d517)
- [http_client_internal_data::sock](../network_application_model_reference/P027_http_client_internal_data_结构体.md#a8486d8e8b64474e75cadeb9fb166a4a5)
- [http_client_internal_data::response](../network_application_model_reference/P027_http_client_internal_data_结构体.md#aa132cb0366969c04250f64075866227c)
- [http_request::data_len](../network_application_model_reference/P035_http_request_结构体.md#a0da554e18c6b159f55fe12e6ba9fe4ca)
- [http_request::payload_cb](../network_application_model_reference/P035_http_request_结构体.md#a15551f2e8c772479fb7acac20765fa12)
- [http_request::content_type_value](../network_application_model_reference/P035_http_request_结构体.md#a1e610f06e9a8ec05cb0de382163a8c79)
- [http_request::protocol](../network_application_model_reference/P035_http_request_结构体.md#a38cad3f92ed5b712f749851bbeed9a2f)
- [http_request::host](../network_application_model_reference/P035_http_request_结构体.md#a3ed1146d59f33e9042fae421619df27c)
- [http_request::payload_len](../network_application_model_reference/P035_http_request_结构体.md#a589615592c6c14bdecc03553c395c12f)
- [http_request::url](../network_application_model_reference/P035_http_request_结构体.md#a6a7573252e31fddb5cad5a6764c486c1)
- [http_request::header_fields](../network_application_model_reference/P035_http_request_结构体.md#a775ef341a6a85b135b10786e9b4a1cbf)
- [http_request::recv_buf_len](../network_application_model_reference/P035_http_request_结构体.md#a9da5216bbd27ad54fd11368897ed660f)
- [http_request::optional_headers](../network_application_model_reference/P035_http_request_结构体.md#aa29c2bcb70011c9776c959667e10bcf5)
- [http_request::optional_headers_cb](../network_application_model_reference/P035_http_request_结构体.md#ab6fe0ec09c24302279124043e82f17ff)
- [http_request::response](../network_application_model_reference/P035_http_request_结构体.md#aba8bf528f3e279d55662eedc9168d25c)
- [http_request::recv_buf](../network_application_model_reference/P035_http_request_结构体.md#abaabd58d149720720ffd61025d58e4a9)
- [http_request::internal](../network_application_model_reference/P035_http_request_结构体.md#abb86ccd0e0801c278ef37a78a4b7a958)
- [http_request::port](../network_application_model_reference/P035_http_request_结构体.md#abe9fdaab40cac6afb16acc2560dfe7e7)
- [http_request::method](../network_application_model_reference/P035_http_request_结构体.md#adbfcd3bcaf57205360bad957a13999e6)
- [http_request::payload](../network_application_model_reference/P035_http_request_结构体.md#af201ae38024233307ed2c87684ea70d3)
- [http_request::http_cb](../network_application_model_reference/P035_http_request_结构体.md#afbe0c199a4a58029bf2d83a0b463639c)
- [http_response::cl_present](../network_application_model_reference/P043_http_response_结构体.md#a0d28b200a74c150e98b5fc18c61638cc)
- [http_response::processed](../network_application_model_reference/P043_http_response_结构体.md#a0eb2181115c753a3e1676a18d9a3ed59)
- [http_response::cb](../network_application_model_reference/P043_http_response_结构体.md#a1936119331645bb421d4a5dc0d3fffb5)
- [http_response::content_range](../network_application_model_reference/P043_http_response_结构体.md#a1f88915f82406ae3592dec32b7430851)
- [http_response::data_len](../network_application_model_reference/P043_http_response_结构体.md#a4208cf209674441a25231732aad91f89)
- [http_response::body_frag_start](../network_application_model_reference/P043_http_response_结构体.md#a45c8596746f5a359a1e18c95838b59d9)
- [http_response::message_complete](../network_application_model_reference/P043_http_response_结构体.md#a4f107746bfff244a841b950dd84b8162)
- [http_response::body_frag_len](../network_application_model_reference/P043_http_response_结构体.md#a58405582a11aa86892b80133f8b4fa43)
- [http_response::http_status](../network_application_model_reference/P043_http_response_结构体.md#a6bf553c9399385afeb921f6abef9a875)
- [http_response::recv_buf_len](../network_application_model_reference/P043_http_response_结构体.md#a7454c5963b7bb1c5311f77971d0d1d2f)
- [http_response::http_status_code](../network_application_model_reference/P043_http_response_结构体.md#a94cd246204b04992712deefe51fc0c26)
- [http_response::recv_buf](../network_application_model_reference/P043_http_response_结构体.md#aa16de8f3485062bf01b0536e64f58b46)
- [http_response::body_found](../network_application_model_reference/P043_http_response_结构体.md#ac713af14995e36c1889291d12803ca18)
- [http_response::cr_present](../network_application_model_reference/P043_http_response_结构体.md#ade896effa407ccdc5c9a7ef3720e66e2)
- [http_response::content_length](../network_application_model_reference/P043_http_response_结构体.md#aedcb476d4055a7ba04516cc7a8ef800f)
- [http_response::http_cb](../network_application_model_reference/P043_http_response_结构体.md#af306ff4c8424b5abad76037abbfe2833)

---

[上一章](P087_hpack.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P089_i2s.h_源码浏览.md)
